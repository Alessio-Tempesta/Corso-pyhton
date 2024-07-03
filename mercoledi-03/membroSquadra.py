# creare una classe base membroSqaudra e diverse classi figlie che rappresentano roli specifici all'interno della squadra di calcio,com Giocatore, Allenatore e assistente. 
# l'esrcizio consente di esploarare come differenti membri della squadra possono erediatare attributi comuni dalla classe base, ma anche come possono differire nei loro comportamenti e responsabiltà.abs
# classe MembroSquadra
# Attributi: nome (stringa), eta(int), metodi : descrivi() (stampa una descrizione generlae del membro della squadra)
# Classi derivate :
# Giocaotre :
#  attributi aggiuntivi come ruole (e.g , attacante, difensore) n.maglia
# metodi come gioca_partita() che possono includere azuioni specifiche del giocatore
# Allenatore: 
# attributi aggiuntivi come anni di ex
# metodi come dirige_allenamento() che dettagliano l'allenatore conduce gli allenamenti
# Assistente: Attributi aggiuntuivi come specilazziazione (fisoterapista, analsita di gicoo)
# metodi specifici del ruolo, coem supporta team() che può descrviere varie forme di supp. al team


# creazione Membrosqaudra classe padre
class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def descrivi(self):
        return f"Nome: {self.nome}, eta: {self.eta}"
    
# creazione sottoclasse Giocatore
class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        
        # metodi gioca partita e desc
    def gioca_partita(self):
        return  f"{self.nome} gioca nel ruolo {self.ruolo} con la maglia n.{self.numero_maglia}"
    
    def descrivi(self):
        return f"Nome: {self.nome}, Eta: {self.eta}, ruolo: {self.ruolo}, n.di maglia {self.numero_maglia}"
    
    
class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_exp):
        super().__init__(nome, eta)
        self.anni_di_exp = anni_di_exp
        
        # metodi dirigi allenamneto e la sua desc
    def dirige_allenamento(self):
        return f"{self.nome} conduce l'allenamneto con: {self.anni_di_exp}"
    
    def descrivi(self):
        return f"Nome:{self.nome}, eta: {self.eta}, anni di XP: {self.anni_di_exp}"
    
class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome,eta)            #costruttore della classe mebro sqadra
        self.specializzazione = specializzazione
        
    def supporta_team(self):
        return f"{self.nome} supporta il team come {self.specializzazione}"
    
    def descrivi(self):
        return f"Nome: {self.nome}, eta {self.eta}, specilizzato in {self.specializzazione}"



# istanze delle classi -> 
giocatore = Giocatore("Lionel messi", 37, "attaccante", 10)
giocatore = Giocatore("romelu lukaku", 31, "attacante", 9)
allenatore = Allenatore("Carlo ancelotti", 65, 20)
assistente = Assistente("Giuseppe", 30, "Fisioterapista")


print(giocatore.descrivi())
print(giocatore.gioca_partita())

print(allenatore.descrivi())
print(allenatore.dirige_allenamento())

print(assistente.descrivi())
print(assistente.supporta_team())