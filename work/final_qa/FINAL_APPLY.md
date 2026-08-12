# Final correction apply contract

run_final_apply.py is the one-shot, no-game-execution text pipeline. It
combines the immutable 29-scenario master index with the separately reviewed
732-key/739-context system UI master, canonicalizes hash-bound reviewer
corrections, rebases the guarded structural overlay, applies only exact
record-bound QA approvals, merges the 12 composed-Numeral keys, and renders the
final RPY set.

## Global manifest schema

    {
      "schema_version": "fatal-twelve-global-correction-manifest-v1",
      "correction_files": [
        {
          "reviewer": "A",
          "path": "work/final_qa/reviews/A.final.jsonl",
          "sha256": "<64 hex>",
          "records": 123
        }
      ],
      "structural_overlay": {
        "path": "work/final_qa/reviews/structural_fixes_spec.json",
        "sha256": "<64 hex>",
        "records": 178
      },
      "approval_ledger": {
        "path": "work/final_qa/reviews/qa_approvals.draft.json",
        "sha256": "<64 hex>",
        "records": 10
      },
      "supplemental_strings": [
        {
          "path": "work/system_ui/runtime_application/numeral_composed_string_keys.ko.rpy",
          "sha256": "b8b8bd0fb905f3346811fa36356f144874f2bf874cf92bdca2e0185da488f6dc",
          "pairs": 12
        }
      ]
    }

Paths may be absolute or repository-root-relative. Each SHA and optional record
count is an exact guard. correction_files may contain several files for one
reviewer; exact duplicate stable IDs collapse, but any semantic conflict aborts.
The structural overlay is not passed as a second correction: it must exactly
match expected_after_semantic, then replaces or creates the one canonical
stable-ID correction row.

Approval entries are accepted only when stable_id, script, sequence,
source_sha256, final target_sha256, rule_id, reviewer, and reason match exactly
one current audit finding. Blanket approvals are forbidden.

## Commands

Preflight and materialize canonical reviewer JSONLs only:

    python .\work\final_qa\run_final_apply.py --manifest .\work\final_qa\reviews\global_correction_manifest.json --output-root .\work\final_qa\final_text_preflight --preflight-only

Full correction, scenario audit, approval application, and final RPY render:

    python .\work\final_qa\run_final_apply.py --manifest .\work\final_qa\reviews\global_correction_manifest.json --output-root .\work\final_qa\final_text_build

The output root must be absent or empty. The wrapper never starts the game. It
requires these exact final render counts:

- 30 input masters: 29 scenario plus 1 system UI
- 18,916 records: 18,184 scenario plus 732 UI
- 18,126 translate blocks
- 790 master string occurrences
- 785 unique master decoded old keys
- 12 supplemental composed-Numeral keys
- 797 total emitted unique decoded old keys
- zero old-key target conflicts