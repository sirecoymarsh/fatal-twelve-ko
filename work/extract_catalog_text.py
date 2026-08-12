from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("catalog", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    records = [
        json.loads(line)
        for line in args.catalog.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    lines: list[str] = []
    for record in records:
        speaker = record.get("speaker")
        speaker_code = speaker.get("code") if speaker else "narrator"
        text = record["source"]["text_ja"].replace("\t", "\\t").replace("\r", "\\r").replace("\n", "\\n")
        lines.append(f'{record["command_index"]}\t{speaker_code}\t{text}')
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
