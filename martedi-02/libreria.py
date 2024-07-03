class Libreria:
    def __init__(self):
        self.catologo = []
    
    def aggiungi_libro(self, libro):
        self.catologo.append(libro)
        
    def rimuovi_libro(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catologo.remove(libro)
                return
            print(f"il libro con isbn: {isbn} non trovato nel catalogo")
    
    def cerca_per_titolo(self, titolo):
        return [libro for libri in self.catalogo if libro.titolo.lower() == titolo.lower()]