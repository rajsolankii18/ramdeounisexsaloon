from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.images, self.styles, self.scripts = set(), [], [], [], []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.add(values["id"])
        if tag == "a" and values.get("href"):
            self.links.append(values["href"])
        if tag == "img" and values.get("src"):
            self.images.append(values["src"])
        if tag == "link" and values.get("href"):
            self.styles.append(values["href"])
        if tag == "script" and values.get("src"):
            self.scripts.append(values["src"])


source = (ROOT / "index.html").read_text(encoding="utf-8")
parser = Parser()
parser.feed(source)

for href in parser.links:
    if href.startswith("#"):
        assert href[1:] in parser.ids, f"Broken anchor: {href}"
    elif not urlparse(href).scheme:
        assert (ROOT / href).exists(), f"Missing linked file: {href}"

for asset in parser.images + parser.styles + parser.scripts:
    assert (ROOT / asset).exists(), f"Missing local asset: {asset}"

for value in ["9352963859", "khanmokaif7786@gmail.com", "UDYAM-BR-22-0030644", "96020"]:
    assert value in source, f"Required public detail missing: {value}"

for term in ["PAN", "bank account", "social category", "owner name", "employment details", "turnover"]:
    assert not re.search(rf"\b{re.escape(term)}\b", source, re.IGNORECASE), f"Private certificate field found: {term}"

print("VALIDATION PASSED")
print(f"Anchors checked: {sum(1 for href in parser.links if href.startswith('#'))}")
print(f"Local assets checked: {len(parser.images + parser.styles + parser.scripts)}")
