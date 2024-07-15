import requests
import json
import random

def carica_pokedex():
    try:
        with open("pokedex.json", "r") as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return {}

def salva_pokedex(pokedex):
    with open("pokedex.json", "w") as file:
        json.dump(pokedex, file, indent=4)

def ottieni_pokemon_casuale():
    numero = random.randint(1, 1002)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}")
    return response.json()

def estrai_dati_pokemon(pokemon_data):
    return {
        "id": pokemon_data["id"],
        "nome": pokemon_data["name"],
        "abilita": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
        "exp": pokemon_data["base_experience"],
        "altezza": pokemon_data["height"],
        "peso": pokemon_data["weight"]
    }

# Carica il Pokedex esistente
pokedex = carica_pokedex()

# Ottieni un Pokemon casuale
pokemon_data = ottieni_pokemon_casuale()
pokemon = estrai_dati_pokemon(pokemon_data)

# Verifica se il Pokemon è già nel Pokedex
if str(pokemon["id"]) not in pokedex:
    print(f"Hai incontrato un {pokemon['nome']} selvatico!")
    cattura = input("Vuoi catturarlo? (s/n): ").lower()
    
    if cattura == 's':
        pokedex[str(pokemon["id"])] = pokemon
        salva_pokedex(pokedex)
        print(f"\n{pokemon['nome']} è stato aggiunto al tuo Pokedex!")
    else:
        print(f"{pokemon['nome']} è fuggito!")
else:
    print(f"Hai incontrato un {pokemon['nome']}. È già nel tuo Pokedex!")