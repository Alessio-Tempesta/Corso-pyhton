# Esercizio 2: Manipolazione e Aggregazione dei Dati

# Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con pandas.

# Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.

# Caricare i dati in un DataFrame.
# Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario.
# Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.
# Trovare il prodotto più venduto in termini di Quantità.
# Identificare la città con il maggior volume di vendite totali.
# Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 1000 euro).
# Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.
# Visualizzare il numero di vendite per ogni città.



import pandas as pd

# Caricare i dati da un file CSV in un DataFrame
def carica_dati():
    path_csv = r'C:\Users\alete\OneDrive\Desktop\Corso-pyhton\mercoledi-17\esercizio-analisiEspolorativa\vendite.csv'
    return pd.read_csv(path_csv)

# Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario
def calcola_tot_vendite(df):
    df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']
    return df

# Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto
def calcola_totale_vendite_prodotto(df):
    return df.groupby('Prodotto')['Totale Vendite'].sum()

# Trovare il prodotto più venduto in termini di Quantità
def trova_prodotto_piu_venduto(df):
    return df.groupby('Prodotto')['Quantità'].sum().idxmax()

# Identificare la città con il maggior volume di vendite totali
def trova_citta_maggior_volume(df):
    return df.groupby('Città')['Totale Vendite'].sum().idxmax()

# Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore
def filtra_vendite_sopra_valore(df, valore):
    return df[df['Totale Vendite'] > valore]

# Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente
def ordina_per_totale_vendite(df):
    return df.sort_values(by='Totale Vendite', ascending=False)

# Visualizzare il numero di vendite per ogni città
def conta_vendite_per_citta(df):
    return df.groupby('Città').size().reset_index(name='Numero di Vendite')

# funzione per preparare i dati
def prepara_dati():
    df = carica_dati()
    df = calcola_tot_vendite(df)
    return df

# funzione menu principale
def menu(df):
    while True:
        print("\nMenu delle operazioni:")
        print("1. Calcolare il totale delle vendite per ciascun prodotto")
        print("2. Trovare il prodotto più venduto in termini di Quantità")
        print("3. Identificare la città con il maggior volume di vendite totali")
        print("4. Filtrare vendite superiori a un certo valore")
        print("5. Ordinare il DataFrame per il totale delle vendite in ordine decrescente")
        print("6. Visualizzare il numero di vendite per ogni città")
        print("0. Esci")
        
        scelta = input("Seleziona un'opzione: ")
        
        if scelta == "1":
            vendite_prodotto = calcola_totale_vendite_prodotto(df)
            print("\nTotale vendite per prodotto:")
            print(vendite_prodotto)
        elif scelta == "2":
            prodotto_piu_venduto = trova_prodotto_piu_venduto(df)
            print("\nProdotto più venduto in termini di Quantità:", prodotto_piu_venduto)
        elif scelta == "3":
            citta_maggior_volume = trova_citta_maggior_volume(df)
            print("\nCittà con il maggior volume di vendite totali:", citta_maggior_volume)
        elif scelta == "4":
            valore = float(input("Inserisci il valore soglia per le vendite: "))
            df_sopra_valore = filtra_vendite_sopra_valore(df, valore)
            print("\nVendite superiori a", valore, "euro:")
            print(df_sopra_valore)
        elif scelta == "5":
            df_ordinato = ordina_per_totale_vendite(df)
            print("\nDataFrame originale ordinato per Totale Vendite:")
            print(df_ordinato)
        elif scelta == "6":
            vendite_per_citta = conta_vendite_per_citta(df)
            print("\nNumero di vendite per ogni città:")
            print(vendite_per_citta)
        elif scelta == "0":
            break
        else:
            print("Opzione non valida. Riprova.")

df = prepara_dati()
menu(df)
