import { InputPathToUrlTransformPlugin, HtmlBasePlugin } from "@11ty/eleventy";
import markdownIt from "markdown-it";
import markdownItAnchor from "markdown-it-anchor";

/**
 * Produce the same anchor slug GitHub does, so the anchor links already written
 * in the markdown (e.g. 1-scope.md#assess-the-level-of-autonomy) keep working.
 * Mirrors heading_to_anchor() in scripts/build-combined.py.
 */
function githubSlug(heading) {
  return heading
    .toLowerCase()
    .replace(/[^a-z0-9 -]/g, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
}

export default function (eleventyConfig) {
  // Rewrites relative .md links (../reference/risk-catalogue.md) to output URLs,
  // so the markdown stays readable on GitHub and correct on the site.
  eleventyConfig.addPlugin(InputPathToUrlTransformPlugin);

  // Applies pathPrefix to every URL in the output, so the site works both at the
  // domain root and under /ai-risk-assessment-framework/ on GitHub Pages.
  eleventyConfig.addPlugin(HtmlBasePlugin);

  // Every page gets the layout without any front matter in the markdown.
  eleventyConfig.addGlobalData("layout", "base.njk");

  eleventyConfig.addPassthroughCopy("assets");

  // The readme links to these; copy them verbatim so the links resolve on the
  // site as well as on GitHub.
  eleventyConfig.addPassthroughCopy("LICENSE");
  eleventyConfig.addPassthroughCopy("LICENSE-CODE");

  const md = markdownIt({ html: true }).use(markdownItAnchor, {
    level: [2, 3, 4],
    slugify: githubSlug,
    permalink: markdownItAnchor.permalink.headerLink({ safariReaderFix: true }),
  });

  // Wide tables (the heatmap, the likelihood/impact matrix) scroll rather than
  // forcing the page to.
  md.renderer.rules.table_open = () => '<div class="table-wrap">\n<table>\n';
  md.renderer.rules.table_close = () => "</table>\n</div>\n";

  eleventyConfig.setLibrary("md", md);

  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    // Set PATH_PREFIX=/ai-risk-assessment-framework/ in CI. Change in one place
    // (here and the workflow) when moving to a custom domain.
    pathPrefix: process.env.PATH_PREFIX || "/",
    // Markdown is content, not a template: don't run it through Liquid/Nunjucks.
    markdownTemplateEngine: false,
    htmlTemplateEngine: "njk",
  };
}
