"""Draws the hero banner and journey map in dark and light themes.

Run after editing a station:  python .github/scripts/build_art.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "assets"

THEMES = {
    "dark": {
        "bg": "#0d1117", "panel": "#161b22", "edge": "#30363d", "text": "#f0f6fc",
        "muted": "#9198a1", "faint": "#21262d", "systems": "#22d3ee",
        "product": "#fbbf24", "ml": "#c084fc",
    },
    "light": {
        "bg": "#ffffff", "panel": "#f6f8fa", "edge": "#d1d9e0", "text": "#1f2328",
        "muted": "#59636e", "faint": "#e6eaef", "systems": "#0891b2",
        "product": "#d97706", "ml": "#9333ea",
    },
}

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,monospace"

# (label, x, y, label above the line?)
STATIONS = {
    "systems": [
        ("Sorting Algos", 90, 190, True),
        ("Twitter API", 250, 190, False),
        ("Matching Engine", 420, 190, True),
        ("Aurora DNS", 590, 190, False),
    ],
    "product": [
        ("Portfolio", 90, 350, True),
        ("Real-time Chat", 420, 350, True),
        ("legalsummary.ai", 1090, 350, True),
        ("BotForge", 1190, 350, False),
        ("ReviveX", 1290, 350, True),
    ],
    "ml": [
        ("Sparse NNs", 740, 490, True),
        ("Diffusion", 830, 490, False),
        ("Fuzzy Pooling", 920, 490, True),
        ("Churn", 1010, 490, False),
        ("Self-Healing RAG", 1120, 490, True),
        ("OCR Grader", 1260, 490, False),
    ],
}

PATHS = {
    "systems": "M 60 190 H 1400",
    "product": "M 60 350 H 1330 L 1400 420",
    "ml": "M 560 350 L 700 490 H 1330 L 1400 420",
}

COLUMNS = [
    ("2024", 40, 330),
    ("2025", 330, 690),
    ("EARLY 2026", 690, 1060),
    ("MID 2026", 1060, 1320),
    ("OCT 2026", 1320, 1520),
]

LEGEND = [
    ("systems", "Systems", "how software works underneath"),
    ("product", "Product", "things people can click on"),
    ("ml", "ML research", "models, then models in production"),
]


def station(label, x, y, above, line):
    label_y = y - 30 if above else y + 44
    return (
        f'<g class="stop"><circle cx="{x}" cy="{y}" r="11" class="dot {line}-stroke"/>'
        f'<text x="{x}" y="{label_y}" text-anchor="middle" class="label">{label}</text></g>'
    )


def terminus(label, sub, x, y, line_classes, text_x=None):
    anchor = "middle" if text_x is None else "start"
    text_x = x if text_x is None else text_x
    rings = "".join(
        f'<circle cx="{x}" cy="{y}" r="{r}" class="dot {c}-stroke"/>'
        for r, c in zip((20, 12), line_classes)
    )
    return (
        f'<g class="stop"><circle cx="{x}" cy="{y}" r="28" class="pulse {line_classes[0]}-fill"/>{rings}'
        f'<text x="{text_x}" y="{y - 40}" text-anchor="{anchor}" class="label strong">{label}</text>'
        f'<text x="{text_x}" y="{y + 54}" text-anchor="{anchor}" class="sub">{sub}</text></g>'
    )


def journey(t):
    w, h = 1560, 660
    css = f"""
    text{{font-family:{SANS}}}
    .label{{font-size:22px;font-weight:600;fill:{t['text']}}}
    .strong{{font-size:25px;font-weight:700}}
    .sub{{font-size:19px;fill:{t['muted']}}}
    .year{{font-family:{MONO};font-size:19px;font-weight:600;letter-spacing:2px;fill:{t['muted']}}}
    .legend{{font-size:21px;font-weight:700;fill:{t['text']}}}
    .line{{fill:none;stroke-width:9;stroke-linecap:round;stroke-linejoin:round}}
    .tail{{fill:none;stroke-width:5;stroke-dasharray:3 13;stroke-linecap:round;stroke:{t['muted']}}}
    .dot{{fill:{t['bg']};stroke-width:6}}
    .pulse{{opacity:.18;transform-box:fill-box;transform-origin:center;animation:pulse 2.8s ease-in-out infinite}}
    .train{{stroke:{t['bg']};stroke-width:2}}
    .systems-line{{stroke:{t['systems']}}}.product-line{{stroke:{t['product']}}}.ml-line{{stroke:{t['ml']}}}
    .systems-stroke{{stroke:{t['systems']}}}.product-stroke{{stroke:{t['product']}}}.ml-stroke{{stroke:{t['ml']}}}
    .systems-fill{{fill:{t['systems']}}}.product-fill{{fill:{t['product']}}}.ml-fill{{fill:{t['ml']}}}
    @keyframes pulse{{50%{{transform:scale(1.25);opacity:.05}}}}
    @media (prefers-reduced-motion:reduce){{.pulse{{animation:none}}.train{{display:none}}}}
    """
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" role="img" '
        f'aria-labelledby="t d"><title id="t">Harsh Vardhan Singh\'s project journey, drawn as a metro map</title>'
        f'<desc id="d">Three lines run from 2024 to October 2026. Systems: sorting algorithms, a Twitter API, '
        f'a matching engine, Aurora DNS, ending at the Distributed Rate Limiter. Product: portfolio, real-time chat, '
        f'legalsummary.ai, BotForge, ReviveX. ML research branches off product in 2026: sparse neural networks, '
        f'diffusion models, fuzzy pooling, churn, Self-Healing RAG, OCR Grader. Product and ML meet at Booking Agent.</desc>'
        f'<style>{css}</style>',
        f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="{t["panel"]}" stroke="{t["edge"]}" stroke-width="2"/>',
    ]
    for i, (name, x0, x1) in enumerate(COLUMNS):
        parts.append(f'<text x="{(x0 + x1) / 2}" y="62" text-anchor="middle" class="year">{name}</text>')
        if i:
            parts.append(f'<line x1="{x0}" y1="84" x2="{x0}" y2="560" stroke="{t["faint"]}" stroke-width="2" stroke-dasharray="4 8"/>')
    parts.append(f'<path d="M 1422 190 H 1500" class="tail"/><path d="M 1422 420 H 1500" class="tail"/>')
    for line, d in PATHS.items():
        parts.append(f'<path d="{d}" class="line {line}-line"/>')
    for line, stops in STATIONS.items():
        for label, x, y, above in stops:
            parts.append(station(label, x, y, above, line))
    parts.append(terminus("Rate Limiter", "shipped Oct 2026", 1400, 190, ("systems", "systems")))
    parts.append(terminus("Booking Agent", "live demo", 1400, 420, ("product", "ml"), text_x=1372))
    for i, (line, d) in enumerate(PATHS.items()):
        parts.append(
            f'<circle r="6" class="train {line}-fill"><animateMotion dur="{11 + i * 2}s" begin="{i * 1.2}s" '
            f'repeatCount="indefinite" path="{d}"/></circle>'
        )
    for i, (line, name, about) in enumerate(LEGEND):
        x = 60 + i * 490
        parts.append(
            f'<line x1="{x}" y1="610" x2="{x + 44}" y2="610" class="{line}-stroke" stroke-width="9" stroke-linecap="round"/>'
            f'<text x="{x + 60}" y="603" class="legend">{name}</text>'
            f'<text x="{x + 60}" y="630" class="sub">{about}</text>'
        )
    parts.append("</svg>")
    return "".join(parts)


def hero(t):
    w, h = 1560, 400
    css = f"""
    text{{font-family:{SANS}}}
    .name{{font-size:78px;font-weight:800;letter-spacing:-1.5px;fill:{t['text']}}}
    .role{{font-size:31px;font-weight:600;fill:{t['muted']}}}
    .motto{{font-family:{MONO};font-size:27px;fill:{t['text']}}}
    .line{{fill:none;stroke-width:9;stroke-linecap:round;stroke-linejoin:round}}
    .node{{fill:{t['panel']};stroke-width:6}}
    @media (prefers-reduced-motion:reduce){{.train{{display:none}}}}
    """
    lines = [
        ("systems", "M 1040 80 L 1240 80 L 1380 220 H 1500"),
        ("product", "M 1040 220 H 1500"),
        ("ml", "M 1040 360 L 1240 360 L 1380 220 H 1500"),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" role="img" aria-labelledby="t">'
        f'<title id="t">Harsh Vardhan Singh. AI engineer, backend and distributed systems, ML research.</title><style>{css}</style>',
        f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="18" fill="{t["panel"]}" stroke="{t["edge"]}" stroke-width="2"/>',
                '<text x="70" y="160" class="name">Harsh Vardhan Singh</text>',
        '<text x="72" y="222" class="role">AI Engineer · Backend &amp; Distributed Systems · ML Research</text>',
        '<text x="72" y="306" class="motto">Deterministic rules around the LLM.</text>',
        '<text x="72" y="346" class="motto">Tests around everything.</text>',
    ]
    for name, d in lines:
        parts.append(f'<path d="{d}" class="line" stroke="{t[name]}"/>')
    for name, x, y in (("systems", 1130, 80), ("product", 1130, 220), ("ml", 1130, 360)):
        parts.append(f'<circle cx="{x}" cy="{y}" r="12" class="node" stroke="{t[name]}"/>')
    parts.append(f'<circle cx="1500" cy="220" r="17" class="node" stroke="{t["text"]}"/>')
    for i, (name, d) in enumerate(lines):
        parts.append(
            f'<circle r="7" class="train" fill="{t[name]}"><animateMotion dur="{7 + i}s" begin="{i * .8}s" '
            f'repeatCount="indefinite" path="{d}"/></circle>'
        )
    parts.append("</svg>")
    return "".join(parts)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for theme, palette in THEMES.items():
        (OUT / f"journey-{theme}.svg").write_text(journey(palette), encoding="utf-8")
        (OUT / f"hero-{theme}.svg").write_text(hero(palette), encoding="utf-8")
