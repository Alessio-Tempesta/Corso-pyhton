# Esercizio: Analizzatore di Dati di Vendita
# Sei stato incaricato di scrivere un programma Python che analizza un insieme di dati di vendita. I dati di vendita sono rappresentati come una lista di numeri, dove ciascun numero rappresenta l'importo totale delle vendite in un giorno specifico. Il tuo programma dovrebbe fare quanto segue:

# Requisiti:
# Inserimento dei Dati: Chiedi all'utente di inserire una serie di importi di vendita, separati da spazi. Converti questi importi in una lista di numeri interi.
# Gestione delle Eccezioni: Durante la conversione degli importi in numeri interi, gestisci qualsiasi ValueError che possa sorgere a causa di un inserimento errato (ad esempio, l'utente inserisce una lettera invece di un numero), informando l'utente dell'errore e chiedendogli di reinserire i dati.
# Calcolo del Totale e della Media: Calcola il totale e la media delle vendite. Stampa entrambi i valori con un messaggio appropriato. Se la lista è vuota (ad esempio, se l'utente non inserisce alcun dato), stampa un messaggio che indica che non sono presenti dati di vendita.
# Vendite Sopra la Media: Trova e stampa una lista di tutti i giorni in cui le vendite hanno superato la media delle vendite di tutto il periodo. Assicurati di gestire correttamente il caso in cui non ci siano vendite sopra la media.
# Visualizzazione dei Risultati: Per ogni punto sopra, stampa i risultati in modo chiaro e leggibile, con messaggi appropriati che spiegano cosa sta mostrando il programma.

class DatiVendite:
    def __init__(self):
        self.vendite = []
        
    def inserisci_dati(self):
        while True:
            try:
                # Chiedere all'utente di inserire una serie di importi separati da spazi
                input_dati = input("inserisci importi di vendita, separati da spazi:")
                # conv. gli input in una list di num
                self.vendite = [int(valore) for valore in input_dati.split()]
                break  #esce dal se l'input è valdio
            except:
                print("Errore, insesrisci solo dei numeri interi separati da spazi")