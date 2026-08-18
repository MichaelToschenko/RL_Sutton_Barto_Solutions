#!/usr/bin/env python3
"""Вставляет в главы сборника ссылки на ноутбуки с вычислительным экспериментом.

Строка \notebook{...}{...} ставится после последнего \end{solution} нужного
упражнения. Скрипт идемпотентен: если ссылка уже стоит, упражнение пропускается.

    python3 tools/add_notebook_links.py
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fix_notebooks import NOTEBOOKS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# номер упражнения -> имя ноутбука
TARGETS = {}
for _, (new, numbers, chapter, _title) in NOTEBOOKS.items():
    for n in numbers:
        TARGETS[n] = (new, chapter)


def main():
    added = skipped = 0
    for chapter in sorted({c for _, c in TARGETS.values()}):
        path = ROOT / "solutions" / "chapters" / f"ch{chapter:02d}.tex"
        lines = path.read_text(encoding="utf-8").split("\n")

        # границы упражнений внутри главы
        bounds = [i for i, l in enumerate(lines) if l.startswith(r"\subsection{")]
        bounds.append(len(lines))

        inserts = []  # (позиция, строка)
        for b, (start, stop) in enumerate(zip(bounds, bounds[1:])):
            m = re.match(r"\\subsection\{\*?Упражнение (\d+\.\d+)", lines[start])
            if not m or m.group(1) not in TARGETS:
                continue
            number = m.group(1)
            if number not in TARGETS or TARGETS[number][1] != chapter:
                continue
            block = lines[start:stop]
            if any(r"\notebook{" in l for l in block):
                skipped += 1
                continue
            ends = [i for i, l in enumerate(block) if l.strip() == r"\end{solution}"]
            if not ends:
                print(f"  упражнение {number}: не найден \\end{{solution}}, пропущено")
                continue
            pos = start + ends[-1] + 1
            inserts.append((pos, "\\notebook{%s}{%s}" % (TARGETS[number][0], number)))
            added += 1

        for pos, line in reversed(inserts):
            lines.insert(pos, line)
        if inserts:
            path.write_text("\n".join(lines), encoding="utf-8")
            print(f"ch{chapter:02d}.tex: вставлено ссылок {len(inserts)}")

    print(f"итого добавлено {added}, пропущено как уже стоящие {skipped}")


if __name__ == "__main__":
    main()
