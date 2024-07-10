# Create con l'oop un pokedex e 4 pokemon, bulbasaur, charmender,squirtle e Pikachu
# le caratteristiche dei pokemon sono mosse, punti vita, tipo

class Pokedex:
        def __init__(self,nome):
            self.nome = nome
            self.dizionario = {}
        
        def aggiungi_pokemon(self,pokemon):
            self.dizionario[pokemon.nome] = pokemon 

        def stampa_diz (self):
            print(self.nome)           


class Pokemon:
    
    sfidanti = }
    def __init__(self, nome):
        self.nome = nome
        self.mosse = {}
        self.punti_vita = 0
        self.tipo = ""
        self.livello = 0
        
    def sfida_pokemon(self):
        lista_pokemon = ["Bulbasaur","Charmender","Squirtle","Pikachu"]
        self.sfidanti[pokemon.nome] = pokemon 
        print(lista_pokemon)
        scelta1 = input("Quale pokemon vuoi sfidare: ")
        if Pokemon.livello() == :
            if scelta1 == "Bulbasaur":
                print("inizia la sfida!")

            elif scelta1 == "Charmender":
                print("inizia la sfida")
            elif scelta1 == "Squirtle":
                print("inizia la sfida")
            elif scelta1 == "Pikachu":
                print("inizia la sfida")
            else: 
                print("pokemon non trovato")

    def livello_pokemon(self,livello):
        
        self.livello += 1

    def combattimento(self):
        print(f"hai incontrato {bulbasaur}")
        x=input("scegli che mossa utilizzare")

class Bulbasaur(Pokemon):
    def __init__(self, nome):
        super().__init__(nome)
        self.mosse = {"Foglielama":30,"Frustata":50,"Parassiseme":20}
        self.punti_vita =  45
        self.tipo = "Erba/Veleno"
        self.livello = 1
    
    
class Charmender(Pokemon):
    def __init__(self, nome):
        super().__init__(nome)
        self.mosse = {"Braciere":50,"Lanciafiamme":40,"Ruggito":10}
        self.punti_vita =  50 
        self.tipo = "Fuoco"
        self.livello = 1
                            
class Squirtle(Pokemon):
    def __init__(self, nome):
        super().__init__(nome)
        self.mosse = {"Pistola_acqua":10,"Idropompa":20,"Colpo_coda":20}
        self.punti_vita =  55 
        self.tipo = "Acqua"
        self.livello = 1
                            
                            
class Pikachu(Pokemon):
    def __init__(self, nome):
        super().__init__(nome)
        self.mosse = {"Fulmine":50,"Tuono":50,"Elettro_palla":50}
        self.punti_vita = 70 
        self.tipo = "Elettro"
        self.livello = 1


print("Benvenuto nella tua avventura Pokémon!")
print("Scegli uno dei seguenti Pokémon per iniziare:")
pokemon1 = Pokedex("Mio_Bulbasaur")
pokemon2 = Pokedex("Mio_Charmender")
pokemon3 = Pokedex("Mio_Squirtle")
pokemon4 = Pokedex("Mio_Pikachu")
pokemon1.stampa_diz()
pokemon2.stampa_diz()
pokemon3.stampa_diz()
pokemon4.stampa_diz()

scelta = input("Quale Pokémon vuoi scegliere? ")

if scelta == pokemon1.nome:
    print(f"Hai scelto {scelta}!")

elif scelta == pokemon2.nome:
    print(f"Hai scelto {scelta}!")

elif scelta == pokemon3.nome:
    print(f"Hai scelto {scelta}!")

elif scelta == pokemon4.nome:
    print(f"Hai scelto {scelta}!")




pokemon1.aggiungi_pokemon(Bulbasaur("mio_bulbasaur"))
pokemon1.aggiungi_pokemon(Charmender("mio_charmender"))
pokemon1.aggiungi_pokemon(Squirtle("Mio_squirtle"))
pokemon1.aggiungi_pokemon(Pikachu("mio_pikachu"))

print(pokemon1.dizionario)

""" Simulazione del gioco di caccia Pokémon
    while True:
        input("Premi Invio per cercare un Pokémon...")
        pokemon_trovato = pokemon1.trova_pokemon()
        print("Hai trovato un Pokémon!")
        pokemon_trovato.mostra_info()

        decisione = input("Vuoi combattere con questo Pokémon? (sì/no) ")
        if decisione.lower() == "sì":
            if pokemon_trovato.punti_vita == 0:
                print(f"Hai catturato {type(pokemon_trovato).name}!")
                break
            else:
                print(f"Hai combattuto contro {type(pokemon_trovato).name}.")
                print("Il Pokémon è scappato!")

        else:
            print("Il Pokémon è scappato!")
else:
    print("Scelta non valida. Riprova.")
  """