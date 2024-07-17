# Esercizio 1: Analisi Esplorativa dei Dati

# Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
# usando pandas.

# Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
# un gruppo di persone: Nome, Età, Città e Salario. 

# Caricare i dati in un DataFrame autogenerandoli casualmente .
# Visualizzare le prime e le ultime cinque righe del DataFrame.
# Visualizzare il tipo di dati di ciascuna colonna.
# Calcolare statistiche descrittive di base per le colonne numeriche (media,
# mediana, deviazione standard).
# Identificare e rimuovere eventuali duplicati.
# Gestire i valori mancanti sostituendoli con la mediana della rispettiva
# colonna.
# Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
# persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
# anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
# Salvare il DataFrame pulito in un nuovo file CSV.


import numpy as np
import pandas as pd

# Funzione per generare dati casuali
def genera_dati_casuali(n):
    data_set = {
        'Nome': [f'Persona{i}' for i in range(n)],
        'Età': np.random.randint(1, 100, size=n),
        'Città': np.random.choice(['Roma', 'Milano', 'Napoli', 'Torino'], size=n),
        'Salario': np.random.randint(20000, 150000, size=n)
    }
    return pd.DataFrame(data_set)

# Funzione per stampare informazioni principali del DataFrame
def stampa_informazioni(df):
    print("Prime 5 righe del DataFrame:")
    print(df.head())

    print("\nUltime 5 righe del DataFrame:")
    print(df.tail())

    print("\nTipo di dati di ciascuna colonna:")
    print(df.dtypes)

    print("\nStatistiche descrittive di base:")
    print(df.describe())

# Funzione per gestire duplicati
def gestisci_duplicati(df):
    df_cleaned = df.drop_duplicates()
    num_duplicates = len(df) - len(df_cleaned)
    if num_duplicates > 0:
        print(f"{num_duplicates} duplicati rimossi.")
    else:
        print("Nessun duplicato trovato.")
    return df_cleaned

# Funzione per gestire valori mancanti
def gestisci_valori_mancanti(df):
    df_filled = df.fillna(df.median())
    print("Valori mancanti gestiti con la mediana della rispettiva colonna.")
    return df_filled

# Funzione per aggiungere categoria età
def aggiungi_categoria_eta(df):
    def categorize_age(age):
        if age <= 18:
            return 'Giovane'
        elif age <= 65:
            return 'Adulto'
        else:
            return 'Senior'
    
    df['Categoria Età'] = df['Età'].apply(categorize_age)
    print("Categoria età aggiunta.")
    return df

def salva_csv(df):
    df.to_csv('dataset.csv', index=False)
    print("\nDataFrame salvato come '{dataset.csv}'")
    

def menu():
    df = None
    while True:
        print("\n Menu ")
        print("1. Genera dati casuali")
        print("2. stampa info")
        print("3. Gestisci duplicati")
        print("4. Gestisci valori mancanti")
        print("5. Aggiungi categoria età")
        print("6. Salva CSV")
        print("7. Esci")

        scelta = input("Inserisci il numero dell'operazione desiderata: ")
        
        if scelta == '1':
            n = int(input("inserisci il numero di righe da generare:"))
            df = genera_dati_casuali(n)
            print(f"Dati casuali generati con successo con {n} righe.")
            
        elif scelta == '2':
            if df is not None:
                stampa_informazioni(df)
            else:
                print("Nessun DataFrame presente. Genera dati casuali prima di procedere.")
                
        elif scelta == '3':
            if df is not None:
                df = gestisci_duplicati(df)
            else:
                print("Nessun DataFrame presente. Genera dati casuali prima di procedere.")
                
        elif scelta == '4':
            if df is not None:
                df = gestisci_valori_mancanti(df)
            else:
                print("nessun dataframe presente. devi generare dati casuali prima di procedere")
                
        elif scelta == '5':
            if df is not None:
                df = aggiungi_categoria_eta(df)
                salva_csv(df)
            else:
                print("Nessun DataFrame presente. Genera dati casuali prima di procedere.")

        elif scelta == '6':
            if df is not None:
                salva_csv(df)
            else:
                print("Nessun DataFrame presente. Genera dati casuali prima di procedere.")
        
        elif scelta == '7':
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Inserisci un numero da 1 a 7.")
            
menu()