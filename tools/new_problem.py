#!/usr/bin/env python3
"""Instantiate the _template skeleton as problems/<slug>/.

Usage: python3 tools/new_problem.py <slug> --title "Problem name" [--question "..."]
"""
import argparse
import datetime
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug", help="kebab-case folder name, e.g. conway-99-graph")
    parser.add_argument("--title", required=True)
    parser.add_argument("--question", default="TODO: one-line form of the question")
    args = parser.parse_args()

    dest = ROOT / "problems" / args.slug
    if dest.exists():
        sys.exit(f"problems/{args.slug} already exists.")

    shutil.copytree(ROOT / "_template", dest)
    today = datetime.date.today().isoformat()
    subs = {
        "{{SLUG}}": args.slug,
        "{{TITLE}}": args.title,
        "{{QUESTION}}": args.question,
        "{{DATE}}": today,
    }
    for path in dest.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".toml", ".cff", ".bib"}:
            text = path.read_text()
            for key, value in subs.items():
                text = text.replace(key, value)
            path.write_text(text)

    print(f"Created problems/{args.slug}/ — now fill in PROBLEM.md, then run tools/board.py.")


if __name__ == "__main__":
    main()
