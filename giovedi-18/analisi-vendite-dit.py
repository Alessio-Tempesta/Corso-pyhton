# Esercizio 1: Analisi di Vendite Fittizie
# Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite
# generato casualmente, applicando le tecniche di pivot e groupby.

# Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
# include i seguenti campi: "Data", "Città", "Prodotto" e "Vendite". I dati
# devono essere generati per un periodo di un mese, con vendite registrate
# per tre diverse città e tre tipi di prodotti.

# Generazione dei Dati: Utilizzare numpy per creare un set di dati
# casuali.
# Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
# le vendite medie di ciascun prodotto per città.
# Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
# vendite totali per ogni prodotto.

import pandas as pd
import numpy as np

# Parametri per la generazione dei dati
date_range = pd.date_range(start='2023-06-01', end='2023-06-30', freq='D')
città = ['Milano', 'Roma', 'Napoli']
prodotti = ['Prodotto1', 'Prodotto2', 'Prodotto3']
num_vendite = len(date_range) * len(città) * len(prodotti)

# Debugging per la generazione dei dati
print("Lunghezza date_range:", len(date_range))
print("Lunghezza città:", len(città))
print("Lunghezza prodotti:", len(prodotti))
print("Numero totale di vendite previste:", num_vendite)

# Generazione dati casuali per le vendite
dates = np.tile(date_range, len(città) * len(prodotti))
città_scelta = np.repeat(città, len(date_range) * len(prodotti) // len(città))
prodotto_scelto = np.tile(prodotti, len(date_range) * len(città) // len(prodotti))
vendite = np.random.randint(1, 100, size=num_vendite)

# Debugging delle dimensioni degli array
print("Lunghezza dates:", len(dates))
print("Lunghezza città_scelta:", len(città_scelta))
print("Lunghezza prodotto_scelto:", len(prodotto_scelto))
print("Lunghezza vendite:", len(vendite))

# Creazione del DataFrame
df = pd.DataFrame({
    'Data': dates,
    'Città': città_scelta,
    'Prodotto': prodotto_scelto,
    'Vendite': vendite
})

# Stampa del DataFrame per verificare la correttezza
print("\nDataFrame delle Vendite:")
print(df.head())

# Calcolo della tabella pivot e delle vendite totali come nell'esempio precedente
tabella_pivot = df.pivot_table(values='Vendite', index='Città', columns='Prodotto', aggfunc='mean')
vendite_totali = df.groupby('Prodotto')['Vendite'].sum()

# Stampa dei risultati
print("\nTabella Pivot delle Vendite Medie:")
print(tabella_pivot)
print("\nVendite Totali per Prodotto:")
print(vendite_totali)
