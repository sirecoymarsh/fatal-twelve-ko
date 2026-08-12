# Fatal Twelve Korean glyph coverage

- Verdict: **PASS**
- Missing font/codepoint pairs: **0**
- Missing unique code points: **0**
- Required visible code points: **1368**
- Corrected master records: **18916**
- Rendered global string targets: **797**
- Game executed: **false**

## Shipped font results

| Role | Archive entry | Glyphs | Required | Missing | cmap formats |
|---|---|---:|---:|---:|---|
| body | `gui/fonts/NotoSansCJKjp-Regular.otf` | 65535 | 1368 | 0 | 4, 12 |
| emphasis | `gui/fonts/NotoSansCJKjp-Medium.otf` | 65535 | 1368 | 0 | 4, 12 |

The audit read the font bytes directly from the shipped `system.rpa`,
accepted only Unicode cmap format 4/12 mappings whose glyph ID is in
`1..numGlyphs-1`, retained both Ren'Py ruby base and ruby reading text,
and did not start the game.

- JSON report: `C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc\work\final_qa\final_text_build_ui_feedback_v2\audit\final_glyph_coverage.json`
- JSON SHA-256: `e75c8728866da3723a7fd400cfb3a92747c71a9052475fc198d342459e54734b`
