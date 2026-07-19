---
name: manage-cheongrok-velog
description: Operate and evolve the Cheongrok (청록) Velog review workspace at C:\Discovery\Cosmo\dev\lab\velog while preserving existing evaluations. Use when Codex is asked to open the Cheongrok evaluation page, review a Velog post against the charter, save or inspect dated review notes, maintain index.html/history.html/records.json/server.py, or improve the project's evaluation dashboards and visualizations.
---

# Manage Cheongrok Velog

Use the Cheongrok charter to review writing, operate the local evaluation UI, preserve its records, and evolve its visual analysis.

## Establish context

1. Use `C:\Discovery\Cosmo\dev\lab\velog` as the default project root. If the active workspace differs, report the mismatch before writing.
2. Read the root `AGENTS.md` completely before changing the project.
3. Inspect `index.html`, `history.html`, `records.json`, `server.py`, `assets/`, and `note/` files relevant to the request.
4. Read [references/cheongrok-charter.md](references/cheongrok-charter.md) when reviewing a post, changing the data contract, or extending visualization semantics.
5. Preserve unrelated user changes and all existing records.

## Choose the workflow

### Open the evaluation workspace

1. Confirm port 8081 is free or identify the existing Cheongrok server.
2. Run `python server.py` from the project root.
3. Open `http://localhost:8081/index.html` in the available browser.
4. Keep the server running while the user evaluates. Stop only a server started for temporary agent validation; do not stop a user-owned session without being asked.
5. Never choose rankings or submit a review on the user's behalf unless the user supplied those exact values or explicitly requested agent evaluation.

### Review a Velog draft

1. Read the supplied draft or URL using the appropriate document, browser, or web capability.
2. Evaluate the three-part flow: observation → analysis → implementation.
3. Assess the intended balance: research 65%, development 30%, blog narrative 5%.
4. Review all nine charter criteria and distinguish evidence from inference.
5. Return concrete revision suggestions, source gaps, reproducibility gaps, and a proposed ranking. Treat the ranking as a proposal until the user accepts or saves it.

### Save and inspect evaluations

- Treat `records.json` as the structured source for the UI and statistics.
- Treat `note/YYYY/YYYY-MM-DD.md` as the human-readable review record.
- Save through `POST /api/records` or the evaluation form so both representations update together.
- Keep the current one-record-per-date behavior unless the user requests multiple posts per day. For that extension, introduce a stable record ID and migration rather than silently changing date semantics.
- Do not overwrite, reset, or hand-edit historical records without inspecting and preserving their existing fields.

### Improve the interface or visualization

1. Keep shared charter data in `assets/charter.js`, shared presentation in `assets/styles.css`, evaluation behavior in `assets/app.js`, and analysis behavior in `assets/history.js`.
2. Derive charts from record IDs and numeric ranks; tolerate legacy records with missing optional fields.
3. Support empty, one-record, and many-record states.
4. Prefer accessible HTML and native SVG for durable local visualization. Add external libraries only when their benefit exceeds offline and maintenance costs.
5. Preserve keyboard controls, responsive layout, Korean UTF-8 text, and HTML escaping.
6. Use the `visualize` skill for rapid interactive chart exploration when useful. If Figma is installed and the user wants design-system exploration or handoff, use Figma before production implementation.

## Validate changes

- Parse `records.json` without modifying it unless a save test is explicitly authorized.
- Run Python syntax and validation checks for `server.py`.
- Run `node --check` for JavaScript files.
- Verify `/api/records`, `index.html`, and `history.html` over the local server.
- Test ranking movement, optional review memo, empty-history behavior, and console errors.
- Check desktop and mobile layouts for horizontal overflow.
- Confirm a saved record produces matching JSON and Markdown content. Use a disposable test date only with explicit permission, then restore data safely.

## Report the result

State which records were preserved, which files changed, what was verified, and whether a server remains running. Mention the exact note path when an evaluation was saved.
