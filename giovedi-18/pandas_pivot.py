# Esempio Pratico: Uso di pivot_table
# Supponiamo di avere un dataset che registra le vendite giornaliere di diversi
# prodotti in varie città. Potremmo voler analizzare le vendite medie per prodotto in
# ciascuna città.

import pandas as pd

# Dati di esempio
data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

print(pivot_df)


# Esempio Pratico: Uso di groupby
# Immaginiamo di voler calcolare il totale delle vendite per ciascun prodotto, utilizzando
# il dataset delle vendite giornaliere.

# Dati di esempio
data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

# Utilizzo di groupby per aggregare i dati
grouped_df = df.groupby('Prodotto').sum()

print(grouped_df)