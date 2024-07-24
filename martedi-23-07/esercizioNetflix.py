# Partendo da questo dataframe su kaggle https://www.kaggle.com/datasets/shivamb/netflix-shows analizzate i dati, 
# sistemate gli elementi mancanti e verificate se ci sono correlazioni e create un grafico a mappa di calore.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importare i dati
df = pd.read_csv("martedi-23-07/netflix_titles (1).csv")

# Visualizzare il dataframe importato e i tipi di dati
print("Dataframe importato: \n",df)

print("Tipi di dati: \n",df.dtypes)

# Riempire i valori mancanti nella colonna 'duration' con '0 min'
df['duration'].fillna('0 min')
 
df['duration'] = df['duration'].str.extract('(\d+)').astype(float)

# Dividere il dataset in film e show televisivi
filtro_film = df[df['type'] == 'Movie']
filtro_show = df[df['type'] == 'TV Show']

# Calcolare le correlazioni
correlazione_film = filtro_film[['duration', 'release_year']].corr()
correlazione_show = filtro_show[['duration', 'release_year']].corr()

print(filtro_film)
print(filtro_show)

# Stampare le correlazioni
print("Correlazione show: \n",correlazione_show)
print("Correlazione film : \n",correlazione_film)

#  Creare la mappa di calore
plt.figure()

sns.heatmap(correlazione_film,annot=True,cmap='Reds', linewidths=.5)

plt.title('Film : Durata/Anno di uscita')

plt.show()

plt.figure()

sns.heatmap(correlazione_show,annot=True, cmap='Blues', linewidths=.5)

plt.title('TV Show : Durata/Anno di uscita', fontsize=16)

plt.show()