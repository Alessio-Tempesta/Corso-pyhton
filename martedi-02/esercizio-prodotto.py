# creato classe prodotto con vari attributi

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

# metodo per calcoare il profitto
        def calcola_profitto(self):
            return self.prezzo_vendita - self.costo_produzione
        
    # esmpio di classi derivate da prodotto + attributi specifici
    
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia
                
                
class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione,prezzo_vendita)
        self.materiale = materiale
                
    # inizzializzazione class fabbrica con un dizionario inventario
class Fabbrica:
    def __init__(self):
        self.inventario = {}
                
    def aggiungi_prodotto(self, prodotto, quantità):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantità
        else:
            self.inventario[prodotto.nome] = quantità
                
                
                
    def vendi_prodotto(self, prodotto, quantità):
        if prodotto.nome in self.inventario and self.inventario[prodotto.nome] >= quantità:
            self.inventario[prodotto.nome] -= quantità
            profitto = prodotto.calcola_profitto() * quantità
            print(f"Profitto ricavato dalla venidta : {profitto}")
        else:
            print("Prodotto non disponibile oppure non cè in magazzino")
                
                
    def resi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita
                
                
# Test per la creazuine prodotti
smartphone = Elettronica("iphone", 100, 1500, "3 anni" )
maglia = Abbigliamento("T-shirt-bianca", 5, 20, "Cotone")

fabbrica = Fabbrica()

fabbrica.aggiungi_prodotto(smartphone, 15)
fabbrica.aggiungi_prodotto(maglia, 15)

print("inventariio:", fabbrica.inventario)

# Vendita dei prodotti
fabbrica.vendi_prodotto(smartphone, 5)
fabbrica.vendi_prodotto(maglia,1)





# # Classe Prodotto con vari attributi
# class Prodotto:
#     def __init__(self, nome, costo_produzione, prezzo_vendita):
#         self.nome = nome
#         self.costo_produzione = costo_produzione
#         self.prezzo_vendita = prezzo_vendita

#     # Metodo per calcolare il profitto
#     def calcola_profitto(self):
#         return self.prezzo_vendita - self.costo_produzione

# # Classi derivate da Prodotto con attributi specifici
# class Elettronica(Prodotto):
#     def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
#         super().__init__(nome, costo_produzione, prezzo_vendita)
#         self.garanzia = garanzia

# class Abbigliamento(Prodotto):
#     def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
#         super().__init__(nome, costo_produzione, prezzo_vendita)
#         self.materiale = materiale

# # Classe Fabbrica con un dizionario inventario
# class Fabbrica:
#     def __init__(self):
#         self.inventario = {}

#     def aggiungi_prodotto(self, prodotto, quantita):
#         if prodotto.nome in self.inventario:
#             self.inventario[prodotto.nome] += quantita
#         else:
#             self.inventario[prodotto.nome] = quantita

#     def vendi_prodotto(self, prodotto, quantita):
#         if prodotto.nome in self.inventario and self.inventario[prodotto.nome] >= quantita:
#             self.inventario[prodotto.nome] -= quantita
#             profitto = prodotto.calcola_profitto() * quantita
#             print(f"Profitto ricavato dalla vendita: {profitto}")
#         else:
#             print("Prodotto non disponibile oppure quantità insufficiente in magazzino")

#     def resi_prodotto(self, prodotto, quantita):
#         if prodotto.nome in self.inventario:
#             self.inventario[prodotto.nome] += quantita
#         else:
#             self.inventario[prodotto.nome] = quantita

# # Test per la creazione prodotti
# smartphone = Elettronica("iPhone", 100, 1500, "3 anni")
# maglia = Abbigliamento("T-shirt bianca", 5, 20, "Cotone")

# # Creazione della fabbrica
# fabbrica = Fabbrica()

# # Aggiunta dei prodotti all'inventario
# fabbrica.aggiungi_prodotto(smartphone, 15)
# fabbrica.aggiungi_prodotto(maglia, 15)

# print("Inventario iniziale:", fabbrica.inventario)

# # Vendita dei prodotti
# fabbrica.vendi_prodotto(smartphone, 5)
# fabbrica.vendi_prodotto(maglia, 1)

# # Visualizzazione dell'inventario dopo la vendita
# print("Inventario dopo le vendite:", fabbrica.inventario)
