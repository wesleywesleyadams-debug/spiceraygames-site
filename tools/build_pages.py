"""Builds the static pages of spiceraygames.com from shared header/footer pieces.

Run: python tools/build_pages.py   (from the repo root)
The Codex page (games/aegis-matrix/codex/index.html) is hand-written and not built here.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# OWNER: swap this one line once the LLC owns the IP (Legal will confirm).
OWNER = "Wesley Adams"


def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
"""


def header(active=""):
    def link(href, label, key):
        on = ' class="on"' if key == active else ""
        return f'<a href="{href}"{on}>{label}</a>'
    return f"""<header class="top">
  <a class="studio" href="/">Spiceray Games</a>
  <nav>{link('/games/', 'Games', 'games')}{link('/studio/', 'Studio', 'studio')}</nav>
</header>
"""


def game_tabs(active):
    def tab(href, label, key):
        on = " on" if key == active else ""
        return f'<a class="tab{on}" href="{href}">{label}</a>'
    return f"""<div class="tabs"><div class="wrap">
  <a class="game{' on' if active == 'home' else ''}" href="/games/aegis-matrix/">Aegis Matrix</a>
  {tab('/games/aegis-matrix/codex/', 'Codex', 'codex')}
</div></div>
"""


FOOTER = f"""<footer>
  <p>Contact: <a href="mailto:hello@spiceraygames.com">hello@spiceraygames.com</a></p>
  <p>&copy; 2026 {OWNER}. All rights reserved.</p>
  <p>Font: JetBrains Mono (<a href="/assets/JetBrainsMono-OFL.txt">SIL OFL 1.1</a>).</p>
</footer>
</body>
</html>
"""

AEGIS_CARD = """<a class="gamecard" href="/games/aegis-matrix/">
  <div class="shot"><img src="/assets/logo_aegis_matrix.png" alt="Aegis Matrix"></div>
  <div>
    <h3>Aegis Matrix&#8482;</h3>
    <p>A pixel-art space RTS. Lead one of three distinct factions, research a deep tech grid, and command fleets in real-time battles for star systems.</p>
    <span class="more">View game &rarr;</span>
  </div>
</a>
"""

PAGES = {
    "index.html": head("Spiceray Games", "Spiceray Games is an independent studio making pixel-art strategy games.") + header() + """
<div class="hero short lined">
  <div class="hero-inner">
    <h1>Spiceray Games</h1>
    <p class="tag">An independent studio making pixel-art strategy games.</p>
  </div>
</div>

<main class="wrap">
  <section>
    <h2>Our games</h2>
""" + AEGIS_CARD + """  </section>
</main>
""" + FOOTER,

    "games/index.html": head("Games – Spiceray Games", "Games by Spiceray Games.") + header("games") + """
<main class="wrap">
  <section>
    <h2>Games</h2>
""" + AEGIS_CARD + """  </section>
</main>
""" + FOOTER,

    "games/aegis-matrix/index.html": head("Aegis Matrix – Spiceray Games", "Aegis Matrix is a pixel-art space RTS by Spiceray Games.") + header("games") + game_tabs("home") + """
<div class="hero">
  <div class="hero-inner">
    <img class="logo" src="/assets/logo_aegis_matrix.png" alt="Aegis Matrix">
    <p class="tag">A pixel-art space RTS. Build, research, and command your fleet across the stars.</p>
    <!-- Swap for the Steam link once the store page is live -->
    <a class="btn" aria-disabled="true">Steam page coming soon</a>
  </div>
</div>

<main class="wrap">
  <section>
    <h2>Aegis Matrix&#8482;</h2>
    <p>Lead one of several distinct factions in real-time battles for star systems. Each faction plays differently, with its own technologies and strengths. Expand across planets, mine resources, research technology, and fight fleets that adapt to how you play.</p>
    <div class="grid">
      <div class="card"><h3>Distinct factions</h3><p>The Trade Federation, the Hive Mind and the Eldar Covenant, each with its own tech tree and bonuses.</p></div>
      <div class="card"><h3>Deep tech</h3><p>A tech grid of Basic, Advanced and Experimental upgrades that change how your ships fight.</p></div>
      <div class="card"><h3>Real fleet battles</h3><p>Lasers, rail cannons, drones, missiles and tractor beams, with every shot simulated.</p></div>
      <div class="card"><h3>Challenging AI</h3><p>Face two kinds of opponent: AI and NAI, alone or in teams.</p></div>
    </div>
    <div class="fleet">
      <img src="/assets/ship_corvette.png" alt="Corvette">
      <img src="/assets/ship_cruiser.png" alt="Cruiser">
      <img src="/assets/ship_carrier.png" alt="Carrier">
    </div>
    <p style="text-align:center;margin-top:32px"><a class="btn" href="/games/aegis-matrix/codex/">Read the Codex</a></p>
  </section>
</main>
""" + FOOTER,

    "studio/index.html": head("Studio – Spiceray Games", "About Spiceray Games.") + header("studio") + """
<main class="wrap">
  <section>
    <h2>The studio</h2>
    <p>Spiceray Games is an independent studio. Aegis Matrix is its first game, built in the Godot engine.</p>
    <p>Gameplay videos and streams are welcome, including monetised ones.</p>
    <h2>Contact</h2>
    <p>General: <a href="mailto:hello@spiceraygames.com">hello@spiceraygames.com</a></p>
    <p>Press and media: <a href="mailto:press@spiceraygames.com">press@spiceraygames.com</a></p>
  </section>
</main>
""" + FOOTER,

    # Old link, kept so shared URLs still work.
    "codex/index.html": """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Aegis Matrix Codex</title>
<link rel="canonical" href="/games/aegis-matrix/codex/">
<script>location.replace('/games/aegis-matrix/codex/' + location.hash)</script>
<meta http-equiv="refresh" content="0; url=/games/aegis-matrix/codex/">
</head><body><p>The Codex has moved: <a href="/games/aegis-matrix/codex/">Aegis Matrix Codex</a>.</p></body></html>
""",
}

if __name__ == "__main__":
    for rel, html in PAGES.items():
        p = ROOT / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(html, encoding="utf-8", newline="\n")
        print("wrote", rel)
