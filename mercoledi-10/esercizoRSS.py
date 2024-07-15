# Scaricare l’RSS di ANSA Ultime Notizie e convertirlo in un file CSV e un file html.


import requests
import xml.etree.ElementTree as ET
import pandas as pd

url_rss = 'https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml'
risposta = requests.get(url_rss)
contenuto_rss = risposta.content

# analizza xml
root = ET.fromstring(contenuto_rss)

righe = []

for item in root.findall('.//item'):
    titolo = item.find('title').text
    descrizione = item.find('description').text
    data = item.find('pubDate').text
    righe.append({'Titolo': titolo, 'Descrizione': descrizione, 'Data': data})

df= pd.DataFrame(righe)

csv_path = 'ansa_notizie.csv'
df.to_csv(csv_path, index=False)

html_path = 'ansa_notizie.html'
df.to_html(html_path, index=False)

print(f'Dati salvati in {csv_path} e {html_path}')
