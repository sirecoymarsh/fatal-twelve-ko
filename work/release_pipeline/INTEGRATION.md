# Fatal Twelve Korean patch release pipeline

This directory builds a reversible, hash-bound Windows patch. The public archive is created only from an explicit list of compiled `game/*.rpyc` files. It never walks or packages a game installation, translation workspace, log, save, backup, or source `.rpy` tree.

## Non-negotiable isolation

- Never invoke the executable in the installed baseline game.
- First prove the baseline tree against the original distribution ZIP with `audit_live_against_original_zip.py`.
- Copy only `fatal.exe`, `fatal.py`, `lib/**`, and `renpy/**` to a disjoint engine root with `prepare_isolated_engine.py`.
- Persist a full baseline snapshot before any copied engine process starts.
- Every engine process receives process-scoped `SDL_AUDIODRIVER=dummy`; `PYTHONHASHSEED=0` is also set for compilation.
- The stage, copied engine, clean payload, reports, public release, installer backup/state/recovery roots, and baseline game must be pairwise disjoint.

## Final build order

1. Assemble a brand-new source stage with `assemble_final_stage.py`. Bind the exact frozen pipeline-result, render-manifest, global-strings, bootstrap, language-slot, and `script_version.txt` hashes. Do not reuse a stage that has ever contained an older render.
2. Generate or review `final_release_config.json`. Every payload target must be a canonical `game/*.rpyc` path in `payload_allowlist.txt`; the supported baseline profile must enumerate the complete exact pre-state combination.
3. Create a brand-new isolated engine copy:

   ```powershell
   python .\prepare_isolated_engine.py `
     --baseline-game-root <read-only-game-root> `
     --engine-root <new-isolated-engine-root> `
     --expected-baseline-tree-sha256 <trusted-full-tree-sha256> `
     --report <isolated-engine-manifest.json>
   ```

4. Compile and extract the clean payload. `prepare_compiled_payload.ps1` is a thin PowerShell 5.1-compatible guard around the Python orchestrator; it requires separate baseline and engine roots:

   ```powershell
   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\prepare_compiled_payload.ps1 `
     -BaselineGameRoot <read-only-game-root> `
     -EngineRoot <isolated-engine-root> `
     -EngineManifest <isolated-engine-manifest.json> `
     -ExpectedBaselineTreeSha256 <trusted-full-tree-sha256> `
     -StageRoot <fresh-stage-root> `
     -ReleaseConfig <final-release-config.json> `
     -CleanPayloadRoot <new-clean-payload-root> `
     -ReportPath <compile-payload-report.json>
   ```

   The orchestrator verifies the isolated-engine manifest before launch, saves full live-tree before/after snapshots and a diff, checks baseline anchors before/after, records copied-engine mutations, rejects error artifacts and unexpected compiled files, and promotes exactly the allowlisted `.rpyc` files.

5. Build twice into separate empty directories:

   ```powershell
   python .\build_release.py --config <config> --payload-root <clean-payload> --output-dir <build-a>
   python .\build_release.py --config <config> --payload-root <clean-payload> --output-dir <build-b>
   ```

   Require identical ZIP bytes, fixed timestamps/order/modes, exact public file set, and a valid external ZIP SHA-256 sidecar.

6. Run `tests/run_final_package_fixture.py` against the actual final ZIP and a disposable baseline fixture. It exercises pristine install, idempotent install/restore, payload and baseline tamper rejection, Nth-replacement rollback, forced-interruption journal recovery, recovery-copy tamper rejection, Unicode/space paths, and Windows PowerShell 5.1 without launching the game.
7. Scan both the final ZIP and its exact extracted package with Microsoft Defender, then regenerate `final_release_evidence.json` and `pipeline_integrity.json`.

## Public vs external state

The ZIP contains only the installer/restorer module and entry scripts, Korean README, generated install manifest/sidecar, and allowlisted `.rpyc` payload. Installer backup, state, journal, recovery, and any user-review-only overlay stay outside both the game and package trees. Restore reproduces the exact supported pre-install state, including absent targets.