/** The nav flattened into reading order, for titles and prev/next links. */
function flatten(nav) {
  return (nav || []).flatMap((group) => group.items);
}

export default {
  /** Title from the nav (which reads each file's first H1) rather than front matter. */
  title: (data) => {
    const stem = data.page?.filePathStem;
    return flatten(data.nav).find((item) => item.stem === stem)?.title ?? data.site.title;
  },

  /** Previous and next page in reading order, so the four steps can be walked through. */
  pager: (data) => {
    const items = flatten(data.nav);
    const index = items.findIndex((item) => item.stem === data.page?.filePathStem);
    if (index === -1) return {};
    return { prev: items[index - 1], next: items[index + 1] };
  },

  /** readme.md is the homepage; everything else keeps its path. */
  permalink: (data) => {
    const stem = data.page?.filePathStem;
    if (!stem || !data.page?.inputPath?.endsWith(".md")) return undefined;
    return stem === "/readme" ? "/index.html" : `${stem}/index.html`;
  },
};
