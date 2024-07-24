
# # Grafico a Barre
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Creare un grafico a barre
# plt.figure(figsize=(10, 6), facecolor='#f2e6ff') 


# # Dati di esempio
# tips = sns.load_dataset("tips")

# # Creare un grafico a barre
# sns.barplot(x="day", y="total_bill", data=tips)
# plt.title('Conto Totale per Giorno')
# plt.show()




# Grafico a Linee

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Dati di esempio
# fmri = sns.load_dataset("fmri")

# # Creare un grafico a linee
# sns.lineplot(x="timepoint", y="signal", data=fmri, hue="region", style="event")
# plt.title('Segnale FMRI nel Tempo')
# plt.show()


# # Istogramma e KDE:
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Generare dati casuali
# data = sns.load_dataset("penguins")

# # Creare un istogramma con KDE
# sns.histplot(data=data, x="flipper_length_mm", kde=True)
# plt.title('Distribuzione Lunghezza Pinne dei Pinguini')
# plt.show()




# Esercizio Medio: Normalizzazione dei Dati:
# Testo dell'esercizio:

# Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo
# di persone, normalizza i dati di altezza e peso usando la normalizzazione min-
# max (ridimensiona i valori in modo che varino tra 0 e 1). 

# Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
# originale e quello modificato.

# Fornisci un codice che:
# Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
# DataFrame chiamato df).
# Applichi la normalizzazione min-max alle colonne altezza e peso.
# Stampa sia il DataFrame originale sia quello modificato per compararli.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Creo DataFrame con dati
data = {
    'altezza': [160, 175, 180, 170, 165],
    'peso': [55, 75, 80, 70, 65],
    'età': [25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)

# Creazione di una copia del DataFrame per non modificare l'originale
df_normalizzato = df.copy()

# Normalizzazione Min-Max
df_normalizzato['altezza'] = (df['altezza'] - df['altezza'].min()) / (df['altezza'].max() - df['altezza'].min())
df_normalizzato['peso'] = (df['peso'] - df['peso'].min()) / (df['peso'].max() - df['peso'].min())

# Aggiungere una colonna per identificare se i dati sono originali o normalizzati
df_melted = pd.melt(df, id_vars=['età'], value_vars=['altezza', 'peso'], var_name='Variabile', value_name='Valore')
df_normalizzato_melted = pd.melt(df_normalizzato, id_vars=['età'], value_vars=['altezza', 'peso'], var_name='Variabile', value_name='Valore')
df_melted['Tipo'] = 'Originale'
df_normalizzato_melted['Tipo'] = 'Normalizzato'

# Unire i DataFrame per facilitare la visualizzazione
df_combined = pd.concat([df_melted, df_normalizzato_melted])

#