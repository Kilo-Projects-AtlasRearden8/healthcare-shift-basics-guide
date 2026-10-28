# STATUS

## What was built

A beginner manual and static HTML site on healthcare shift basics, published by Asdale Dynamics, LLC.

**Files**
- `README.md` — overview, credits Asdale Dynamics, LLC, education-only / never medical advice notices
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `AGENTS.md` — project conventions (education only, no secrets, no `.github/workflows`, plain commits)
- `docs/handoffs.md` — handoff basics, SBAR/I-PASS, what to include, privacy reminders
- `docs/report-sheets.md` — report sheet contents, usage tips, blank practice template
- `docs/break-planning.md` — planning breaks, coverage, facility policy
- `docs/shift-recovery.md` — post-shift recovery, sleep, support resources, error reporting
- `docs/shift-prep-checklist.md` — printable shift-prep checklist (before shift, arrival, handoff, mid-shift, end of shift, after shift)
- `docs/ai-notes-aids.md` — education-only AI aids for drafting notes, strict privacy limits, fictional practice example
- `site/index.html` — static HTML site with printable shift-prep checklist, AI note aids, and links to manual topics
- `site/style.css` — site styles, including print-only styles that hide navigation when printing

**Content safeguards**
- Every docs page and the site carry an "Education only. Never medical advice. Follow facility policy" notice.
- AI note aids never use real patient data; examples are explicitly fictional.
- No secrets, API keys, or personal data in any file.
- No `.github/workflows` directory.

## How to run it

- Read the manual: open any file in `docs/` with a Markdown reader or text editor.
- Use the site: open `site/index.html` in any browser. No build step, no server, no dependencies — it is a static HTML file with inline-linked CSS.
- Print the checklist: open `site/index.html` and use the browser print command (Ctrl+P / Cmd+P). Print styles hide the header/navigation and show a clean checklist.
- The site works offline and locally first.

## Verification results

- `site/index.html` parses with zero HTML parser errors.
- `LICENSE` line 3 is exactly `Copyright (c) 2026 Asdale Dynamics, LLC`.
- `README.md` credits Asdale Dynamics, LLC (multiple occurrences).
- Secret scan (`api key`, `sk-`, `secret`, `password`, `token`): no actual secrets found (only the word "secret" in AGENTS.md project convention text).
- No `.github/workflows` directory present.
- Git initialized and committed as `03b6897` with plain message, no Co-authored-by trailer, no remote, no push.

## Known gaps

- No automated test suite or linter configured (static site and Markdown docs have no build step); verification was manual parsing and grep scans.
- Print styles were not validated against an actual printer; browser print preview is the recommended check.
- Docs are Markdown only; no rendered HTML versions of the `docs/` pages exist in the repo.
- Content is general education; facilities may have specific forms, formats, or policies that differ — users must follow their own facility's policy.
