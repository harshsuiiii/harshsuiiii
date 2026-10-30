"""Refreshes the stats cards and the "Latest pushes" list from the GitHub API.

Runs in the profile workflow. Standard library only, so there is nothing to install.
Set GITHUB_TOKEN for the contribution count; without it that tile is left out.
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError

from build_art import MONO, SANS, THEMES

USER = os.environ.get("PROFILE_USER", "harshsuiiii")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ROOT = Path(__file__).resolve().parents[2]
# Notebook bytes are mostly saved outputs, so they would swamp the real code.
SKIP_LANGUAGES = {"Jupyter Notebook"}
# The profile repo itself and leftovers that say nothing about the work.
SKIP_REPOS = {USER, "12123"}
TOP_LANGUAGES = 6
LATEST_PUSHES = 5
# One-line summaries for repos whose GitHub description is blank or too long.
TAGLINES = {
    "rate-limiter": "One shared limit across N servers, built on atomic Redis Lua scripts",
    "Booking-Agent": "Natural-language flight search for travel agents",
    "botforge-saas": "Multi-tenant SaaS to create, embed and monitor AI chatbots",
    "ReviveX": "AI payment-recovery agent with deterministic compliance rules",
    "aurora-DNS": "DNS server from scratch in TypeScript, with caching and failover",
    "Self-healing-RAG": "RAG pipeline where a critic audits every answer for grounding",
    "legalsummary.ai": "Plain-language summaries and clause analysis of legal documents",
    "OCR-Semantic-Grader": "Grades handwritten answers with TrOCR and Sentence-BERT",
}
LANGUAGE_COLORS = {
    "TypeScript": "#3178c6", "Python": "#3fb950", "JavaScript": "#e3b341", "Java": "#b07219",
    "HTML": "#e34c26", "CSS": "#8957e5", "C++": "#f34b7d", "C": "#7d8590",
}


def api(path, body=None):
    url = path if path.startswith("https://") else f"https://api.github.com/{path}"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": f"{USER}-profile"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    data = json.dumps(body).encode() if body else None
    with urllib.request.urlopen(urllib.request.Request(url, data, headers), timeout=30) as response:
        return json.load(response)


def contributions():
    if not TOKEN:
        return None
    query = "query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{totalContributions}}}}"
    result = api("https://api.github.com/graphql", {"query": query, "variables": {"u": USER}})
    return result["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]


def collect():
    repos = api(f"users/{USER}/repos?per_page=100&sort=pushed")
    own = [r for r in repos if not r["fork"] and r["name"] not in SKIP_REPOS]
    totals = {}
    for repo in own:
        for language, size in api(f"repos/{USER}/{repo['name']}/languages").items():
            if language not in SKIP_LANGUAGES:
                totals[language] = totals.get(language, 0) + size
    return own, totals, contributions()


def card(theme, own, totals, contribution_count):
    t = THEMES[theme]
    w, h = 1560, 300
    tiles = [(len(own), "original repos"), (len(totals), "languages")]
    if contribution_count is not None:
        tiles.insert(1, (contribution_count, "contributions, last 12 months"))
    grand = sum(totals.values()) or 1
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    top = [(name, size) for name, size in ranked[:TOP_LANGUAGES] if size / grand >= 0.01]
    rest = grand - sum(size for _, size in top)
    if rest:
        top.append(("Other", rest))

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" role="img" aria-labelledby="t">'
        f'<title id="t">GitHub stats for {USER}: '
        + ", ".join(f"{value} {name}" for value, name in tiles)
        + ". Top languages: "
        + ", ".join(name for name, _ in top)
        + f"</title><style>text{{font-family:{SANS}}}"
        f".n{{font-family:{MONO};font-size:58px;font-weight:700;fill:{t['text']}}}"
        f".c{{font-size:23px;fill:{t['muted']}}}.l{{font-size:22px;font-weight:600;fill:{t['text']}}}"
        f".p{{font-family:{MONO};font-size:20px;fill:{t['muted']}}}</style>",
        f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="{t["panel"]}" stroke="{t["edge"]}" stroke-width="2"/>',
    ]
    step = (w - 120) / len(tiles)
    for i, (value, name) in enumerate(tiles):
        x = 60 + i * step
        parts.append(f'<text x="{x:.0f}" y="100" class="n">{value:,}</text><text x="{x:.0f}" y="140" class="c">{name}</text>')

    bar_x, bar_w, x = 60, w - 120, 60.0
    parts.append(f'<clipPath id="b"><rect x="{bar_x}" y="178" width="{bar_w}" height="16" rx="8"/></clipPath><g clip-path="url(#b)">')
    for name, size in top:
        width = size / grand * bar_w
        colour = LANGUAGE_COLORS.get(name, t["muted"])
        parts.append(f'<rect x="{x:.1f}" y="178" width="{width:.1f}" height="16" fill="{colour}"/>')
        x += width
    parts.append("</g>")

    step = (w - 120) / len(top)
    for i, (name, size) in enumerate(top):
        x = 60 + i * step
        colour = LANGUAGE_COLORS.get(name, t["muted"])
        parts.append(
            f'<circle cx="{x + 8:.0f}" cy="238" r="8" fill="{colour}"/>'
            f'<text x="{x + 24:.0f}" y="245" class="l">{name}</text>'
            f'<text x="{x + 24:.0f}" y="273" class="p">{size / grand:.0%}</text>'
        )
    parts.append("</svg>")
    return "".join(parts)


def update_readme(own):
    readme = ROOT / "README.md"
    rows = []
    for repo in own[:LATEST_PUSHES]:
        summary = TAGLINES.get(repo["name"]) or (repo.get("description") or "").strip()
        if len(summary) > 100:
            summary = summary[:100].rsplit(" ", 1)[0] + "…"
        about = f" — {summary}" if summary else ""
        rows.append(f"- `{repo['pushed_at'][:10]}` **[{repo['name']}]({repo['html_url']})**{about}")
    block = "<!--START_SECTION:pushes-->\n" + "\n".join(rows) + "\n<!--END_SECTION:pushes-->"
    text = readme.read_text(encoding="utf-8")
    pattern = r"<!--START_SECTION:pushes-->.*?<!--END_SECTION:pushes-->"
    readme.write_text(re.sub(pattern, lambda _: block, text, flags=re.S), encoding="utf-8", newline="\n")


def main():
    try:
        own, totals, contribution_count = collect()
    except (HTTPError, URLError) as error:
        # Keep the last good cards rather than publishing an empty one.
        sys.exit(f"GitHub API failed, nothing changed: {error}")
    out = ROOT / "assets"
    out.mkdir(exist_ok=True)
    for theme in THEMES:
        (out / f"stats-{theme}.svg").write_text(card(theme, own, totals, contribution_count), encoding="utf-8")
    update_readme(own)


if __name__ == "__main__":
    main()
