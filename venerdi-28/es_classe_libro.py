# Create un classe libro che ha al suo interno:
# -titolo;
# - autore;
# - prezzo;
# - codice isbn viene generato automaticamente in maniera randomica ogni volta che inserito un libro;
# - stato_prestito;

# Metodo

# Create poi 2 metodi:
# - Metodo sconto per applicare lo sconto della percentuale passata al prezzo;
# - Metodo prestito per cambiare lo stato del prestito, quindi se è libero diventa prestato, se è prestato diventa libero

# import random

# class Libro:
#     def __init__(self, titolo, autore, prezzo):
#         self.titolo = titolo
#         self.autore = autore
#         self.prezzo = prezzo
#         self.isbn = self.genera_isbn()
#         self.stato_prestito = "libero"

#     def genera_isbn(self):
#         return str(random.randint(1, 100))

#     def applica_sconto(self, percentuale):
#         if 0 <= percentuale <= 100:
#             self.prezzo -= self.prezzo * (percentuale / 100)
#         else:
#             print("Percentuale non valida")

#     def cambia_stato_prestito(self):
#         if self.stato_prestito == "libero":
#             self.stato_prestito = "prestato"
#         elif self.stato_prestito == "prestato":
#             self.stato_prestito = "libero"
#         else:
#             print("Stato prestito non valido")

#     def info_libro(self):
#         return f"Titolo: {self.titolo}, Autore: {self.autore}, Prezzo: {self.prezzo}, ISBN: {self.isbn}, Stato prestito: {self.stato_prestito}"

# # Creazione delle istanze di Libro
# libro1 = Libro("Il signore degli anelli", "J.R.R. Tolkien", 25)
# libro2 = Libro("Padre ricco padre povero", "R. Kiyosaki", 30)
# libro3 = Libro("Ciao", "Ciao", 10)

# # Stampa delle informazioni dei libri
# print(libro1.info_libro())
# print(libro2.info_libro())
# print(libro3.info_libro())

# # Cambio stato da prestito a libero per libro1
# libro1.cambia_stato_prestito()
# print("\nDopo il cambiamento dello stato:")
# print(libro1.info_libro())

# # Applicazione sconto del 5% a libro1
# libro1.applica_sconto(5)
# print("\nDopo l'applicazione dello sconto:")
# print(libro1.info_libro())



# Create tre classi:
# - classe madre mezzo;
# - Classe figlio moto;
# - Classe figlio auto.

# class Mezzo:
#     def __init__(self, marca, modello):
#         self.marca = marca
#         self.modello = modello
        
        
#         def desc(self):
#             return f"Mezzo :{self.marca}, {self.modello}"
        
        
        
#         class Moto(Mezzo):
#             def __init__(self, marca, modello, cilindrata):
#                 super().__init_(marca,modello)
#                 self.cilindrata = cilindrata
                
#         def desc(self):
#             return f"Moto : {self.marca} {self.modello} cC: {self.cilindrata}"
        
#         class Auto(Mezzo):
#             def __init__(self, marca, modello):
#             self.marca = marca
#             self.modello = modello