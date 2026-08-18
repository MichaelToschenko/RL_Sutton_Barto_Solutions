# Решения упражнений к книге Саттона и Барто

[![Сборка PDF](https://github.com/MichaelToschenko/RL_Sutton_Barto_Solutions/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/MichaelToschenko/RL_Sutton_Barto_Solutions/actions/workflows/build-pdf.yml)

Я прочитал «Обучение с подкреплением» Саттона и Барто от корки до корки и по ходу
решал все упражнения подряд. Здесь лежит то, что из этого получилось: 140 разборов,
включая помеченные в книге звёздочкой. Ссылки на страницы даны по русскому изданию.

Решения написаны в LaTeX и собираются в один PDF. Там, где задача требует посчитать
и построить графики, рядом лежит ноутбук с кодом. Читать его можно прямо здесь,
на GitHub, вместе со всеми картинками.

### 📄 [Читать сборник целиком (PDF)](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/main.pdf)

## Содержание

<!-- ОГЛАВЛЕНИЕ:НАЧАЛО -->
| Глава | Упражнений | PDF |
|---|:-:|---|
| Глава 1. Введение | 5 | [ch01.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch01.pdf) |
| Глава 2. Многорукие бандиты | 11 | [ch02.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch02.pdf) |
| Глава 3. Конечные марковские процессы принятия решений | 29 | [ch03.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch03.pdf) |
| Глава 4. Динамическое программирование | 10 | [ch04.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch04.pdf) |
| Глава 5. Методы Монте-Карло | 14 | [ch05.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch05.pdf) |
| Глава 6. Обучение на основе временных различий | 14 | [ch06.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch06.pdf) |
| Глава 7. n-шаговый бутстрэппинг | 11 | [ch07.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch07.pdf) |
| Глава 8. Планирование и обучение табличными методами | 8 | [ch08.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch08.pdf) |
| Глава 9. Предсказание с единой стратегией и аппроксимацией | 5 | [ch09.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch09.pdf) |
| Глава 10. Управление с единой стратегией и аппроксимацией | 9 | [ch10.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch10.pdf) |
| Глава 11. *Методы с разделенной стратегией и аппроксимацией | 4 | [ch11.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch11.pdf) |
| Глава 12. Следы приемлемости | 14 | [ch12.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch12.pdf) |
| Глава 13. Методы градиента стратегии | 5 | [ch13.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch13.pdf) |
| Глава 17. Передовые рубежи | 1 | [ch17.pdf](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/ch17.pdf) |
| **Всего** | **140** | [весь сборник](https://michaeltoschenko.github.io/RL_Sutton_Barto_Solutions/main.pdf) |

В главах 14-16 упражнений нет: в книге они про психологию, нейробиологию и приложения.
<!-- ОГЛАВЛЕНИЕ:КОНЕЦ -->

## Упражнения с кодом

Ноутбуки сохранены вместе с выводами и графиками, так что запускать ничего не нужно:
открываете и читаете.

<!-- НОУТБУКИ:НАЧАЛО -->
| Упражнение | Ноутбук | О чём |
|---|---|---|
| 2.5 | [`02_05.ipynb`](notebooks/02_05.ipynb) | Нестационарный 10-рукий стенд: выборочное среднее против постоянного шага |
| 2.11 | [`02_11.ipynb`](notebooks/02_11.ipynb) | Параметрическое исследование для нестационарного случая |
| 4.7 | [`04_07.ipynb`](notebooks/04_07.ipynb) | Итерация по стратегиям: аренда машин Джека с модификациями |
| 4.9 | [`04_09.ipynb`](notebooks/04_09.ipynb) | Итерация по ценности: задача об азартном игроке |
| 5.12 | [`05_12.ipynb`](notebooks/05_12.ipynb) | Кольцевые гонки |
| 6.9, 6.10 | [`06_09_10.ipynb`](notebooks/06_09_10.ipynb) | Ветреный сеточный мир: ходы короля и стохастический ветер |
| 7.2 | [`07_02.ipynb`](notebooks/07_02.ipynb) | n-шаговый TD против суммы TD-ошибок |
| 7.10 | [`07_10.ipynb`](notebooks/07_10.ipynb) | Задача предсказания с разделённой стратегией |
| 8.4 | [`08_04.ipynb`](notebooks/08_04.ipynb) | Приз за исследование как бонус к выбору действия |
| 8.8 | [`08_08.ipynb`](notebooks/08_08.ipynb) | Однократная и ожидаемая выборка при разной ветвистости |
| 11.3 | [`11_03.ipynb`](notebooks/11_03.ipynb) | Полуградиентное Q-обучение на контрпримере Бэрда |
<!-- НОУТБУКИ:КОНЕЦ -->

## Что где лежит

```
solutions/
  main.tex              точка сборки: преамбула, титул, список глав
  preamble.tex          пакеты и общие настройки
  chapters/chNN.tex     по файлу на главу
  figures/own/          графики, построенные в ноутбуках
  figures/book/         иллюстрации из книги, чтобы текст читался без неё под рукой
notebooks/              вычислительные эксперименты, NN_MM.ipynb по номеру упражнения
tools/                  скрипты сборки
```

## Как собрать самому

PDF пересобирается сам при каждом пуше в `main` и уезжает на GitHub Pages и в релиз
`latest`, так что вручную это обычно не нужно. Но если хочется:

```bash
bash tools/build_pdf.sh      # весь сборник и по PDF на главу, в solutions/build/
```

Понадобится TeX Live с поддержкой русского (`babel-russian`, `cm-super`) и пакетом
`algorithm2e`. Собирать нужно именно через **pdflatex**: из-за `T2A` и `inputenc`
xelatex преамбулу не переварит.

Если правите одну главу и не хотите ждать весь сборник, раскомментируйте
`\includeonly` в [`solutions/main.tex`](solutions/main.tex).

Для ноутбуков:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Оглавление в этом файле собирается из исходников командой
`python3 tools/build_index.py`, так что после правки глав его надо обновить.

## Лицензия

Код и текст решений под [MIT](LICENSE), берите и пользуйтесь. Картинки в
`solutions/figures/book/` взяты из книги и принадлежат правообладателям издания,
они здесь только для того, чтобы решения читались без неё под рукой.
