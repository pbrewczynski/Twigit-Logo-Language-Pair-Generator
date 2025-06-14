Current bulk prompt:

process_png.py default-background.png  --svg-dir input_language_pairs --postfix "" --output-dir "output-icons-bulk" -sc 0.85 --offset-x 25 --shadow --shadow-color "#1a7569ff" --shadow-offset-x -20 --shadow-offset-y 20 --shadow-blur 0.0

./main.py --top-country fr --top-fill-type gradient --right-country de --right-fill-type gradient --right-direction vertical


# en-uk
python3 svg_styler_cli.py --output my_logo \
    --left-country "United Kingdom" \
    --left-fill-type flag-svg \
    --left-zoom 104.3 \
    --left-pan-x 13.5 \
    --left-pan-y 0.0 \
    --top-country "United Kingdom" \
    --top-fill-type flag-svg \
    --top-zoom 100.0 \
    --top-pan-x 0.0 \
    --top-pan-y 0.0 \
    --right-country "Ukraine" \
    --right-fill-type gradient \
    --right-direction vertical \
    --right-transition 41.9

#es-en
python3 svg_styler_cli.py --output my_logo \
    --left-country "Spain" \
    --left-fill-type gradient \
    --left-direction vertical \
    --left-transition 6.4 \
    --top-country "Spain" \
    --top-fill-type gradient \
    --top-direction vertical \
    --top-transition 6.0
#es pl
python3 svg_styler_cli.py --output my_logo \
    --left-country "Spain" \
    --left-fill-type gradient \
    --left-direction vertical \
    --left-transition 6.4 \
    --top-country "Spain" \
    --top-fill-type gradient \
    --top-direction vertical \
    --top-transition 6.0 \
    --right-country "Poland" \
    --right-fill-type gradient \
    --right-direction vertical \
    --right-transition 41.9

#it en
python3 code/svg_styler_cli.py --output output/it-en \
    --top-country "Italy" \
    --top-fill-type gradient \
    --top-direction horizontal \
    --top-transition 69.4

#uk-pl
python3 svg_styler_cli.py --output my_logo \
    --left-country "Ukraine" \
    --left-fill-type gradient \
    --left-direction vertical \
    --left-transition 41.9 \
    --top-country "Ukraine" \
    --top-fill-type gradient \
    --top-direction vertical \
    --top-transition 42.3 \
    --right-country "Poland" \
    --right-fill-type gradient \
    --right-direction vertical \
    --right-transition 41.9


#zh-en
python3 svg_styler_cli.py --output my_logo \
    --left-country "China" \
    --left-fill-type flag-svg \
    --left-zoom 100.0 \
    --left-pan-x -51.9 \
    --left-pan-y 0.0 \
    --top-country "China" \
    --top-fill-type flag-svg \
    --top-zoom 203.5 \
    --top-pan-x 7.7 \
    --top-pan-y 34.6

python3 svg_styler_cli.py --output my_logo \
    --left-country "Russia" \
    --left-fill-type gradient \
    --left-direction vertical \
    --left-transition 99.0 \
    --top-country "Russia" \
    --top-fill-type gradient \
    --top-direction vertical \
    --top-transition 99.0

python3 svg_styler_cli.py --output my_logo \
    --left-country "Israel" \
    --left-fill-type gradient \
    --left-direction horizontal \
    --left-transition 20.0 \
    --top-country "Israel" \
    --top-fill-type gradient \
    --top-direction horizontal \
    --top-transition 20.0
# sim hebrew?
