"""Generate a redirect map from openMINDS schema type URIs
to their rendered documentation pages on Read the Docs.

Run this script after cloning/building the schema sources:

    python -m pipeline.redirect_map

It produces a JSON file named `redirect_map.json` in the project root, e.g.

    "/types/Subject": "https://openminds.om-i.org/en/latest/schema_specifications/core/research/subject.html#subject"

Serve the resulting map with your static-site host or edge platform
(e.g. Netlify, Vercel, Cloudflare Workers) to perform the redirects.
"""

from __future__ import annotations

import json
import os
from typing import Dict

from pipeline.utils import clone_sources, SchemaLoader, InstanceLoader
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Helper functions

def _pluralize(term: str) -> str:
    """Return an English plural for simple openMINDS instance types."""
    if term.endswith("s"):
        return f"{term}es"
    if term.endswith("y"):
        return f"{term[:-1]}ies"
    return f"{term}s"


def _anchorize(name: str) -> str:
    """Convert an instance name to the anchor used in HTML (lower-case, '_' and '.' → '-')."""
    return name.replace("_", "-").replace(".", "-").lower()

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

DOCS_BASE_URL = "https://openminds.om-i.org"  # without trailing slash
DOCS_VERSION_SLUG = "latest"                  # RTD version alias to use
OUTPUT_FILENAME = ".htaccess"                 # output path (project root)


# ---------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------


def generate_redirect_map() -> Dict[str, str]:
    """
    Return a {uri -> url} mapping for *all* schema types discovered
    across all versions in the openMINDS sources.
    """
    # Ensure fresh sources
    clone_sources()

    loader = SchemaLoader()
    redirect_map: Dict[str, str] = {}

    # Track which version each schema appears in (prefer latest available)
    schema_versions = {}
    
    # Process versions in priority order: latest first, then highest version numbers
    all_versions = loader.get_schema_versions()
    ordered_versions = []
    if "latest" in all_versions:
        ordered_versions.append("latest")
    # Sort versioned releases in descending order (v4.0, v3.0, v2.0, v1.0)
    versioned = [v for v in all_versions if v.startswith("v") and v != "latest"]
    versioned.sort(reverse=True)
    ordered_versions.extend(versioned)
    
    for version in ordered_versions:
        abs_paths = loader.find_schemas(version)
        rel_paths = loader.get_relative_paths_for_schema_docu(abs_paths, version)

        for schema_name, rel_path in rel_paths.items():
            # Only record if we haven't seen this schema yet (prioritizes earlier processed versions)
            if schema_name not in schema_versions:
                schema_versions[schema_name] = {
                    "version": version,
                    "rel_path": rel_path
                }

    # Generate URLs using the appropriate version for each schema
    for schema_name, info in schema_versions.items():
        uri = f"/types/{schema_name}"
        version_slug = DOCS_VERSION_SLUG if info["version"] == "latest" else info["version"]
        url = (
            f"{DOCS_BASE_URL}/en/{version_slug}/schema_specifications/"
            f"{info['rel_path']}.html#{schema_name.lower()}"
        )
        redirect_map[uri] = url

    # ----------------------------------------------------------
    # Instance redirects
    # ----------------------------------------------------------
    iloader = InstanceLoader()
    simple_types = {"brainAtlases", "contentTypes", "commonCoordinateSpaces", "licenses"}
    subpage_types = {"parcellationEntities", "brainAtlasVersions", "commonCoordinateSpaceVersions"}
    subpage2_types = {"parcellationEntityVersions"}

    for version in iloader.get_instance_versions():
        abs_paths = iloader.find_instances(version)
        base_dir = os.path.join(iloader.instances_sources, version)
        for ap in abs_paths:
            rel = os.path.relpath(ap, start=base_dir)
            inst_type = rel.split(os.sep)[0]
            filename = os.path.basename(ap).replace(".jsonld", "")
            plural = _pluralize(inst_type)

            # Determine page location based on instance type
            if inst_type in simple_types:
                page_path = f"instance_libraries/{inst_type}.html"
            elif inst_type in subpage_types:
                page_heading = filename.split("_")[0]
                page_path = f"instance_libraries/{inst_type}/{page_heading}.html"
            elif inst_type in subpage2_types:
                page_heading = "_".join(filename.split("_")[:2])
                page_path = f"instance_libraries/{inst_type}/{page_heading}.html"
            else:
                # Handle terminologies with subdirectories
                rel_parts = rel.split(os.sep)
                if len(rel_parts) > 1:
                    # Extract the subdirectory (e.g., 'molecularEntity' from 'terminologies/molecularEntity/filename.jsonld')
                    subdir = rel_parts[1]
                    page_path = f"instance_libraries/terminologies/{subdir}.html"
                else:
                    page_path = f"instance_libraries/terminologies/{inst_type}.html"

            anchor = _anchorize(filename)
            uri = f"/instances/{inst_type}/{filename}"
            url = f"{DOCS_BASE_URL}/en/{DOCS_VERSION_SLUG}/{page_path}#{anchor}"
            redirect_map[uri] = url

    return redirect_map


# ---------------------------------------------------------------------
# Verification helpers
# ---------------------------------------------------------------------


def _url_works(url: str, timeout: float = 10.0) -> bool:
    """Return True if the URL returns HTTP <400 (HEAD, falling back to GET)."""
    try:
        r = requests.head(url, timeout=timeout, allow_redirects=True)
        if r.status_code < 400:
            return True
        # Some servers don't handle HEAD properly – try GET but fetch nothing
        r = requests.get(url, timeout=timeout, allow_redirects=True, stream=True)
        return r.status_code < 400
    except Exception:
        return False


def verify_redirect_map(filename: str = OUTPUT_FILENAME, max_workers: int = 16) -> None:
    """
    Load an existing .htaccess file and check every target URL.
    """
    redirects = {}
    
    # Parse .htaccess format: Redirect 301 "/uri" "url"
    with open(filename, "r", encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if line.startswith('Redirect 301 "') and line.count('"') >= 4:
                # Extract URI and URL from: Redirect 301 "/uri" "url"
                parts = line.split('"')
                if len(parts) >= 4:
                    uri = parts[1]
                    url = parts[3]
                    redirects[uri] = url

    # 1. Identify broken URLs in parallel
    broken_keys = []

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        future_to_key = {pool.submit(_url_works, url): key for key, url in redirects.items()}
        for fut in as_completed(future_to_key):
            key = future_to_key[fut]
            try:
                ok = fut.result()
            except Exception:
                ok = False
            if not ok:
                print(f"Broken link found: {key} -> {redirects[key]}")
                broken_keys.append(key)

    if not broken_keys:
        print("All redirect targets are reachable – nothing to fix.")
        return

    print(f"{len(broken_keys)} broken links detected.")


def main() -> None:
    redirects = generate_redirect_map()
    
    # Write .htaccess file
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as fp:
        fp.write("# openMINDS redirect rules\n")
        fp.write("# Generated automatically by pipeline/redirect_map.py\n\n")
        
        # Sort by URI for consistent output
        sorted_redirects = sorted(redirects.items())
        
        for uri, url in sorted_redirects:
            # Apache redirect rule format: Redirect 301 /from /to
            fp.write(f'Redirect 301 "{uri}" "{url}"\n')
    
    print(f"Wrote {len(redirects)} redirect entries to {OUTPUT_FILENAME}")

    # Optional: immediately verify all links
    print("Verifying redirect targets...")
    verify_redirect_map(OUTPUT_FILENAME)


if __name__ == "__main__":
    main()
