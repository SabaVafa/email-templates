#!/usr/bin/env python3
"""
Set-wide copy fixes from the Fotowettbewerb review (2026-11), applied to ALL
templates for consistency:

- Item 9: sign-off "— Ihr Team von Metzler" -> "Ihr Metzler-Team"
  (drops the English em-dash convention; German idiom).
- Item 11: opening hours "Mo–Fr.:" -> "Mo.–Fr.:" (consistent abbreviation dots).
  Handles both the HTML-entity form (Mo&ndash;Fr.:) and the literal en-dash form.

Idempotent: the replacement targets no longer match once applied.
Run from either repo; it rewrites templates/*.html in place.
"""
import pathlib

TDIR = pathlib.Path(__file__).resolve().parent.parent / "templates"
REPLACEMENTS = [
    ("&mdash; Ihr Team von Metzler", "Ihr Metzler-Team"),   # item 9 (sign-off)
    ("Mo&ndash;Fr.:", "Mo.&ndash;Fr.:"),                    # item 11 (entity dash)
    ("Mo–Fr.:", "Mo.–Fr.:"),                      # item 11 (literal en-dash)
]


def main() -> None:
    changed = []
    for p in sorted(TDIR.glob("*.html")):
        if p.name == "theme-preview.html":
            continue
        s = p.read_text(encoding="utf-8")
        o = s
        hits = []
        for old, new in REPLACEMENTS:
            if old in s:
                s = s.replace(old, new)
                hits.append(old.split()[0] if " " in old else old)
        if s != o:
            p.write_text(s, encoding="utf-8")
            changed.append(f"{p.name}: {', '.join(hits)}")
    print(f"Updated {len(changed)} templates:")
    print("\n".join(changed) if changed else "(none — already applied)")


if __name__ == "__main__":
    main()
