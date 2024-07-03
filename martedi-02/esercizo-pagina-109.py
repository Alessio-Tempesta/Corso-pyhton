# Creare una class Ristorante che permetta di destire alcune funzionalità di base:
# Requisiti:
# Definizione della classe:
# la classe dovrebbe avere un costruttore __init__ che accetta due parametriu: nome (nome del risotrante) e tipo_cucina (tipo di cucina offerta).
# Definire una attributo aperto che indica se il ristornate è aperto o chiuso. questo attributo deve essere impostato su flase di default (cioè il ristornante è chiuso).
# un dizionario menu dove dentro ci sono i piatti a prezzi che ha il ristorante
# 2:metodi della classe:
# descrivi_ristorante() un metodo che stampa una frase descrviendo il ristorante, includendo il nome e il tipo di cucina.
#stato_apertura(): un metodo che stampa se il ristorante è aperto o chiuso.
# apri_ristorante() un metodo che imposta l'attributo  aperto su true e stampa un messaggio che indicia che il risotrante è ora aperto.
# chiudi_ristorante(): un metodo che imposta l'attributo aperto su false e stampa un messaggio che indica il ristrnate ora è chiuso.

# 




# class Ristorante:
#     def __init__(self,nome,tipo_cucina):
#         self.nome = nome
#         self.tipo_cucina = tipo_cucina
#         self.aperto = False
#         self.menu = []
        
#         def stato_ristorante(self):
#             if self.aperto:
#                 print(f"Il ristorante {self.nome} è aperto.")
#             else:
#                 print(f"Il ristorante {self.nome} è chiuso.")
    
#         def apri_ristorante(self):
#             self.aperto = True
#             print(f"il risotrante {self.nome} è aperto")
            
#         def chiudi_ristorante(self):
#             self.aperto = False
#             print(f"il ristorante è {self.nome} è chiuso")
            
#         def aggiungi_al_menu(self, piatto, prezzo):
#             self.menu.append((piatto, prezzo))
#             print(f"il paitto {piatto} è sato aggiunto al menu")
            
#         def togli_dal_menu(self, piatto):
#             for e in self.menu:
#                 if e[0] == piatto:
#                     self.menu.remove(e)
#                     print(f"il piatto {piatto} è stato tolto dal menu")
#                     return
#                 print(f"il piatto { piatto } non cè nel menu ")