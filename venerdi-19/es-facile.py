# Esercizio Facile: Calcolo di Statistiche di Base

# Testo dell'esercizio:

# Hai a disposizione un dataset, che devi autogenerare,
# contenuto in un DataFrame pandas con una singola colonna
# temperature che rappresenta la temperatura giornaliera in
# una città per un mese. 

# Scrivi un programma Python che calcoli e stampi le seguenti
# statistiche:
# La temperatura massima
# La temperatura minima
# La temperatura media
# La mediana delle temperature

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Genera un dataframe con colonna temperature per un mese
num_giorni = 30

# Generiamo delle temperature casuali tra i 15 ed i 25 gradi
temperature = np.random.uniform(low=15, high=25, size=num_giorni)
df = pd.DataFrame(temperature, columns=['temperature'])

# Calcolo delle statistiche
temp_max = df['temperature'].max()
temp_min = df['temperature'].min()
media_temp = df['temperature'].mean()
mediana_temp = df['temperature'].median()

# Stampa delle statistiche
print(f'Temperatura massima: {temp_max:.2f} gradi')
print(f'Temperatura minima: {temp_min:.2f} gradi')
print(f'Temperatura media: {media_temp:.2f} gradi')
print(f'Mediana delle temperature: {mediana_temp:.2f} gradi')

# Visualizzazione con Matplotlib
plt.figure(figsize=(10, 6), facecolor='#f2e6ff')

# Grafico a linee delle temperature
plt.plot(df.index, df['temperature'], color='red')

# Titoli e etichette
plt.title('Temperature Giornaliera', fontsize=24)
plt.xlabel('Giorno del Mese', fontsize=18)
plt.ylabel('Temperatura (°C)', fontsize=18)

# Aggiungere una griglia
# plt.grid(True, linestyle='--', alpha=0.5)

# Mostra grafico
plt.show()
