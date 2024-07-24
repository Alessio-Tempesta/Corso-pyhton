# Creazione e Caricamento

# Spiegazione: Questa categoria include metodi per leggere dati da file
# esterni come CSV, Excel, o database SQL, e per creare DataFrame
# direttamente da strutture dati come dizionari, liste, o altri
# DataFrame.

import pandas as pd

# Creazione di un DataFrame da un dizionario

data = {'nome': ['Alice', 'Bob'], 'età': [25, 30]}

df = pd.DataFrame(data)
# Caricamento di un DataFrame da un file CSV
df_csv = pd.read_csv('data.csv')


# Esplorazione e Pulizia
# Spiegazione: Questi metodi aiutano a esplorare i dati per capire
# meglio la loro struttura e distribuzione e a pulire i dati rimuovendo
# o correggendo valori mancanti o duplicati.


# Visualizzazione delle statistiche descrittive
print(df.describe())

# Rimozione dei valori mancanti

df_clean = df.dropna()


# Selezione e Filtraggio
# Spiegazione: Pandas fornisce metodi per selezionare specifiche colonne
# o righe da un DataFrame, e per filtrare i dati basandosi su condizioni
# logiche.

# Selezione di una colonna
ages = df['età']

# Filtraggio basato su una condizione
adults = df[df['età'] >= 18]


# Manipolazione dei Dati
# Spiegazione: Include funzioni per modificare l'ordine dei dati,
# combinarli con altri set di dati, o cambiare la loro struttura
# organizzativa.

# Ordinamento dei dati per età
df_sorted = df.sort_values(by='età')

# Unione di due DataFrame
merged_df = pd.merge(df, df_csv, on='nome')



# Trasformazioni
# Spiegazione: Questi metodi permettono di applicare funzioni a colonne
# o righe per trasformare i dati in un modo più utile per l'analisi.

# Applicazione di una funzione a una colonna

df['età_doppia'] = df['età'].apply(lambda x: x * 2)


# Output:
# Spiegazione: Metodi per esportare i DataFrame in diversi formati di
# file come CSV, Excel, o JSON per l'utilizzo esterno o per salvataggio.


# Esportazione di un DataFrame in un file CSV

df.to_csv('data_output.csv')


# Serie Temporali:
# Spiegazione: Pandas offre strumenti specifici per manipolare date e
# tempi, permettendo di analizzare serie temporali, cambiare la
# frequenza dei dati, e generare periodi di tempo.

# Generazione di una serie di date
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

# Resampling dei dati di una serie temporale
df_resampled = df.resample('M').mean()

