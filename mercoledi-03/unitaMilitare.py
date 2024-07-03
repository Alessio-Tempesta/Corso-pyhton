# estendere una classe base UnitaMilitare per creare diverse unita specializzate, ciascuna con compiti e metodi specifici
# inoltre, implementare una classe controllo militare che eredita da tuttw le altre classi per gestire e tenere traccia dellediverse unità.
# 1.classe unitàMilitare:
#     attributi:
#         Nome(stringa): nome dell' unita
#         numero_soldati (intero): numero di soldati nell'unità
#     metodi:
#         muovi(): stampa un messaggio si movimento dell'unita.
#         attacca(): stampa un messaggio sull'attacco
#         ritira(): gestisce il ritiro strategico.
# 2 classi derviate:
#     Fanteria:
#         costruisci_trincea() : costitusice difese temporanee.
#         Artiglieria:
#             calibra_artiglieria() calibra i pezzi di artiglieria per la precsione.
#         Cavalleria:
#             esplora_terreno() : esplora l'area per raccolgiere informazioni sul nemico.
#         SupportoLogistico:
#         rifornisci_unità() gestisce il rifornimento e la manutenzione.

#     Ricongnizione:
#       conduci_ricognizone() conduce missioni di sorveglianza.
# 3 classe ControlloMilitare:
# eredita da tutte le classi precedenti.
# attributi aggiuntivi:
# unita_registrate: dizionario/due liste per tenere traccia delle unità create.
# Metodi:
# registra_unità(unita): aggiunge un'unita al registro.
# mostra_unità(): elenca tutte le unità registarte.
# dettagli_unità(nome): mostra dettagli specifici di un'unita.










# -1 definiamo claasse base unita miliotare
class UnitàMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    # Metodo per il movimento dell'unità
    def muovi(self):
        print(f"L'unità {self.nome} si sta muovendo.")
        
    # Metodo per l'attacco dell'unità
    def attacca(self):
        print(f"L'unità {self.nome} sta iniziando l'attacco.")
            
    # Metodo per la ritirata dell'unità
    def ritira(self):
        print(f"L'unità {self.nome} si sta ritirando.")


# 2- Creazione delle classi derivate

class Fanteria(UnitàMilitare):
    # Metodo per costruire trincee
    def costruisci_trincea(self):
        print(f"L'unità di fanteria {self.nome} sta costruendo una trincea...")

class Artiglieria(UnitàMilitare):
    # Metodo dell'artiglieria 
    def calibra_artiglieria(self):
        print(f"L'unità di artiglieria {self.nome} sta calibrando i pezzi di artiglieria")

class Cavalleria(UnitàMilitare):
    # Metodo della cavalleria 
    def esplora_terreno(self):
        print(f"L'unità di cavalleria {self.nome} sta esplorando il terreno")

class SupportoLogistico(UnitàMilitare):
    # Metodo del supporto logistico
    def rifornisci_unità(self):
        print(f"L'unità di supporto logistico {self.nome} sta facendo rifornimento e manutenzione")

class Ricognizione(UnitàMilitare):
    # Metodoper la ricognzione
    def conduci_ricognizione(self):
        print(f"L'unità di ricognizione {self.nome} sta conducendo una missione di sorveglianza")


# Classe ControlloMilitare che eredita tutte le classi precedenti:
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self):
        super().__init__("Controllo militare", 0)  
        self.unità_registrate = []  
    
    # Metodo per registrare un'unità
    def registra_unita(self, unita):
        self.unità_registrate.append(unita)  # Aggiungiamo un'unità al registro
    
    # Metodo per mostrare tutte le unità registrate
    def mostra_unità(self):
        print("Unità registrate:")
        for unita in self.unità_registrate:
            print(f"Unità: {unita.nome}")
    
    # Metodo per mostrare i dettagli di una specifica unità
    def dettagli_unita(self, nome):
        unita_non_trovata = True  #  se l'unità non è stata trovata nel registro
        for unita in self.unità_registrate:
            if unita.nome == nome:
                unita_non_trovata = False  # se l'unita è stata trovata 
                print(f"Dettagli dell'unità {nome}:")
                print(f"Numero di soldati: {unita.numero_soldati}")
                unita.muovi()  # Chiama il metodo muovi() dell'unità
                unita.attacca()  # Chiam il metodo attacca() dell'unità
                unita.ritira()  # Chiama il metodo ritira() dell'unità
                break
        
        if unita_non_trovata:
            print(f"Unità {nome} non trovata nel registro.")  # Mex se l'unità non è trovata nel registro


# Test dell'istanza ControlloMilitare

controllo_militare = ControlloMilitare()

# Registrazione di alcune unità di diversi tipi
controllo_militare.registra_unita(Fanteria("Fante squadra Alpha", 100))
controllo_militare.registra_unita(Artiglieria("Artiglieria Delta00", 1000))
controllo_militare.registra_unita(SupportoLogistico("Supporto Fieramosca", 50))
controllo_militare.registra_unita(Cavalleria("Cavalleria 021", 60))
controllo_militare.registra_unita(Ricognizione("Squadra di Ricognizione", 20))

# Mostra le unità registrate
controllo_militare.mostra_unità()
print()

# Mostriamo i dettagli di alcune unità specifiche
controllo_militare.dettagli_unita("Fante squadra Alpha")
print()
controllo_militare.dettagli_unita("Artiglieria Delta00")
print()
controllo_militare.dettagli_unita("Supporto Fieramosca")
print()
controllo_militare.dettagli_unita("Cavalleria 021")
print()
controllo_militare.dettagli_unita("Squadra di Ricognizione")
print()
controllo_militare.dettagli_unita("Unita non esistente")  
print()
