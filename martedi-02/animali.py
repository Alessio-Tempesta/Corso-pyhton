# Creare una classe base animale e diverse classi derivate che rappresentano diversi tipi di animali in uno zoo. ogni classe derivata avrà attributi e metodi specifici che riflettono le caratterstiche e comportamneti unici degli aniamlei che rappresenatno. class Animale ,nome eta metodi un metdo che stampa un suono generico dell'animale e classi figlie craerae almno tre classi figlie di animale es: leone, giraffa e pinguino. ogni classe avrà attributi e metodi specific: per esempio la classe leone potrebbe avere un metodo caccia() che stampa un messaggio su come  il leone sta cacciando  

# classe Animale
class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
        
    # metodo per fare verso
    def fai_verso(self):
        return f"{self.nome} fa il suo verso"
        

class Leone(Animale):
    def __init__(self, nome, eta, sesso):
        super().__init__(nome, eta)
        self.sesso = sesso
        
    def fai_verso(self):
        return "Ruggito!"
    
    def caccia(self):
        print(f"Il leone {self.nome} sta cacciando")
        

class Giraffa(Animale):
    def __init__(self, nome, eta, lunghezza_collo):
        super().__init__(nome, eta)
        self.lunghezza_collo = lunghezza_collo
    
    def fai_verso(self):
        return "Barrito!"
    
    def mangia_foglie(self):
        print(f"La giraffa {self.nome} sta mangiado le foglie degli alberi con il suo collo lungo {self.lunghezza_collo}")
        

class Pinguino(Animale):
    def __init__(self, nome, eta, tipo):
        super().__init__(nome, eta)
        self.tipo = tipo
    
    def fai_verso(self):
        return "Garrito!"
    
    def nuota(self):
        return f"Il pinguino {self.nome} sta nuotando nell'acqaua in antartide."

# creazione degli oggetti
leone = Leone("Simba", 10, "Maschio")
giraffa = Giraffa("Nome giraffa", 8, 5)
pinguino = Pinguino("Skipper", 4, "Pinguino di Madagascar")

# utilizzo dei metodi delle classi derivate
print(leone.fai_verso())       
leone.caccia()                 

print(giraffa.fai_verso())     
giraffa.mangia_foglie()        

print(pinguino.fai_verso())   
print(pinguino.nuota())        
