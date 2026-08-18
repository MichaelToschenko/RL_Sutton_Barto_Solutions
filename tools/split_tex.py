#!/usr/bin/env python3
"""Разрезает монолитный main.tex на преамбулу и файлы глав.

Одноразовый скрипт: запускается один раз при переезде со сборника-монолита
на структуру solutions/{preamble.tex, main.tex, chapters/chNN.tex}.
Сохранён в репозитории, чтобы разрезку можно было воспроизвести или откатить.

    python3 tools/split_tex.py ИСХОДНЫЙ_main.tex solutions/
"""
import re
import sys
from pathlib import Path

# Заголовки глав 12 и 13 в исходнике записаны без слова «Глава N» —
# приводим к единому виду, чтобы оглавление было однородным.
TITLE_FIXES = {
    "Следы приемлемости": (12, "Глава 12. Следы приемлемости"),
    "Методы градиента стратегии": (13, "Глава 13. Методы градиента стратегии"),
}

HYPERREF = r"""
% --- навигация по документу -------------------------------------------------
% hyperref загружается до algorithm2e: обратный порядок ломает нумерацию
% строк в окружении algorithm.
\usepackage[unicode, hidelinks]{hyperref}
\hypersetup{
    bookmarksnumbered = true,
    bookmarksopen     = true,
    pdftitle          = {Ответы к книге «Обучение с подкреплением», Саттон и Барто},
    pdfsubject        = {Решения упражнений},
}
"""


def chapter_number(title):
    """Номер главы по заголовку \\section."""
    if title in TITLE_FIXES:
        return TITLE_FIXES[title][0]
    m = re.match(r"Глава\s+(\d+)", title)
    if not m:
        raise SystemExit(f"не удалось определить номер главы: {title!r}")
    return int(m.group(1))


def main():
    src = Path(sys.argv[1]).read_text(encoding="utf-8")
    out = Path(sys.argv[2])
    lines = src.split("\n")

    # 1. Преамбула: всё до \title, дальше — титульный блок до \begin{document}.
    i_title = next(i for i, l in enumerate(lines) if l.startswith(r"\title"))
    i_begin = next(i for i, l in enumerate(lines) if l.startswith(r"\begin{document}"))
    i_end = max(i for i, l in enumerate(lines) if l.startswith(r"\end{document}"))

    preamble = lines[1:i_title]          # без \documentclass — он остаётся в main.tex
    title_block = lines[i_title:i_begin]

    # algorithm2e требует, чтобы hyperref был загружен раньше него
    i_alg = next(i for i, l in enumerate(preamble) if "algorithm2e" in l)
    preamble = preamble[:i_alg] + HYPERREF.strip("\n").split("\n") + [""] + preamble[i_alg:]

    (out / "preamble.tex").write_text(
        "% Преамбула сборника. Подключается из main.tex и из сборок отдельных глав.\n"
        + "\n".join(preamble).rstrip()
        + "\n",
        encoding="utf-8",
    )

    # 2. Тело: режем по \section, \part выносим в main.tex.
    body = lines[i_begin + 1 : i_end]
    body = [l for l in body if not l.startswith((r"\maketitle", r"\tableofcontents"))]

    skeleton = []        # строки нового main.tex между \tableofcontents и \end{document}
    chapters = {}        # номер главы -> строки
    current = None

    for line in body:
        if line.startswith(r"\section{"):
            title = re.match(r"\\section\{(.*)\}\s*$", line).group(1)
            num = chapter_number(title)
            if title in TITLE_FIXES:
                line = "\\section{%s}" % TITLE_FIXES[title][1]
            current = num
            chapters[num] = [line]
            skeleton.append("\\include{chapters/ch%02d}" % num)
        elif line.startswith(r"\part{"):
            # \part в классе article не начинает страницу сам — \newpage обязателен
            skeleton.append("")
            skeleton.append(r"\newpage")
            skeleton.append(line)
            skeleton.append("")
            current = None
        elif line.strip() == r"\newpage" and current is None:
            pass          # \newpage перед \part уже добавлен выше
        elif current is None:
            if line.strip():
                raise SystemExit(f"текст вне главы: {line!r}")
        else:
            chapters[current].append(line)

    # Хвостовой \newpage у главы бесполезен: \include сам делает \clearpage
    for num, body_lines in chapters.items():
        while body_lines and body_lines[-1].strip() in ("", r"\newpage"):
            body_lines.pop()
        path = out / "chapters" / ("ch%02d.tex" % num)
        path.write_text("\n".join(body_lines) + "\n", encoding="utf-8")

    # 3. Новый main.tex
    main_tex = [
        r"\documentclass{article}",
        r"\input{preamble}",
        "",
        *title_block,
        "",
        "% Раскомментируйте, чтобы быстро пересобрать одну главу:",
        r"% \includeonly{chapters/ch06}",
        "",
        r"\begin{document}",
        r"\maketitle",
        r"\tableofcontents",
        *skeleton,
        "",
        r"\end{document}",
    ]
    (out / "main.tex").write_text("\n".join(main_tex) + "\n", encoding="utf-8")

    total = 0
    for num in sorted(chapters):
        n_ex = sum(1 for l in chapters[num] if l.startswith(r"\subsection{"))
        total += n_ex
        print("ch%02d.tex  строк %5d  упражнений %3d" % (num, len(chapters[num]), n_ex))
    print("итого глав %d, упражнений %d" % (len(chapters), total))


if __name__ == "__main__":
    main()
