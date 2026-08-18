#!/usr/bin/env python3
"""Пересобирает оглавление в README.md по исходникам сборника.

Читает solutions/chapters/*.tex и таблицу ноутбуков из fix_notebooks.py,
после чего переписывает два блока README между маркерами. Запускается вручную
и в CI, чтобы оглавление не расходилось с содержимым.

    python3 tools/build_index.py            # переписать README.md
    python3 tools/build_index.py --check    # упасть, если README устарел
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fix_notebooks import NOTEBOOKS, PAGES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

MARKERS = {
    "ОГЛАВЛЕНИЕ": "build_toc",
    "НОУТБУКИ": "build_notebooks",
}


def chapters():
    """[(номер, заголовок, [номера упражнений])] по файлам глав."""
    out = []
    for path in sorted((ROOT / "solutions" / "chapters").glob("ch*.tex")):
        num = int(path.stem[2:])
        text = path.read_text(encoding="utf-8")
        title = re.search(r"\\section\{(.*?)\}", text).group(1)
        exercises = re.findall(r"\\subsection\{\*?Упражнение ([\d.]+)", text)
        out.append((num, title, exercises))
    return out


def build_toc():
    rows = [
        "| Глава | Упражнений | PDF |",
        "|---|:-:|---|",
    ]
    total = 0
    for num, title, exercises in chapters():
        total += len(exercises)
        rows.append(
            f"| {title} | {len(exercises)} | "
            f"[ch{num:02d}.pdf]({PAGES}/ch{num:02d}.pdf) |"
        )
    rows.append(f"| **Всего** | **{total}** | [весь сборник]({PAGES}/main.pdf) |")
    rows.append("")
    rows.append(
        "В главах 14–16 упражнений нет — в книге они посвящены психологии, "
        "нейробиологии и приложениям."
    )
    return "\n".join(rows)


def build_notebooks():
    # упражнение -> глава, чтобы не полагаться на порядок словаря
    by_number = {}
    for _, (new, numbers, chapter, title) in NOTEBOOKS.items():
        by_number[tuple(numbers)] = (new, chapter, title)

    rows = [
        "| Упражнение | Ноутбук | О чём |",
        "|---|---|---|",
    ]
    # сортировка по номеру главы и номеру упражнения как по целым числам:
    # как дроби "2.11" оказалось бы раньше "2.5"
    def key(ns):
        major, minor = ns[0].split(".")
        return int(major), int(minor)

    for numbers in sorted(by_number, key=key):
        new, chapter, title = by_number[numbers]
        nums = ", ".join(numbers)
        rows.append(f"| {nums} | [`{new}.ipynb`](notebooks/{new}.ipynb) | {title} |")
    return "\n".join(rows)


def main():
    text = README.read_text(encoding="utf-8")
    original = text
    for name, func in MARKERS.items():
        block = globals()[func]()
        pattern = re.compile(
            rf"(<!-- {name}:НАЧАЛО -->).*?(<!-- {name}:КОНЕЦ -->)", re.S
        )
        if not pattern.search(text):
            raise SystemExit(f"в README нет маркеров {name}")
        text = pattern.sub(
            lambda m: m.group(1) + "\n" + block + "\n" + m.group(2), text
        )

    if "--check" in sys.argv:
        if text != original:
            raise SystemExit("README устарел: запустите python3 tools/build_index.py")
        print("README актуален")
        return
    README.write_text(text, encoding="utf-8")
    print("README обновлён")


if __name__ == "__main__":
    main()
