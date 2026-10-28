#!/usr/bin/env python3
"""
support-title-generalize.py  (idempotent)

Canonical support block heading. The original "Fragen zu Ihrer Bestellung?"
assumed every email is about an order, which is wrong for account / password /
newsletter / contact / Kaufberater / payment-info templates. Final heading is the
natural, native-German, context-neutral "Haben Sie noch Fragen?" (the "noch" flows
after the email's content). Subtitle "Wir antworten Ihnen persoenlich." unchanged.

Re-runnable: maps any known prior heading to the final one.
"""
import pathlib

TEMPLATES = pathlib.Path(__file__).resolve().parent.parent / "templates"
NEW = '<div class="support-title">Haben Sie noch Fragen?</div>'
OLD_VARIANTS = [
    '<div class="support-title">Fragen zu Ihrer Bestellung?</div>',
    '<div class="support-title">Haben Sie Fragen?</div>',
]

changed = []
for f in sorted(TEMPLATES.glob("*.html")):
    text = f.read_text(encoding="utf-8")
    new = text
    for old in OLD_VARIANTS:
        new = new.replace(old, NEW)
    if new != text:
        f.write_text(new, encoding="utf-8")
        changed.append(f.name)

print(f"updated ({len(changed)}): {', '.join(changed) or '-'}")
