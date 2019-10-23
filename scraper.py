"""Scrapes toti.eu.com/beatles for all song lyrics and dumps them to file.

The dump has the format:
    <title 1>\t<writers>\t<line 1>\\<line 2>\\...\\<line n>\n
    <title 2>\t<writers>\t<line 1>\\<line 2>\\...\\<line n>\n
    ...
    <title m>\t<writers>\t<line 1>\\<line 2>\\...\\<line n>\n
"""

import re
import requests
import random
from bs4 import BeautifulSoup

if __name__ == "__main__":
    with open('calaveritas_links.txt', 'r') as file_:
        links = file_.readlines()

    calaveritas = []
    for link in links:
        link = f"https://{link.strip()}"
        html = requests.get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        calaverita = soup.find("div", {"class" : "entry-content"})
        if calaverita is not None:
            lines = calaverita.get_text().replace("(adsbygoogle = window.adsbygoogle || []).push({});", "").split('\n')
            text = "\\".join([line for line in lines if line.strip()])
            print(text)
            calaveritas.append(text)

    random.shuffle(calaveritas)
    with open('calaveritas_dataset.txt', 'w') as file_:
        for i, calaverita in enumerate(calaveritas):
            file_.write(f'{i}\taba\t{calaverita}\n')
    
