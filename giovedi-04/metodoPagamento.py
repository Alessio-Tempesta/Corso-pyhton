# # creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.

# Classe MetodoPagamento:
# Metodi:
# effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
# Classi Derivate:
# CartaDiCredito:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
# PayPal:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
# BonificoBancario:
# Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
# GestorePagamenti:
# Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.


class MetodoPagamento:
    def effettua_pagamento(self, importo):
        print(f"Pagamento dell'{importo} in euro effettuato")
        
        #classe con pagamneto carta 
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamnemto di questo {importo} euro fatto con carta di credito")
        
        #classe con pagamento Paypal
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamnemto di questo {importo} euro fatto con cPayPal")
        
        #classe con pagamento bonifico 
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamnemto di questo {importo} euro fatto con Bonifico Bancario")

# classe GestorePagamenti che utilizza metodo di pagamaneto

class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento
        
    def paga(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)
        
        
gestore_paga = GestorePagamenti(CartaDiCredito())
gestore_paga.paga(100)

gestore_paga = GestorePagamenti(PayPal())
gestore_paga.paga(150)

gestore_paga = GestorePagamenti(BonificoBancario())
gestore_paga.paga(200)


# menu per utente

def menu():
    while True:
        print("\nScegli il metodo di pagamento:")
        print("1. Carta di Credito")
        print("2. PayPal")
        print("3. Bonifico Bancario")
        print("4. Esci")
        scelta = input("Inserisci il numero della tua scelta:")
        
        if scelta == "1":
            metodo = CartaDiCredito()
        elif scelta == "2":
            metodo = PayPal()
        elif scelta == "3":
            metodo = BonificoBancario()
        elif scelta == '4':
            print("Esci dal programma")
            break
        else:
            print("scelta non valida. Riprova")
            continue
        
        importo = float(input("Inserisci l'importo d apagare:"))
        gestore = GestorePagamenti(metodo)
        gestore.paga(importo)
        menu()
        