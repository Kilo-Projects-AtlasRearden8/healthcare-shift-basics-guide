# STATUS

## What was built

A beginner manual and static HTML site on healthcare shift basics, published by Asdale Dynamics, LLC.

**Files**
- `README.md` — polished, beginner-friendly overview: who this is for, what's inside, step-by-step how-to-use, important notices, Asdale Dynamics, LLC credit, license
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `AGENTS.md` — project conventions (education only, no secrets, no `.github/workflows`, plain commits)
- `docs/handoffs.md` — handoff basics, SBAR/I-PASS, what to include, how to give/receive report, privacy reminders
- `docs/report-sheets.md` — report sheet contents, usage tips, blank practice template (fake patient only)
- `docs/break-planning.md` — planning breaks during a shift, coverage, facility policy
- `docs/shift-recovery.md` — post-shift recovery, sleep, support resources, error/near-miss reporting
- `docs/shift-prep-checklist.md` — printable shift-prep checklist (before shift, arrival, handoff, mid-shift, end of shift, after shift)
- `docs/ai-notes-aids.md` — education-only AI aids for drafting notes, strict privacy limits, fictional practice example
- `site/index.html` — static HTML site: printable shift-prep checklist, AI note aids, links to manual topics
- `site/style.css` — site styles including print styles that hide navigation when printing
- `tests/validate.py` — validation script (HTML parse, exact LICENSE line, README credit, no workflows, no secrets)

**Content safeguards**
- Every docs page and the site carry an "Education only. Never medical advice. Follow facility policy" notice.
- AI note aids never use real patient data; examples are explicitly fictional.
- No secrets, API keys, or personal data in any file (validation script confirms).
- No `.github/workflows` directory.

## How to run it

- Read the manual: open any file in `docs/` with a text editor or Markdown reader.
- Use the site: open `site/index.html` in any browser. No build step, no server, no dependencies, works offline/local-first.
- Print the checklist: open `site/index.html` and use the browser print command (Ctrl+P / Cmd+P). Print styles hide the header/navigation for a clean copy.
- Run validation: `python3 tests/validate.py`

## Verification results

`python3 tests/validate.py` — VALIDATION PASSED
- `site/index.html` parses with zero HTML parser errors
- `site/style.css` braces balanced (40 open / 40 close)
- `LICENSE` line is exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` credits Asdale Dynamics, LLC
- No `.github/workflows` directory present
- No high-signal secret patterns (API keys, tokens, private keys) found in files
- Git initialized and committed; tree clean; no remote, no push

## Known gaps

- Docs are Markdown only; no rendered HTML versions of the `docs/` pages exist in the repo (the `site/` HTML is self-contained for the checklist and note aids).
- Print styles were not validated against a physical printer; browser print preview is the recommended check.
- Content is general education; facilities may have specific forms, formats, or policies that differ — users must follow their own facility's policy.
- No test runner framework; validation is a single Python script appropriate for a static Markdown/HTML project.
