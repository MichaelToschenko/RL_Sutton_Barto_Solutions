#!/usr/bin/env python3
"""Готовит ноутбуки к публикации на GitHub.

Что делает:
  * переименовывает в вид NN_MM.ipynb, чтобы порядок совпадал с порядком глав;
  * заменяет tqdm.notebook/tqdm.auto на обычный tqdm и вычищает виджетные
    выводы — GitHub не умеет отрисовывать application/vnd.jupyter.widget-view+json
    и показывает такие ячейки пустыми;
  * приводит метаданные ядра к единому виду;
  * ставит единообразную шапку со ссылкой на соответствующую главу сборника.

Выводы ячеек намеренно сохраняются: именно они делают ноутбуки читаемыми
прямо на GitHub, без запуска.

    python3 tools/fix_notebooks.py            # править на месте, в notebooks/
    python3 tools/fix_notebooks.py --check    # только проверить, ничего не писать
"""
import json
import re
import sys
from pathlib import Path

PAGES = "https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions"

# старое имя -> (новое имя, номера упражнений, глава, краткое название)
NOTEBOOKS = {
    "2_5":    ("02_05", ["2.5"],        2,  "Нестационарный 10-рукий стенд: выборочное среднее против постоянного шага"),
    "2_11":   ("02_11", ["2.11"],       2,  "Параметрическое исследование для нестационарного случая"),
    "4_7":    ("04_07", ["4.7"],        4,  "Итерация по стратегиям: аренда машин Джека с модификациями"),
    "4_9":    ("04_09", ["4.9"],        4,  "Итерация по ценности: задача об азартном игроке"),
    "5_12":   ("05_12", ["5.12"],       5,  "Кольцевые гонки"),
    "6_9_10": ("06_09_10", ["6.9", "6.10"], 6, "Ветреный сеточный мир: ходы короля и стохастический ветер"),
    "7_2":    ("07_02", ["7.2"],        7,  "n-шаговый TD против суммы TD-ошибок"),
    "7_10":   ("07_10", ["7.10"],       7,  "Задача предсказания с разделённой стратегией"),
    "8_4":    ("08_04", ["8.4"],        8,  "Приз за исследование как бонус к выбору действия"),
    "8_8":    ("08_08", ["8.8"],        8,  "Однократная и ожидаемая выборка при разной ветвистости"),
    "11_3":   ("11_03", ["11.3"],       11, "Полуградиентное Q-обучение на контрпримере Бэрда"),
}

KERNELSPEC = {"display_name": "Python 3", "language": "python", "name": "python3"}

TQDM_IMPORTS = re.compile(r"from\s+tqdm\.(?:notebook|auto)\s+import")
WIDGET_MIME = "application/vnd.jupyter.widget-view+json"


def header_cell(numbers, chapter, title):
    nums = ", ".join(numbers)
    plural = "Упражнения" if len(numbers) > 1 else "Упражнение"
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# {plural} {nums}. {title}\n",
            "\n",
            "Саттон, Барто, «Обучение с подкреплением».\n",
            f"Полный разбор — в сборнике решений: "
            f"[глава {chapter} (PDF)]({PAGES}/ch{chapter:02d}.pdf).\n",
        ],
    }


def clean_outputs(cell):
    """Убирает виджетные выводы, оставляя текстовые и картиночные."""
    kept, dropped = [], 0
    for out in cell.get("outputs", []):
        data = out.get("data")
        if data and WIDGET_MIME in data:
            data.pop(WIDGET_MIME, None)
            out.get("metadata", {}).pop(WIDGET_MIME, None)
            if not data:
                dropped += 1
                continue
        kept.append(out)
    cell["outputs"] = kept
    return dropped


def process(path, new_name, numbers, chapter, title, check):
    nb = json.loads(path.read_text(encoding="utf-8"))
    report = []

    if nb.get("metadata", {}).get("kernelspec") != KERNELSPEC:
        nb.setdefault("metadata", {})["kernelspec"] = dict(KERNELSPEC)
        report.append("ядро")
    # версия интерпретатора у ноутбуков разъезжается — фиксируем только язык
    li = nb.get("metadata", {}).get("language_info")
    if li:
        li.pop("version", None)
    if nb.get("metadata", {}).pop("widgets", None) is not None:
        report.append("метаданные виджетов")

    dropped = 0
    replaced_imports = 0
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        dropped += clean_outputs(cell)
        src = cell["source"]
        for i, line in enumerate(src):
            if TQDM_IMPORTS.search(line):
                src[i] = TQDM_IMPORTS.sub("from tqdm import", line)
                replaced_imports += 1
    if dropped:
        report.append(f"виджетных выводов удалено: {dropped}")
    if replaced_imports:
        report.append(f"импортов tqdm исправлено: {replaced_imports}")

    # шапка
    head = header_cell(numbers, chapter, title)
    first = nb["cells"][0] if nb["cells"] else None
    is_title = (
        first
        and first["cell_type"] == "markdown"
        and re.match(r"\s*#+\s*Упражнени", "".join(first["source"]))
    )
    if is_title:
        nb["cells"][0] = head
        report.append("шапка заменена")
    else:
        nb["cells"].insert(0, head)
        report.append("шапка добавлена")

    # единственный H1 — наш; остальные заголовки первого уровня опускаем до H2
    demoted = 0
    for cell in nb["cells"][1:]:
        if cell["cell_type"] != "markdown":
            continue
        for i, line in enumerate(cell["source"]):
            if re.match(r"# (?!#)", line):
                cell["source"][i] = "#" + line
                demoted += 1
    if demoted:
        report.append(f"заголовков H1 понижено: {demoted}")

    target = Path("notebooks") / f"{new_name}.ipynb"
    if not check:
        target.write_text(
            json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
    print(f"{path.name:14s} -> {target.name:14s} {'; '.join(report)}")


def main():
    check = "--check" in sys.argv
    for old, (new, numbers, chapter, title) in NOTEBOOKS.items():
        src = Path(f"{old}.ipynb")
        if not src.exists():
            src = Path("notebooks") / f"{new}.ipynb"
        if not src.exists():
            print(f"пропущен: {old}.ipynb не найден")
            continue
        process(src, new, numbers, chapter, title, check)


if __name__ == "__main__":
    main()
