

# Generador de Calaveritas Literarias

(Inspirado de <https://github.com/EugenHotaj/beatles>)

Este script genera Calaveritas literarias utilizando Machine Learning.
El conjunto de datos es sacado de diferentes calaveritas literarias de
una pagina de internet.


## Para ejecutar

    pipenv install
    pipenv run python bigram_model.py


## Para generar el dataset

    chmod +x scrapper.sh
    ./scrapper.sh <nombre-del-tipo-de-calaverita> >> calaverita_links.txt
    python scraper.py

