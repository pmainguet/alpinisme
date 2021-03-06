#!/bin/bash

find * -iname "*.md" -type f -exec sh -c 'pandoc -f markdown-implicit_figures "${0}" -V linkcolor:blue -V geometry:a4paper -V geometry:margin=2cm -V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono" -o "${0%.md}.pdf"' {} \;
rm ./pdf/*.pdf
find . -iname "*.pdf" -type f -exec mv {} ./pdf \;