#!/usr/bin/env python3
"""
Normalize hero <td> bottom padding across all templates to the order-confirmation
reference value (20px) for every meta-card hero.

Background: the hero <td> inline `padding-bottom` had drifted across batches
(20px on the transactional cluster, 26px on the account/registration/review
cluster, 16px on track-trace/widerruf, 22px on password-reset). order-confirmation
is the house reference at 20px, so all meta-card heroes are aligned to it.

No-meta-card heroes (subtitle is the last hero element: gutschein, contact-form,
account-deletion, produktberater, amazon-pay-info) carry NO inline override and
stay at the .hero class default (36px) — they are intentionally left untouched.

Idempotent: only the single `<td class="hero" ...>` line matches these exact
strings (they contain class="hero"), so a global replace is safe.
"""
import pathlib

TDIR = pathlib.Path(__file__).resolve().parent.parent / "templates"
REF = '<td class="hero" bgcolor="#f7f9f7" style="padding-bottom:20px;">'
VARIANTS = ("16px", "22px", "26px")


def main() -> None:
    targets = {
        f'<td class="hero" bgcolor="#f7f9f7" style="padding-bottom:{v};">': REF
        for v in VARIANTS
    }
    changed = []
    for p in sorted(TDIR.glob("*.html")):
        if p.name == "theme-preview.html":
            continue
        s = p.read_text(encoding="utf-8")
        o = s
        for old, new in targets.items():
            s = s.replace(old, new)
        if s != o:
            p.write_text(s, encoding="utf-8")
            changed.append(p.name)
    print(f"Normalized {len(changed)} hero paddings to 20px:")
    print("\n".join(changed) if changed else "(none — already consistent)")


if __name__ == "__main__":
    main()
