# Partendo da questo dataframe su kaggle https://www.kaggle.com/datasets/vikrishnan/boston-house-prices :
# -analizzate il tipo di dati,
# # - sistemate gli elementi mancanti - verificate se ci sono correlazioni - create un grafico a mappa di calore.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# # Specifica il percorso del file CSV
# percorso_file = "martedi-23-07/housing.csv"

# # Carica il DataFrame
# try:
#     df = pd.read_csv(percorso_file)
# except FileNotFoundError:
#     print(f"Errore: il file '{percorso_file}' non è stato trovato.")
# else:
#     # Analisi dei tipi di dati
#     print("Tipi di dati: \n", df.dtypes)

#     # Converti colonne numeriche che sono lette come stringhe
#     for col in df.columns:
#         if df[col].dtype == 'object':
#             # Prova a convertire le colonne oggetto in numeriche
#             df[col] = pd.to_numeric(df[col], errors='coerce')

#     # Controlla i valori mancanti
#     valori_mancanti = df.isnull().sum()
#     print("\nElementi mancanti per colonna: \n", valori_mancanti)

#     # Gestisci i valori mancanti
#     # Sostituisce i valori mancanti con la mediana per le colonne numeriche
#     df.fillna(df.median(numeric_only=True), inplace=True)

#     # Verifica se ci sono ancora valori mancanti
#     valori_mancanti_dopo = df.isnull().sum()
#     print("\nElementi mancanti dopo la sostituzione: \n", valori_mancanti_dopo)

#     # Calcola la matrice di correlazione solo per colonne numeriche
#     correlazione = df.select_dtypes(include=[np.number]).corr()

#     # Visualizza la matrice di correlazione con una heatmap
#     plt.figure(figsize=(12, 8))
#     sns.heatmap(correlazione, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
#     plt.title('Mappa di calore della matrice di correlazione')
#     plt.show()




"""Partendo da questo dataframe su kaggle https://www.kaggle.com/datasets/vikrishnan/boston-house-prices :
-analizzate il tipo di dati,
- sistemate gli elementi mancanti - verificate se ci sono correlazioni - create un grafico a mappa di calore
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

colonne = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

df = pd.read_csv("martedi-23-07/housing.csv", header=None,names= colonne,delimiter=r"\s+")
print("Dataframe importato: \n",df)


print("Tipi di dati: \n",df.dtypes)

print("Sistemare elementi mancanti: \n",df.isnull().sum())

correlazione = df.corr()

print("Verificare correlazioni : \n",correlazione)

plt.figure()

sns.heatmap(correlazione)

plt.title('Mappa di calore della matrice di correlazione')

plt.show()