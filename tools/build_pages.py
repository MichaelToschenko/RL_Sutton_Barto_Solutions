#!/usr/bin/env python3
"""Собирает каталог для GitHub Pages: PDF-файлы плюс страница со ссылками.

Ожидает, что PDF уже собраны в solutions/build/ (см. tools/build_pdf.sh).
Результат складывается в solutions/build/site/.
"""
import html
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_index import chapters  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "solutions" / "build"
SITE = BUILD / "site"

PAGE = """<!doctype html>
<html lang="ru">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Решения упражнений — Саттон, Барто</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{
    font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    max-width: 46rem; margin: 0 auto; padding: 3rem 1.25rem;
  }}
  h1 {{ font-size: 1.6rem; line-height: 1.3; margin-bottom: .25rem; }}
  p.lead {{ margin-top: 0; opacity: .75; }}
  a {{ color: inherit; }}
  .whole {{
    display: inline-block; margin: 1.5rem 0 2rem;
    padding: .7rem 1.2rem; border: 1px solid currentColor; border-radius: .5rem;
    text-decoration: none; font-weight: 600;
  }}
  table {{ border-collapse: collapse; width: 100%; }}
  td {{ padding: .45rem .5rem; border-bottom: 1px solid rgba(128,128,128,.25); }}
  td.num {{ text-align: right; opacity: .6; white-space: nowrap; }}
  footer {{ margin-top: 2.5rem; font-size: .9rem; opacity: .7; }}
</style>
<h1>Решения упражнений к книге Саттона и Барто «Обучение с подкреплением»</h1>
<p class="lead">140 разобранных упражнений, {n} глав.</p>
<a class="whole" href="main.pdf">📄 Весь сборник, PDF</a>
<table>
{rows}
</table>
<footer>
  Исходники и ноутбуки —
  <a href="https://github.com/MichaelToschenko/RL_Sutton_Barto_Solutions">на GitHub</a>.
</footer>
"""


def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    rows = []
    chs = chapters()
    for num, title, exercises in chs:
        pdf = BUILD / f"ch{num:02d}.pdf"
        if not pdf.exists():
            raise SystemExit(f"нет собранного {pdf.name} — сначала tools/build_pdf.sh")
        shutil.copy2(pdf, SITE / pdf.name)
        rows.append(
            f'<tr><td><a href="{pdf.name}">{html.escape(title)}</a></td>'
            f'<td class="num">{len(exercises)} упр.</td></tr>'
        )

    main_pdf = BUILD / "main.pdf"
    if not main_pdf.exists():
        raise SystemExit("нет собранного main.pdf — сначала tools/build_pdf.sh")
    shutil.copy2(main_pdf, SITE / "main.pdf")

    (SITE / "index.html").write_text(
        PAGE.format(n=len(chs), rows="\n".join(rows)), encoding="utf-8"
    )
    print(f"site/: {len(list(SITE.iterdir()))} файлов")


if __name__ == "__main__":
    main()
