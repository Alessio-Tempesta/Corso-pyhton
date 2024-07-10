# Scrivere un programma Python che scarica l’xml della home page ANSA e stampa tutte le informazioni della prima notizia.


# import requests
# import xml.etree.ElementTree as ET

# # Scaruca l'XMl ANSA
# url = "https://www.ansa.it/sito/notizie/sport/calcio/calcio_rss.xml"
# risposta = requests.get(url)
# contenuto_xml= risposta.content


# root = ET.fromstring(contenuto_xml)
# prima_notizia = root.find("channel/item")

# # estrazione notizie

# titolo = prima_notizia.findall("title", "link","description", ).text
# link = prima_notizia.find("link").text
# desc= prima_notizia.find("description").text
# pub_data = prima_notizia.find("pubDate").text

# print(f"il titolo è:", titolo, "\nIl link è :", link, "\nla sua descrzione:", desc, "\nla sua prima notizia è :", pub_data)