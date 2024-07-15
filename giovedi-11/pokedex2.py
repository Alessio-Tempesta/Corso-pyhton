import requests
import json
import random
import os

def cerca_pokemon():
    numero = random.randint(1, 1002)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}")
    
    dizionario_pokedex = response.json()
    
    nome = dizionario_pokedex.get("forms")[0].get("name")
    id = numero
    abilita = [dato.get("ability").get("name") for dato in dizionario_pokedex.get("abilities")]
    exp = dizionario_pokedex.get("base_experience")
    altezza = dizionario_pokedex.get("height")
    peso = dizionario_pokedex.get("weight")

    return {
        "ID": id,
        "Nome": nome,
        "Abilità": abilita,
        "Exp": exp,
        "Altezza": altezza,
        "Peso": peso
    }

def carica_pokedex():
    if os.path.exists("pokedex.json"):
        with open("pokedex.json", "r") as file:
            return json.load(file)
    else:
        return {}

def salva_pokedex(pokedex):
    with open("pokedex.json", "w") as file:
        json.dump(pokedex, file, indent=4, ensure_ascii=False)

def aggiungi_pokemon():
    pokedex = carica_pokedex()
    pokemon = cerca_pokemon()
    
    if str(pokemon["ID"]) not in pokedex:
        pokedex[str(pokemon["ID"])] = pokemon
        print(f"Hai catturato:")
        for chiave, valore in pokemon.items():
            print(f"{chiave}: {valore}")
        
        salva_pokedex(pokedex)
    else:
        print(f"Pokémon ID: {pokemon['ID']} Nome: {pokemon['Nome']} è già nel Pokédex.")

print("Benvenuto in Pokemon!\n")
while True:
    print("Cerca Pokemon...")
    aggiungi_pokemon()
    print("\n")

    continua = input("Desideri cercare un altro Pokemon? (si/no): ").strip().lower()
    if continua != "si":
        print("Arrivederci")
        break