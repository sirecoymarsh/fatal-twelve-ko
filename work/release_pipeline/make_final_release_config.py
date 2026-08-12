#!/usr/bin/env python3
"""Create the final additive-patch config from a trusted read-only game tree.

The payload path list is explicit (one canonical game/*.rpyc path per line).
Every target must be absent in the trusted baseline; supporting a previous or
mixed patch requires a separately reviewed manual config.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath


KNOWN_ANCHORS = {
    "fatal.exe": "987b9a1d43e46b8665a0cc4c6280459ef3d13c365fba8ba0b55a88e9f03f43bd",
    "game/scenario.rpa": "ea39387ae13432a79ffe4601af7b50478d063432ce3b7bc4013c92e09f036d22",
    "game/system.rpa": "a298b88f12c98435b015a647b51f5a35987ea4d714b5bf92e90972f3fcf6b648",
    "game/tl.rpa": "ad628d5aa7b0601e69fa99c13d6f67c21854ae0a290599dc478a986cfc53ac5f",
    "game/localize.rpyc": "5ba31f69d3646990d42e7044d97bf4cfb07bc105619b4f220fdcf1ad374d1d2f",
}
VERSION_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical_payload(value: str) -> str:
    if not value or "\\" in value or ":" in value:
        raise ValueError(f"invalid payload path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        raise ValueError(f"invalid payload path: {value!r}")
    result = path.as_posix()
    if result != value or not result.startswith("game/") or not result.lower().endswith(".rpyc"):
        raise ValueError(f"payload must be canonical game/*.rpyc: {value!r}")
    return result


def load_allowlist(path: Path) -> list[str]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("allowlist must be UTF-8 without BOM")
    lines = raw.decode("utf-8").splitlines()
    values = [canonical_payload(line.strip()) for line in lines if line.strip() and not line.lstrip().startswith("#")]
    if not values:
        raise ValueError("payload allowlist is empty")
    folded: set[str] = set()
    for value in values:
        key = value.casefold()
        if key in folded:
            raise ValueError(f"duplicate/case-colliding payload path: {value}")
        folded.add(key)
    return sorted(values)


def build_config(game_root: Path, allowlist_path: Path, version: str) -> dict:
    if not VERSION_RE.fullmatch(version):
        raise ValueError("release version contains unsupported characters")
    game_root = game_root.resolve(strict=True)
    if not game_root.is_dir():
        raise ValueError("game root is not a directory")
    payload_paths = load_allowlist(allowlist_path)
    anchors = []
    for rel, expected in KNOWN_ANCHORS.items():
        path = game_root.joinpath(*PurePosixPath(rel).parts)
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"trusted anchor missing or unsafe: {rel}")
        actual = sha256_file(path)
        if actual != expected:
            raise ValueError(f"trusted anchor hash rejected: {rel}: {actual}")
        anchors.append({
            "path": rel,
            "accepted": [{"id": "trusted-original", "size": path.stat().st_size, "sha256": actual}],
        })
    for rel in payload_paths:
        target = game_root.joinpath(*PurePosixPath(rel).parts)
        if target.exists():
            raise ValueError(
                f"additive pristine profile requires an absent target, but this path exists: {rel}; "
                "use a separately reviewed exact mixed/upgrade profile instead"
            )
    return {
        "patch_id": "fatal-twelve-ko",
        "release_version": version,
        "release_root_name": f"FatalTwelve_KoreanPatch_{version}",
        "game": {
            "display_name": "Fatal Twelve",
            "process_executable_relative_path": "fatal.exe",
            "anchors": anchors,
        },
        "payload_allowlist": [
            {
                "path": rel,
                "role": "compiled Korean localization",
                "pre_states": [{"id": "absent", "kind": "absent"}],
            }
            for rel in payload_paths
        ],
        "supported_prestate_profiles": [
            {
                "id": "trusted-pristine",
                "description": "Every additive Korean .rpyc target is absent in the trusted original game.",
                "states": [{"path": rel, "state_id": "absent"} for rel in payload_paths],
            }
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game-root", required=True, type=Path)
    parser.add_argument("--payload-allowlist", required=True, type=Path)
    parser.add_argument("--release-version", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        config = build_config(args.game_root, args.payload_allowlist, args.release_version)
        output = args.output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(config, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8", newline="\n")
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"CONFIG REJECTED: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"status": "PASS", "payload_count": len(config["payload_allowlist"])}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
