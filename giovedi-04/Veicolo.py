# creare una classe base Veicolo con attributi comuni a tutti i veicoli e metodi per operazioni comuni come l'accensione
# e lo spegnimento. Derivando questa classe, creeranno specifiche classi per Auto, Furgone e Motocicletta, aggiungendo
# caratteristiche uniche per ciascun tipo di veicolo. Infine, dovranno implementare una classe GestoreParcoVeicoli per
# amministrare l'insieme dei veicoli.


# Classe Veicolo: 
# # Attributi privati:
# _marca (stringa)
# _modello (stringa)
# _anno (intero)
# _accensione (booleano)
# Metodi:
# accendi(): cambia lo stato di _accensione a vero.
# spegni(): cambia lo stato di _accensione a falso.
# Classi Derivate:
# Auto:
# Attributi aggiuntivi come _numero_porte
# Metodo specifico come suona_clacson()
# Furgone:
# Attributi per _capacità_carico
# Metodo per carica() e scarica()
# Motocicletta:
# Attributo per _tipo (e.g., sportiva, touring)
# Metodo per esegui_wheelie() se il tipo è sportivo
# Classe GestoreParcoVeicoli:
# Attributi:
# _veicoli: lista di tutti i veicoli.
# Metodi:
# aggiungi_veicolo(veicolo): aggiunge un veicolo alla lista.
# rimuovi_veicolo(marca, modello): rimuove un veicolo specifico dalla lista.
# lista_veicoli(): stampa un elenco di tutti i veicoli nel parco.

# classe Veicolo base
class Veicolo:
    def __init__(self, marca, modello, anno):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False #di base false quindi spenta
        
        #metodo accendi 
    def accendi(self):
        self._accensione = True
        print(f"{self._marca} {self._modello}: il motore è accesso")
        
        # metodo spegni
    def spegni(self):
        self._accensione = False
        print(f"{self._marca} {self._modello} il motore è spento")


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self._numero_porte = numero_porte
        
    # metodo suona clacson
    def suona_clacson(self):
        print(f"{self._marca} {self._modello}: sta suonaando")
        
        # classe furgone derivata veciolo
class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, capacita_carico):
        super().__init__(marca, modello, anno)
        self._capacita_carico = capacita_carico
    
    def carica(self):
        print(f"{self._marca} {self._modello} : carica in corso")

    def scarica(self):
        print(f"{self._marca} {self._modello} scaricamneto in corso" )
        
class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self._tipo = tipo
        
    def esegui_wheelie(self):
        if self._tipo == "sportiva":
            print(f"{self._marca} {self._modello} : sta facendo un wheelie!!!! ")
        else:
            print(f"{self._marca} {self._modello} : la motocicletta non è di tipo sportivo")
            
# classe per gestione dei veicoli
class GestoreParcoVeicoli:
    def __init__(self):
        self._veicoli = []
        
    def aggiungi_veicolo(self, veicolo):
        self._veicoli.append(veicolo)
        print(f"Veicolo {veicolo._marca} {veicolo._modello } è  stato aggiunto al parco.")
    
    def rimuovi_veicolo(self, marca, modello):
        veicolo_trovato = False
        
        for veicolo in self._veicoli:
            if veicolo._marca == marca and veicolo._modello == modello:
                self._veicoli.remove(veicolo)
                veicolo_trovato = True
                print(f"Il veicolo {marca} {modello} rimosso dal parco")
                break
            
            # se il veciolo non è trovato
            
        if not veicolo_trovato:
            print(f"Veicolo { marca} {modello} non è stato trovato nel parco ")
    
    # stampa lista di veicoli
    def lista_veicoli(self):
        if not self._veicoli:
            print("non ci sono dei vecioli presenti nel parco")
        else:
            print("Quetsa è la lista dei vecioli nel parco:")
            for veicolo in self._veicoli:
                print(f" LA marca del veicolo è : {veicolo._marca} e {veicolo._modello}")
    

# test generali 
gestore = GestoreParcoVeicoli()

auto1 = Auto("Fiat", "500", 2020, 3)
auto2 = Auto("Porsche ", "Panamera", 2022, 5)
furgone1 = Furgone("Iveco", "Daily", 2019, 2000)
motocicletta1 = Motocicletta("Ducati", "Monster", 2021, "sportiva")

# Aggiunta dei veicoli al parco veicoli
gestore.aggiungi_veicolo(auto1)
gestore.aggiungi_veicolo(auto2)
gestore.aggiungi_veicolo(furgone1)
gestore.aggiungi_veicolo(motocicletta1)

gestore.lista_veicoli()

gestore.rimuovi_veicolo("Fiat", "500")

# Stampare la lista aggiornata dei veicoli nel parco veicoli
gestore.lista_veicoli()

#test su un'auto, un furgone e una motocicletta
auto1.accendi()
auto1.suona_clacson()

furgone1.accendi()
furgone1.carica()
furgone1.scarica()

motocicletta1.accendi()
motocicletta1.esegui_wheelie()