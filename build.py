#!/usr/bin/env python3
"""Build the complete Friday story as a static bande dessinée."""

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).parent
SOURCE = ROOT / "story.txt"
OUTPUT = ROOT / "dist" / "index.html"

SCENE_ART = {
    ("Friday", "7:00 PM"): ("rain-walk.png", "wide"),
    ("Friday", "9:30 PM"): ("doner-shop.png", "wide"),
    ("Friday", "11:30 PM"): ("friday-night.png", "sheet"),
    ("Friday", "2:00 AM"): ("friday-night.png", "crop-right"),
    ("Saturday", "11:00 AM"): ("saturday-morning.png", "sheet"),
    ("Saturday", "12:30 PM"): ("saturday-morning.png", "crop-right"),
    ("Saturday", "2:00 PM"): ("saturday-day.png", "sheet"),
    ("Saturday", "2:15 PM"): ("saturday-day.png", "crop-center"),
    ("Saturday", "4:30 PM"): ("saturday-day.png", "crop-right"),
    ("Saturday", "9:00 PM"): ("lovers-become-trees.png", "trees"),
    ("Saturday", "11:30 PM"): ("saturday-night.png", "sheet"),
    ("Saturday", "1:00 AM"): ("saturday-night.png", "crop-right"),
    ("Sunday", "7:00 AM"): ("winter-room.png", "wide"),
    ("Sunday", "10:00 AM"): ("winter-room.png", "crop-left"),
    ("Sunday", "11:30 AM"): ("sunday-flashbacks.png", "sheet"),
    ("Sunday", "1:00 PM"): ("sunday-flashbacks.png", "crop-right"),
    ("Sunday", "3:30 PM"): ("sunday-later.png", "sheet"),
    ("Later", "Later"): ("sunday-later.png", "crop-right"),
}


def prose(block: str) -> str:
    lines = [line.strip() for line in block.splitlines()]
    verse = len(lines) > 1
    body = "<br>".join(escape(line) for line in lines)
    return f'<p class="{"verse" if verse else ""}">{body}</p>'


raw = SOURCE.read_text(encoding="utf-8").strip()
blocks = re.split(r"\n\s*\n", raw)
chapters = []
chapter = None
scene = None

for block in blocks:
    block = block.strip()
    chapter_match = re.fullmatch(r"## (Saturday|Sunday|Later)", block)
    if block == "Friday" or chapter_match:
        chapter = {"name": block.removeprefix("## "), "scenes": []}
        chapters.append(chapter)
        scene = None
        continue
    time_match = re.fullmatch(r"\*\*(\d{1,2}:\d{2} (?:AM|PM))\*\*", block)
    if time_match:
        scene = {"time": time_match.group(1), "paragraphs": []}
        chapter["scenes"].append(scene)
        continue
    if chapter["name"] == "Later" and scene is None:
        scene = {"time": "Later", "paragraphs": []}
        chapter["scenes"].append(scene)
    scene["paragraphs"].append(prose(block))


def scene_html(chapter_name: str, item: dict, index: int) -> str:
    filename, art_class = SCENE_ART[(chapter_name, item["time"])]
    copy = "\n".join(item["paragraphs"])
    tree_quote = ""
    scene_class = f"scene scene-{index}"
    if art_class == "trees":
        scene_class += " tree-scene"
        tree_quote = '<blockquote>I think all true lovers eventually become trees.</blockquote>'
    image_loading = 'fetchpriority="high"' if chapter_name == "Friday" and index == 0 else 'loading="lazy" decoding="async"'
    return f'''<article class="{scene_class}">
      <div class="scene-head"><time>{escape(item["time"])}</time><span aria-hidden="true"></span></div>
      <figure class="comic-art {art_class}"><img src="assets/{filename}" alt="" {image_loading}></figure>
      <div class="story-copy">{copy}</div>
      {tree_quote}
    </article>'''


sections = []
for ci, chapter_item in enumerate(chapters):
    name = chapter_item["name"]
    scenes = "".join(scene_html(name, s, i) for i, s in enumerate(chapter_item["scenes"]))
    sections.append(f'''<section class="chapter chapter-{ci + 1}" id="{name.lower()}">
      <header class="chapter-title"><h2>{escape(name)}</h2></header>
      {scenes}
    </section>''')

page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#eeeae2">
  <meta name="description" content="Friday, a black and white bande dessinée.">
  <title>Friday — Bande Dessinée</title>
  <link rel="preload" as="image" href="assets/rain-walk.png">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="progress" aria-hidden="true"><span id="progress-fill"></span></div>
  <header class="masthead">
    <a href="#friday">Friday</a>
    <nav aria-label="Friday"><a href="#friday">Friday</a><a href="#saturday">Saturday</a><a href="#sunday">Sunday</a><a href="#later">Later</a></nav>
  </header>
  <main>{''.join(sections)}</main>
  <footer><a href="#friday">Friday</a></footer>
  <script src="script.js" defer></script>
</body>
</html>'''

OUTPUT.write_text(page, encoding="utf-8")
print(f"Built {OUTPUT} with {sum(len(c['scenes']) for c in chapters)} scenes")
