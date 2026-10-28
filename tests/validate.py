#!/usr/bin/env python3
"""Validate the healthcare-shift-basics-guide project.

Checks:
- site/index.html parses as HTML with no parser errors
- LICENSE contains the exact copyright line
- README credits Asdale Dynamics, LLC
- No .github/workflows directory exists
- No high-signal secret patterns (API keys, tokens, private keys) in files
"""
import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []


def fail(msg):
    ERRORS.append(msg)
    print("FAIL: " + msg)


def pass_check(msg):
    print("ok: " + msg)


def validate_html():
    path = os.path.join(ROOT, "site", "index.html")
    if not os.path.exists(path):
        fail("site/index.html missing")
        return
    with open(path, encoding="utf-8") as f:
        content = f.read()

    class Parser(html.parser.HTMLParser):
        def __init__(self):
            super().__init__()
            self.errors = []

        def error(self, message):
            self.errors.append(message)

    parser = Parser()
    try:
        parser.feed(content)
    except Exception as exc:  # pragma: no cover - defensive
        fail("site/index.html raised while parsing: %s" % exc)
        return
    if parser.errors:
        for err in parser.errors:
            fail("site/index.html parse error: " + err)
    else:
        pass_check("site/index.html parses with no HTML errors")


def validate_license():
    path = os.path.join(ROOT, "LICENSE")
    if not os.path.exists(path):
        fail("LICENSE missing")
        return
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    target = "Copyright (c) 2026 Asdale Dynamics, LLC"
    if target in lines:
        pass_check("LICENSE has exact copyright line")
    else:
        fail("LICENSE missing exact line: " + target)


def validate_readme():
    path = os.path.join(ROOT, "README.md")
    if not os.path.exists(path):
        fail("README.md missing")
        return
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if "Asdale Dynamics, LLC" in content:
        pass_check("README credits Asdale Dynamics, LLC")
    else:
        fail("README does not credit Asdale Dynamics, LLC")


def validate_no_workflows():
    path = os.path.join(ROOT, ".github", "workflows")
    if os.path.exists(path):
        fail(".github/workflows directory exists (should not)")
    else:
        pass_check("no .github/workflows directory")


def validate_no_secrets():
    # High-signal patterns that indicate a real leaked secret, not policy text.
    patterns = [
        re.compile(r"sk-[A-Za-z0-9]{20,}"),          # OpenAI-style keys
        re.compile(r"AKIA[0-9A-Z]{16}"),             # AWS access key ids
        re.compile(r"ghp_[A-Za-z0-9]{36,}"),         # GitHub personal access tokens
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),  # private keys
    ]
    hits = []
    for dirpath, _dirs, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for name in files:
            fpath = os.path.join(dirpath, name)
            try:
                with open(fpath, encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except (OSError, UnicodeDecodeError):
                continue
            for pat in patterns:
                for _m in pat.finditer(content):
                    hits.append(fpath)
                    break
    if hits:
        for h in hits:
            fail("possible secret in " + os.path.relpath(h, ROOT))
    else:
        pass_check("no high-signal secret patterns found")


def main():
    validate_html()
    validate_license()
    validate_readme()
    validate_no_workflows()
    validate_no_secrets()

    print()
    if ERRORS:
        print("VALIDATION FAILED (%d error(s))" % len(ERRORS))
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
