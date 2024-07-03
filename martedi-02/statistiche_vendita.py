class StatisticheVendite:
    def __init__(self, vendite):
        self.vendite = vendite
        self.totale
        self.media
    
    def calcolo_tot_e_media(self):
        # Calcolo il totale e la media delle vendite
        if not self.vendite:
            self.totale and self.media == 0 
        else:
            # calcolo tot vendite
            self.tot = sum(self.vendite)
            # calcola media vendite
            self.media = self.tot / len(self.vendite)
        return self.tot, self.media
    
    def vendite_sopra_media(self):
        if self.media == 0:
            return [vendita for vendita in self.vendite if vendita > self.media]
                