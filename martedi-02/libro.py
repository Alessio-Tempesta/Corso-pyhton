# Esercizio: Immagina di gestire una libreria. Crea due classi: Libro e Libreria.

# La classe Libro dovrebbe avere gli attributi:
# titolo
# autore
# isbn (numero identificativo unico per ogni libro)
# Inoltre, dovrebbe avere un metodo descrizione() che restituisce una stringa che descrive il libro usando tutti e tre gli attributi.
# La classe Libreria dovrebbe avere l'attributo:
# catalogo (una lista che conterrà oggetti della classe Libro)
# La classe Libreria dovrebbe avere i seguenti metodi:
# aggiungi_libro(libro): che prende in input un oggetto della classe Libro e lo aggiunge al catalogo.
# rimuovi_libro(isbn): che rimuove un libro dal catalogo in base al suo ISBN.
# cerca_per_titolo(titolo): che restituisce una lista di libri che corrispondono al titolo dato.
# mostra_catalogo(): che stampa una descrizione di tutti i libri presenti nel catalogo.

class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        
    def descrizione(self):
        return f"Titolo:{self.titolo}, Autore: {self.autore}, coduice isbn: {self.isbn} "