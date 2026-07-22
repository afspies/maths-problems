#!/usr/bin/env python3
"""Mint or update a per-problem Zenodo DOI.

Bundles problems/<slug>/{writeup/,certificates/,PROBLEM.md,STATUS.toml} into a
tarball and uploads it as a Zenodo deposition. Each problem subfolder gets its
own concept DOI; subsequent releases of the same problem create new versions.

Usage:
  python3 tools/release.py <slug> --version v1 [--dry-run] [--sandbox]

Requires ZENODO_TOKEN in the environment (a Zenodo personal access token with
deposit:write + deposit:actions). --sandbox targets sandbox.zenodo.org for
testing. --dry-run builds the bundle and prints the metadata without uploading.

On success, writes the minted DOI into the problem's STATUS.toml (`doi = ...`)
and appends it to writeup/CITATION.cff. Rerun tools/board.py afterwards.

Precondition: the repo must be public before a DOI is worth minting (the DOI
should resolve to something a reader can see), and the result must be verified
and written up. Do not release drafts.
"""
import argparse
import json
import os
import re
import sys
import tarfile
import tomllib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def api(base, token, method, path, payload=None, data=None, content_type="application/json"):
    url = f"{base}{path}"
    body = None
    if payload is not None:
        body = json.dumps(payload).encode()
    elif data is not None:
        body = data
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    if body is not None:
        req.add_header("Content-Type", content_type)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read() or b"{}")


def build_bundle(slug, version, scratch):
    problem = ROOT / "problems" / slug
    if not problem.is_dir():
        sys.exit(f"No such problem: problems/{slug}")
    bundle = scratch / f"{slug}-{version}.tar.gz"
    with tarfile.open(bundle, "w:gz") as tar:
        for rel in ["PROBLEM.md", "STATUS.toml", "writeup", "certificates"]:
            path = problem / rel
            if path.exists():
                tar.add(path, arcname=f"{slug}-{version}/{rel}")
    return bundle


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    parser.add_argument("--version", required=True, help="e.g. v1")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--sandbox", action="store_true")
    args = parser.parse_args()

    problem = ROOT / "problems" / args.slug
    status_file = problem / "STATUS.toml"
    with open(status_file, "rb") as fh:
        status = tomllib.load(fh)

    title = f"{status.get('title', args.slug)} — results ({args.version})"
    description = (
        f"Verified artifacts and write-up for the problem '{status.get('title', args.slug)}' "
        f"({status.get('question', '')}) from the maths-problems repository "
        f"(https://github.com/afspies/maths-problems), problem folder problems/{args.slug}/. "
        f"Best result at release: {status.get('best_result', 'see writeup')}."
    )
    metadata = {
        "metadata": {
            "title": title,
            "upload_type": "dataset",
            "description": description,
            "creators": [{"name": "Spies, Alex"}],
            "version": args.version,
            "keywords": ["mathematics", "open problems", "certificates", args.slug],
        }
    }

    scratch = ROOT / "scratch"
    scratch.mkdir(exist_ok=True)
    bundle = build_bundle(args.slug, args.version, scratch)
    print(f"Bundle: {bundle} ({bundle.stat().st_size} bytes)")
    print(json.dumps(metadata, indent=2))

    if args.dry_run:
        print("--dry-run: not uploading.")
        return

    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        sys.exit("ZENODO_TOKEN not set.")
    base = "https://sandbox.zenodo.org/api" if args.sandbox else "https://zenodo.org/api"

    existing_doi = status.get("doi", "")
    if existing_doi:
        m = re.search(r"zenodo\.(\d+)", existing_doi)
        if not m:
            sys.exit(f"Cannot parse existing DOI {existing_doi!r} for versioning.")
        dep = api(base, token, "POST", f"/deposit/depositions/{m.group(1)}/actions/newversion")
        dep_id = dep["links"]["latest_draft"].rstrip("/").rsplit("/", 1)[-1]
        api(base, token, "PUT", f"/deposit/depositions/{dep_id}", payload=metadata)
    else:
        dep = api(base, token, "POST", "/deposit/depositions", payload=metadata)
        dep_id = dep["id"]

    bucket = api(base, token, "GET", f"/deposit/depositions/{dep_id}")["links"]["bucket"]
    with open(bundle, "rb") as fh:
        req = urllib.request.Request(f"{bucket}/{bundle.name}", data=fh.read(), method="PUT")
        req.add_header("Authorization", f"Bearer {token}")
        req.add_header("Content-Type", "application/octet-stream")
        urllib.request.urlopen(req)

    published = api(base, token, "POST", f"/deposit/depositions/{dep_id}/actions/publish")
    doi = published["doi"]
    print(f"Published DOI: {doi}")

    text = status_file.read_text()
    if re.search(r"^doi\s*=", text, flags=re.M):
        text = re.sub(r'^doi\s*=.*$', f'doi = "{doi}"', text, flags=re.M)
    else:
        text += f'\ndoi = "{doi}"\n'
    status_file.write_text(text)

    cff = problem / "writeup" / "CITATION.cff"
    if cff.exists() and "doi:" not in cff.read_text():
        with open(cff, "a") as fh:
            fh.write(f"identifiers:\n  - type: doi\n    value: {doi}\n")

    print("STATUS.toml and writeup/CITATION.cff updated — rerun tools/board.py and commit.")


if __name__ == "__main__":
    main()
