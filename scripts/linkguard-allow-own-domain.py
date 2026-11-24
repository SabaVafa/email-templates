#!/usr/bin/env python3
"""
Public-repo link-guard refinement: let pf-lockdown-js allow portfolio
cross-links to the own domain (sabavafa.github.io), matching what pf-ext-js
already does and the CLAUDE.md policy ("portfolio cross-links to
sabavafa.github.io are fine").

Before: pf-lockdown-js blocked the click on ANY absolute http/tel/mailto link,
so an own-domain CTA (e.g. the Fotowettbewerb "Zur Gewinnergalerie" button ->
https://sabavafa.github.io/kundenwettbewerb/#galerie) was not clickable in the
portfolio preview. tel:/mailto:/other-domain links and footer links stay blocked.

PUBLIC REPO ONLY (the private repo has no guard scripts). Idempotent.
"""
import pathlib

TDIR = pathlib.Path(__file__).resolve().parent.parent / "templates"
OLD = "if(/^(https?:|tel:|mailto:)/i.test(h))return true;"
NEW = ("if(/^(https?:|tel:|mailto:)/i.test(h)"
       "&&!/^https?:\\/\\/sabavafa\\.github\\.io/i.test(h))return true;")


def main() -> None:
    changed = []
    for p in sorted(TDIR.glob("*.html")):
        s = p.read_text(encoding="utf-8")
        if OLD in s:
            p.write_text(s.replace(OLD, NEW), encoding="utf-8")
            changed.append(p.name)
    print(f"Updated {len(changed)} templates:")
    print("\n".join(changed) if changed else "(none — already applied)")


if __name__ == "__main__":
    main()
