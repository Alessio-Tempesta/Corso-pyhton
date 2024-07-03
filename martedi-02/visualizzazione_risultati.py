class VisualizzazioneRisultati:
    def __init__(self, totale, media, vendite, vendite_sup_alla_media):
        self.totale = totale
        self.media = media
        self.vendite = vendite
        self.vendite_sup_alla_media = vendite_sup_alla_media
        
        
        
        def mostra_risultati(self):
            # visualizza ris del totale, della media e venidte sopra la media
            if self.vendite:
                print(f"il totale delle vendite :{self.tot}")
                print(f"la media delle vendite: {self.media}")
            else:
                print("Non sono presneti dei dati")
                
            if self.vendite_sup_alla_media:
                print("venidte suepriroi alla media:", self.vendite_sup_alla_media)