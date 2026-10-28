#!/usr/bin/env python3
"""
support-title-generalize.py  (idempotent)

Canonical support block: the heading "Fragen zu Ihrer Bestellung?" assumes every
email is about an order, which is wrong for account / password / newsletter /
contact / Kaufberater / payment-info templates. Replace with a context-neutral,
formal heading that fits all of them, keeping the "Wir antworten Ihnen
persoenlich." subtitle.

Re-runnable: only touches files still carrying the old heading.
"""
import pathlib

TEMPLATES = pathlib.Path(__file__).resolve().parent.parent / "templates"
OLD = '<div class="support-title">Fragen zu Ihrer Bestellung?</div>'
NEW = '<div class="support-title">Haben Sie Fragen?</div>'

changed = []
for f in sorted(TEMPLATES.glob("*.html")):
    text = f.read_text(encoding="utf-8")
    if OLD not in text:
        continue
    f.write_text(text.replace(OLD, NEW), encoding="utf-8")
    changed.append(f.name)

print(f"updated ({len(changed)}): {', '.join(changed) or '-'}")
