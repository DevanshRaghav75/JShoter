import re
import sys
import requests
import threading
from JShoter.core.args import web_url
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from JShoter.core.colors import GRAY, GRAY, RED, RESET, GREEN

html = requests.get(web_url).content
soup = BeautifulSoup(html, "html.parser")

js_files = []

def extractor(web_url):
    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            url = script.attrs.get("src")
            js_files.append(url)

def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.submit(extractor, web_url)
    for i in js_files:
        print(i)
    with open('js_files', 'w') as f:
        for i in js_files:
            print(i, file=f)
    print('')
    print(GREEN + "[+] " + RESET + "Total JS files found:",(len(js_files)))