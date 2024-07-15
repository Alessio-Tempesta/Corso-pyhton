# Create un programma python che permette tramite le api
# https://open-meteo.com/en/docs (per le previsioni metereologiche) e
# https://www.bigdatacloud.com/free-api/free-reverse-geocode-tocity-
# api#getStarted (per l’ottenimento in automatico della propria
# langitudine e latitudine tramite l’indirizzo ip), di vedere le previsione
# metereologiche.
# L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
# visionare oltre che le temperature anche la velocità del vento e le
# probabili precipitazioni.

import json

def converti_json_dict():
    with open("file.json", "r") as file:
        contenuto = file.read()
    dizionario_json = json.loads(contenuto)
    print(dizionario_json["colore"])

def converti_dict_json():
    dizionario = {"colore":"blu","frutto":"mela"}
    json2= json.dumps(dizionario)
    
    with open("file.json","w") as file:
        file.write(json2)
    print("file creato!")


import requests
def request_and_json():
    risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.5921&longitude=9.5734&hourly=temperature_2m")
    risposta = requests.request("GET", "https://api.open-meteo.com/v1/forecast?latitude=45.5921&longitude=9.5734&hourly=temperature_2m")
    risposta_text = risposta.text

    risposta_json = json.loads(risposta_text)

    for element in risposta_json:
        print(element)

def request1():
    risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.5921&longitude=9.5734&hourly=temperature_2m")
    risposta_json = risposta.json()
    print(type(risposta_json))

request1()