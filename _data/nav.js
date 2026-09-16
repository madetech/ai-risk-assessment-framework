import fs from "node:fs";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");

/**
 * The site's navigation, and the definitive list of which markdown files
 * become pages. Order follows the Contents section of readme.md.
 *
 * `label` is the short name shown in the sidebar, where the group heading
 * already supplies the context each H1 spells out. Omit it to use the H1.
 *
 * (scripts/build-combined.py keeps its own FILE_ORDER: the single document
 * deliberately puts the templates before the reference library.)
 */
const GROUPS = [
  {
    title: null,
    items: [
      { file: "readme.md", label: "Overview" },
      { file: "getting-started.md", label: "Getting started" },
    ],
  },
  {
    title: "The assessment",
    items: [
      { file: "assess/1-scope.md" },
      { file: "assess/2-check-tool.md" },
      { file: "assess/3-assess-risks.md" },
      { file: "assess/4-record-and-work.md" },
    ],
  },
  {
    title: "Reference library",
    items: [
      { file: "reference/use-type-profiles.md", label: "Use-type profiles" },
      { file: "reference/risk-catalogue.md", label: "Risk catalogue" },
      { file: "reference/checklists.md", label: "Per-use checklists" },
      { file: "reference/worked-examples.md", label: "Worked examples" },
      { file: "reference/government-guidance.md", label: "UK government guidance" },
      { file: "reference/glossary.md", label: "Glossary" },
    ],
  },
  {
    title: "Templates",
    items: [
      { file: "templates/risk-assessment.md", label: "Risk assessment" },
      { file: "templates/tool-evaluation.md", label: "Tool profile" },
      { file: "templates/introduction.md", label: "Introduction" },
    ],
  },
];

/** The page title is the file's first H1, so the markdown needs no front matter. */
function titleOf(file) {
  const content = fs.readFileSync(path.join(ROOT, file), "utf8");
  const match = content.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : file;
}

export default function () {
  return GROUPS.map((group) => ({
    title: group.title,
    items: group.items.map(({ file, label }) => {
      const title = titleOf(file);
      return {
        file,
        title,
        label: label ?? title,
        stem: "/" + file.replace(/\.md$/, ""),
        url: file === "readme.md" ? "/" : "/" + file.replace(/\.md$/, "") + "/",
      };
    }),
  }));
}
