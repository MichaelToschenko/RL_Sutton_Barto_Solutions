# Решения упражнений к книге Саттона и Барто

[![Сборка PDF](https://github.com/MichaelToschenko/RL_Sutton_Barto_Solutions/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/MichaelToschenko/RL_Sutton_Barto_Solutions/actions/workflows/build-pdf.yml)

Разборы всех упражнений из книги Р. Саттона и Э. Барто «Обучение с подкреплением»
(Reinforcement Learning: An Introduction), сделанные при сплошном чтении книги —
самостоятельно и в полном объёме: **140 упражнений**, включая помеченные звёздочкой.
Ссылки на страницы даны по русскому изданию.

Решения оформлены в LaTeX и собираются в единый PDF. Упражнения, требующие
вычислительного эксперимента, дополнительно разобраны в Jupyter-ноутбуках —
их можно читать прямо здесь, на GitHub, вместе с графиками.

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

В главах 14–16 упражнений нет — в книге они посвящены психологии, нейробиологии и приложениям.
<!-- ОГЛАВЛЕНИЕ:КОНЕЦ -->

## Упражнения с вычислительным экспериментом

Ноутбуки сохранены вместе с выводами и графиками, поэтому открываются и читаются
прямо на GitHub — запускать ничего не нужно.

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

## Структура репозитория

```
solutions/
  main.tex              точка сборки: преамбула, титул, список глав
  preamble.tex          пакеты и общие настройки
  chapters/chNN.tex     по файлу на главу
  figures/own/          графики, построенные в ноутбуках
  figures/book/         иллюстрации из книги, приведённые для контекста
notebooks/              вычислительные эксперименты, NN_MM.ipynb по номеру упражнения
tools/                  скрипты сборки и поддержки репозитория
```

## Сборка

PDF пересобирается автоматически при каждом пуше в `main`
(см. [`.github/workflows/build-pdf.yml`](.github/workflows/build-pdf.yml))
и публикуется на GitHub Pages и в релизе `latest`. Локально:

```bash
bash tools/build_pdf.sh      # весь сборник + по PDF на главу, в solutions/build/
```

Нужен любой полный TeX Live с поддержкой русского (`babel-russian`, `cm-super`)
и пакетом `algorithm2e`. Документ собирается **pdflatex** — из-за `T2A` и
`inputenc` он не пройдёт через xelatex без правки преамбулы.

Чтобы быстро пересобрать одну главу, раскомментируйте `\includeonly` в
[`solutions/main.tex`](solutions/main.tex).

Для запуска ноутбуков:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

После правки глав или списка ноутбуков оглавление в этом файле обновляется
командой `python3 tools/build_index.py`.

## Лицензия

Код и текст решений — [MIT](LICENSE). Иллюстрации в `solutions/figures/book/`
взяты из книги, принадлежат правообладателям издания и приведены здесь только
для того, чтобы решения читались без неё под рукой.
