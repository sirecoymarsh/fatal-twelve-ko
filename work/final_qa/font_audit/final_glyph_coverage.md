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

- JSON report: `C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc\work\final_qa\font_audit\final_glyph_coverage.json`
- JSON SHA-256: `502a517a712ccf94dad27ce23b1ab1c272b8b30ce46509e1447241b4cc070bf2`
