from dati_vendite import DatiVendite
from statistiche_vendita import StatisticheVendite
from visualizzazione_risultati import VisualizzazioneRisultati

def visualizza():
    
    dati_vendite = DatiVendite()
    dati_vendite.inserisci_dati()
    
    # Calcolo delle statistiche
    statistiche = StatisticheVendite(dati_vendite.vendite)
    totale, media = statistiche.calcola_totale_e_media()
    vendite_superiori_alla_media = statistiche.vendite_sopra_media()

    # Visualizzazione dei risultati
    visualizzazione = VisualizzazioneRisultati(totale, media, dati_vendite.vendite, vendite_superiori_alla_media)
    visualizzazione.mostra_risultati()