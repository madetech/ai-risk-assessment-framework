#!/usr/bin/env python3

"""
Combines the split markdown files into a single document.
Run: python3 scripts/build-combined.py
"""

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / f"ai-risk-assessment-framework-{date.today().strftime('%Y-%m-%d')}.md"

FILE_ORDER = [
    "readme.md",
    "getting-started.md",
    "assess/1-scope.md",
    "assess/2-check-tool.md",
    "assess/3-assess-risks.md",
    "assess/4-record-and-work.md",
    "templates/risk-assessment.md",
    "templates/tool-evaluation.md",
    "templates/introduction.md",
    "reference/use-type-profiles.md",
    "reference/risk-catalogue.md",
    "reference/checklists.md",
    "reference/worked-examples.md",
    "reference/government-guidance.md",
    "reference/glossary.md",
]

PAGE_BREAK = "\n<div style=\"page-break-before: always;\"></div>\n"


def heading_to_anchor(heading: str) -> str:
    """Convert a markdown heading to a GFM-style anchor slug."""
    slug = heading.lower()
    slug = re.sub(r"[^a-z0-9 -]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def main():
    # 1. Read all files and extract H1 headings
    sections = []
    for filename in FILE_ORDER:
        content = (ROOT / filename).read_text(encoding="utf-8")
        h1_match = re.search(r"^# (.+)$", content, re.MULTILINE)
        heading = h1_match.group(1) if h1_match else filename
        sections.append({
            "filename": filename,
            "content": content,
            "heading": heading,
            "anchor": heading_to_anchor(heading),
        })

    # 2. Build filename → anchor mapping for inter-file link conversion
    # Map both the full path and the basename so links work from any directory
    file_to_anchor = {}
    for s in sections:
        file_to_anchor[s["filename"]] = s["anchor"]
        # Also map relative paths that start with ../ (e.g. ../reference/glossary.md)
        file_to_anchor["../" + s["filename"]] = s["anchor"]
        # Also map the bare basename so sibling links within a subdirectory
        # (e.g. [Step 3](3-assess-risks.md) inside assess/) resolve too.
        # Basenames are unique across the framework, so this cannot collide.
        file_to_anchor[Path(s["filename"]).name] = s["anchor"]

    def replace_link(match):
        text = match.group(1)
        prefix = match.group(2) or ""
        file = match.group(3)
        fragment = match.group(4) or ""
        # Try the full path as written, then with prefix
        anchor = file_to_anchor.get(file) or file_to_anchor.get(prefix + file)
        if not anchor:
            return match.group(0)
        # A link to a specific heading (e.g. 3-assess-risks.md#adjust-for-autonomy)
        # can keep its fragment: that heading survives in the combined document.
        # Only the file path needs dropping.
        if fragment:
            return f"[{text}]({fragment})"
        return f"[{text}](#{anchor})"

    # 3. Process each section
    processed = []
    for i, section in enumerate(sections):
        md = section["content"]

        # Strip leading --- (e.g. step-7-checklists.md)
        md = re.sub(r"^---\n+", "", md)

        # Strip navigation footer: --- followed by [Next/Back ...](file.md)
        md = re.sub(r"\n---\n+\[(?:Next|Back).*?\]\(.*?\.md\)\s*$", "\n", md)

        # Strip the "Contents" section from readme.md
        if section["filename"] == "readme.md":
            md = re.sub(r"\n## Contents[\s\S]*$", "\n", md)

        # Convert inter-file .md links to internal anchor links
        md = re.sub(
            r"\[([^\]]+)\]\((\.\.?/)?([a-z][\w/-]*\.md)(#[\w-]+)?\)",
            replace_link,
            md,
        )

        # Add page break before each section (except the first)
        if i > 0:
            md = PAGE_BREAK + "\n" + md

        processed.append(md)

    # 4. Join and write
    combined = "\n".join(processed)
    OUTPUT.write_text(combined, encoding="utf-8")
    print(f"Combined {len(sections)} files into {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
