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
    "step-1-define.md",
    "step-2-understand-data.md",
    "step-3-assess-risks.md",
    "step-4-check-tool.md",
    "step-5-mitigate.md",
    "step-6-record.md",
    "step-7-checklists.md",
    "step-8-share.md",
    "appendix-a-tool-evaluation.md",
    "appendix-b-risk-template.md",
    "appendix-c-playbook-mapping.md",
    "appendix-d-glossary.md",
    "appendix-e-worked-examples.md",
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
    file_to_anchor = {s["filename"]: s["anchor"] for s in sections}

    def replace_link(match):
        text = match.group(1)
        file = match.group(2)
        anchor = file_to_anchor.get(file)
        if anchor:
            return f"[{text}](#{anchor})"
        return match.group(0)

    # 3. Process each section
    processed = []
    for i, section in enumerate(sections):
        md = section["content"]

        # Strip leading --- (e.g. step-7-checklists.md)
        md = re.sub(r"^---\n+", "", md)

        # Strip navigation footer: --- followed by [Next: ...](file.md)
        md = re.sub(r"\n---\n+\[Next:.*?>\]\(.*?\.md\)\s*$", "\n", md)

        # Strip the "Contents" section from readme.md
        if section["filename"] == "readme.md":
            md = re.sub(r"\n## Contents[\s\S]*$", "\n", md)

        # Convert inter-file .md links to internal anchor links
        md = re.sub(r"\[([^\]]+)\]\(([a-z][\w-]*\.md)\)", replace_link, md)

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
