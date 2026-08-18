#!/usr/bin/env bash
# Собирает сборник целиком и по одному PDF на каждую главу.
# Один и тот же скрипт используется локально и в GitHub Actions.
set -euo pipefail

cd "$(dirname "$0")/../solutions"
OUT=build
# \include пишет .aux рядом с исходником внутри выходного каталога,
# поэтому подкаталог нужно создать заранее
mkdir -p "$OUT/chapters"

echo "==> сборник целиком"
latexmk -pdf -outdir="$OUT" main.tex

echo "==> отдельные главы"
for src in chapters/ch*.tex; do
    ch=$(basename "$src" .tex)
    wrapper="$OUT/${ch}_standalone.tex"
    cat > "$wrapper" <<TEX
% Автогенерируется tools/build_pdf.sh, править бессмысленно.
\documentclass{article}
\input{preamble}
\begin{document}
\input{$src}
\end{document}
TEX
    # компиляция идёт из solutions/, поэтому \input{preamble} и \graphicspath
    # разрешаются относительно неё
    latexmk -pdf -outdir="$OUT" "$wrapper" >/dev/null
    mv "$OUT/${ch}_standalone.pdf" "$OUT/${ch}.pdf"
    echo "    $ch.pdf"
done

echo "==> готово: $(cd "$OUT" && ls -1 *.pdf | tr '\n' ' ')"
