# Create con l'oop un pokedex e 4 pokemon, bulbasaur, charmender,
# # squirtle e Pikachu, le caratteristiche dei pokemon sono mosse, punti vita, tipo
# 1) All'avvio vi fa scegliere uno dei pokemon possibili e lo aggiunge al pokedex;
# 2) Il gioco va avanti con voi che cercate i pokemon, quando trovate un pokemon vedete il suo livello e razza e decidete se combattere;
# 3) se combattete potete catturarlo solo se gli azzerate i punti vita, altrimenti scappa!
import random

class Pokemon:
    def __init__(self, nome, tipo, mosse, punti_vita, attacco=0.0):
        self.nome = nome
        self.tipo = tipo
        self.mosse = mosse
        self.punti_vita = punti_vita
        self.attacco = attacco

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - HP: {self.punti_vita} - Attacco: {self.attacco}"

    def attacca(self):
        attacco_scelto = random.choice(self.mosse)
        danni_inflitti = random.randint(5, 15)
        print(f"{self.nome} usa {attacco_scelto} e infligge {danni_inflitti} danni!")
        return danni_inflitti

    def subisci_danno(self, danni):
        self.punti_vita -= danni
        if self.punti_vita <= 0:
            self.punti_vita = 0
            print(f"{self.nome} è stato sconfitto!")
        else:
            print(f"{self.nome} ha ancora {self.punti_vita} HP.")

class Pokedex:
    def __init__(self):
        self.pokemons = []

    def aggiungi_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{pokemon.nome} è stato aggiunto al pokedex")

    def mostra_pokemon(self):
        if len(self.pokemons) == 0:
            print("Il Pokedex è vuoto!")
        else:
            for pokemon in self.pokemons:
                print(pokemon)

def scegli_pokemon_iniziale():
    pokemons_disponibili = [
        Pokemon("Bulbasaur", "Erba", ["Foglie Lama", "Frustata", "Parassiseme"], 50, 45),
        Pokemon("Charmander", "Fuoco", ["Braciere", "Fiammata", "Azione"], 40, 55),
        Pokemon("Squirtle", "Acqua", ["IdroPompa", "Pistolacqua", "Bollaraggio"], 45, 50),
        Pokemon("Pikachu", "Elettrico", ["Tuononda", "Tuono", "Fulmine"], 60, 60)
    ]

    print("Scegli il tuo Pokémon iniziale:")
    for i in range(len(pokemons_disponibili)):
        print(f"{i+1}. {pokemons_disponibili[i]}")

    scelta = int(input("Inserisci il numero del Pokémon scelto: ")) - 1
    return pokemons_disponibili[scelta]

def cerca_pokemon():
    pokemons_disponibili = [
        Pokemon("Bulbasaur", "Erba", ["Foglie Lama", "Frustata", "Parassiseme"], 50, 45),
        Pokemon("Charmander", "Fuoco", ["Braciere", "Fiammata", "Azione"], 40, 55),
        Pokemon("Squirtle", "Acqua", ["IdroPompa", "Pistolacqua", "Bollaraggio"], 45, 50),
        Pokemon("Pikachu", "Elettrico", ["Tuononda", "Tuono", "Fulmine"], 60, 60)
    ]

    pokemon_trovato = random.choice(pokemons_disponibili)
    print(f"Hai incontrato un {pokemon_trovato.nome} selvatico di tipo {pokemon_trovato.tipo}.")

    return pokemon_trovato

def combatti(pokedex, pokemon_selvatico):
    print(f"Combatterai contro {pokemon_selvatico.nome}")

    while pokemon_selvatico.punti_vita > 0:
        danni_inflitti = pokemon_selvatico.attacca()
        pokemon_selvatico.subisci_danno(danni_inflitti)

        if pokemon_selvatico.punti_vita <= 0:
            print(f"Hai sconfitto {pokemon_selvatico.nome}!")
            cattura = input("Vuoi catturarlo? (sì/no): ").lower()
            if cattura == "sì":
                pokemon_selvatico.punti_vita = random.randint(20, 40)  # Ripristina i punti vita a un valore casuale
                pokedex.aggiungi_pokemon(pokemon_selvatico)
                print(f"Hai catturato {pokemon_selvatico.nome}!")
            else:
                print(f"{pokemon_selvatico.nome} è scappato!")
            break

def fuga():
    print("Sei fuggito dal combattimento!")

def menu_combattimento():
    print("Cosa vuoi fare?")
    print("1. Combattere")
    print("2. Fuggire")

pokedex = Pokedex()
pokemon_iniziale = scegli_pokemon_iniziale()
pokedex.aggiungi_pokemon(pokemon_iniziale)

while True:
    scelta_da_fare = input("\nCosa vuoi fare? (cerca, mostra, esci): ").lower()

    if scelta_da_fare == "cerca":
        pokemon_selvatico = cerca_pokemon()
        menu_combattimento()
        combatti_decisione = input("Inserisci il numero dell'azione: ")
        if combatti_decisione == "1":
            combatti(pokedex, pokemon_selvatico)
        elif combatti_decisione == "2":
            fuga()
    elif scelta_da_fare == "mostra":
        pokedex.mostra_pokemon()
    elif scelta_da_fare == "esci":
        print("Grazie per aver giocato!")
        break

