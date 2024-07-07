# 1- Ereditarietà : permette ad una classe di ereditare degli attrubuti e metodi da una classe base, promuovendo il riutilizzo del codice.
# classe base 
# class Veicolo:
#     def __init__(self, anno):
#         self.anno = anno

#     def mostra_anno(self):
#         print(f"L'anno del veicolo è {self.anno}")

# class Automobile(Veicolo):
#     def __init__(self, anno, marca):
#         # chiamo costruttore della classe base 
#         super().__init__(anno) 
#         self.marca = marca

#     def mostra_dettagli(self):
#         print(f"Questa automobile è del {self.anno} e della marca {self.marca}")

# # Utilizzo dell'ereditarietà
# auto = Automobile(2022, "Toyota")
# auto.mostra_anno()
# auto.mostra_dettagli()


# incapsulamento : 'incanpuslamento nasconde i dettagli di implemnentazione all'esterno di un oggetto e permette l'accesso controllato attraverso dei metodi pubblici
# classe base
# class ContoBancario:
#     def __init__(self, saldo_iniziale):
#         self.__saldo = saldo_iniziale #come attriubtuo privato
#     def deposita(self,importo):
#         if importo >0 :
#             self.__saldo += importo
#             print(f"il desposito di:  {importo}€ è stato effettuato , il nuovo saldo: {self.__saldo}€")
#         else:
#             print("L'importo del deposito deve essere maggiore")
#     def preleva(self, importo):
#         if 0 < importo <= self.__saldo:
#             self.__saldo -= importo
#             print(f"Prelievo di {importo}€ effettuato il  Nuovo saldo: {self.__saldo}€")
#         else:
#             print("Importo non valido o saldo insufficiente.")

# conto = ContoBancario(1000)
# conto.deposita(500)
# conto.preleva(200)


# Polimorifsimo : il polimorfismo permette ad oggeti di classi diverse di rispondere allo stesso metodo consentendo il trattamneto uniforme di oggetti di diverse classi.

# # classe base:
# class Animale:
#     def fai_verso(self):
#         pass

# class Cane(Animale):
#     def fai_verso(self):
#         return "Bau!"

# class Gatto(Animale):
#     def fai_verso(self):
#         return "Miao!"
    
    
# # funzione che utilizza il polimorfismo
# def fai_verso(animale):
#     print(animale.fai_verso())
    
# cane = Cane()
# gatto = Gatto()

# fai_verso(cane)
# fai_verso(gatto)
