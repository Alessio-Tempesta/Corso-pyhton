# Create con l'oop un pokedex e 4 pokemon, bulbasaur, charmender,
# # squirtle e Pikachu, le caratteristiche dei pokemon sono mosse, punti vita, tipo
# 1) All'avvio vi fa scegliere uno dei pokemon possibili e lo aggiunge al pokedex;
# 2) Il gioco va avanti con voi che cercate i pokemon, quando trovate un pokemon vedete il suo livello e razza e decidete se combattere;
# 3) se combattete potete catturarlo solo se gli azzerate i punti vita, altrimenti scappa!

# class Pokedex:
#     def __init__(self, nome):
#         self.nome = nome
#         self.dizionario = {}

#     def aggiungi_pokemon(self, pokemon):
#         self.dizionario[pokemon.nome] = pokemon

# class Pokemon:
#     def __init__(self, nome, lv=1):
#         self.nome = nome
#         self.lv = lv
#         self.mosse = []
#         self.punti_vita = 0
#         self.tipo = ""

#     def mostra_info(self):
#         print(f"Razza: {type(self).__name__}")
#         print(f"Livello: {self.lv}")
#         print(f"Tipo: {self.tipo}")

#     def attacca(self, mossa, avversario):
#         punti_attacco = mossa.punti_attacco
#         avversario.punti_vita -= punti_attacco
#         print(f"{self.nome} usa {mossa.nome}!")
#         print(f"{avversario.nome} perde {punti_attacco} punti vita.")

# class Mossa:
#     def __init__(self, nome, punti_attacco):
#         self.nome = nome
#         self.punti_attacco = punti_attacco

# class Bulbasaur(Pokemon):
#     def __init__(self, nome, lv=1):
#         super().__init__(nome, lv)
#         self.mosse = [
#             Mossa("Foglielama", 20),
#             Mossa("Velenozanna", 15),
#             Mossa("Parassiseme", 10)
#         ]
#         self.punti_vita = 45 + (lv * 5)
#         self.tipo = "Erba/Veleno"

# class Charmender(Pokemon):
#     def __init__(self, nome, lv=1):
#         super().__init__(nome, lv)
#         self.mosse = [
#             Mossa("Braciere", 25),
#             Mossa("Lanciafiamme", 30),
#             Mossa("Ruggito", 5)
#         ]
#         self.punti_vita = 50 + (lv * 5)
#         self.tipo = "Fuoco"

# class Squirtle(Pokemon):
#     def __init__(self, nome, lv=1):
#         super().__init__(nome, lv)
#         self.mosse = [
#             Mossa("Pistola_acqua", 22),
#             Mossa("Idropompa", 28),
#             Mossa("Colpo_coda", 15)
#         ]
#         self.punti_vita = 55 + (lv * 5)
#         self.tipo = "Acqua"

# class Pikachu(Pokemon):
#     def __init__(self, nome, lv=1):
#         super().__init__(nome, lv)
#         self.mosse = [
#             Mossa("Fulmine", 27),
#             Mossa("Tuono", 32),
#             Mossa("Elettro_palla", 18)
#         ]
#         self.punti_vita = 70 + (lv * 5)
#         self.tipo = "Elettro"

# # Creazione del Pokedex e aggiunta dei Pokémon
# pokemon1 = Pokedex("Mio")
# pokemon1.aggiungi_pokemon(Bulbasaur("mio_bulbasaur", 5))
# pokemon1.aggiungi_pokemon(Charmender("mio_charmender", 5))
# pokemon1.aggiungi_pokemon(Squirtle("Mio_squirtle", 5))
# pokemon1.aggiungi_pokemon(Pikachu("mio_pikachu", 5))

# # Scelta iniziale di un Pokémon
# print("Benvenuto nella tua avventura Pokémon!")

# while True:
#     scelta = input("Scegli un Pokémon tra Bulbasaur, Charmender, Squirtle e Pikachu: ").strip().lower()

#     if scelta == "bulbasaur":
#         pokemon_scelto = pokemon1.dizionario["mio_bulbasaur"]
#         break
#     elif scelta == "charmender":
#         pokemon_scelto = pokemon1.dizionario["mio_charmender"]
#         break
#     elif scelta == "squirtle":
#         pokemon_scelto = pokemon1.dizionario["Mio_squirtle"]
#         break
#     elif scelta == "pikachu":
#         pokemon_scelto = pokemon1.dizionario["mio_pikachu"]
#         break
#     else:
#         print("Scelta non valida. Riprova.")

# print(f"Hai scelto {scelta.capitalize()}!")

# # Simulazione del gioco di caccia Pokémon
# while True:
#     print("Trovi un Pokémon!")
#     # Esempio di un Pokémon avversario
#     pokemon_trovato = Pikachu("pokemon_avversario", 5)
#     pokemon_trovato.mostra_info()

#     decisione = input("Vuoi combattere con questo Pokémon? (sì/no) ")
#     if decisione.lower() == "sì":
#         while pokemon_trovato.punti_vita > 0 and pokemon_scelto.punti_vita > 0:
#             # Turno del giocatore
#             print(f"È il turno di {pokemon_scelto.nome}.")
#             print("Scegli una mossa:")
#             for idx, mossa in enumerate(pokemon_scelto.mosse):
#                 print(f"{idx + 1}. {mossa.nome}")

#             scelta_mossa = int(input("Quale mossa scegli? ")) - 1
#             if 0 <= scelta_mossa < len(pokemon_scelto.mosse):
#                 pokemon_scelto.attacca(pokemon_scelto.mosse[scelta_mossa], pokemon_trovato)
#             else:
#                 print("Mossa non valida. Perdi il turno.")

#             # Verifica se il Pokémon avversario è stato sconfitto
#             if pokemon_trovato.punti_vita <= 0:
#                 print(f"Hai catturato {type(pokemon_trovato).__name__}!")
#                 break

#             # Turno del Pokémon avversario
#             if pokemon_trovato.punti_vita > 0:
#                 print(f"È il turno di {pokemon_trovato.nome}.")
#                 mossa_avversario = random.choice(pokemon_trovato.mosse)
#                 pokemon_trovato.attacca(mossa_avversario, pokemon_scelto)

#                 # Verifica se il giocatore è stato sconfitto
#                 if pokemon_scelto.punti_vita <= 0:
#                     print("Hai perso il combattimento!")
#                     break

#         # Uscita dal ciclo principale di gioco
#         break
#     else:
#         print("Il Pokémon è scappato.")
