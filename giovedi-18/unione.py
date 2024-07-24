# Esempio Pratico finale: Unione e Risistemazione

# Supponiamo di avere due dataset: uno con le vendite
# giornaliere di prodotti in varie città e l'altro con le
# informazioni sul costo dei prodotti. Utilizzeremo pandas
# per unire questi dataset e creare una tabella pivot per
# analizzare le vendite totali per prodotto e città.

# Dataset di esempio:
# Vendite: Prodotto, Quantità, Città, Data
# Costi: Prodotto, Costo per unità
# Operazioni:
# Unire i due dataset su "Prodotto".
# Creare una tabella pivot con le vendite totali per
# prodotto per città.

import pandas as pd

# creazione dataset vendite e costi
data_vendite = {
    'Prodotto': ['Prod_A', 'Prod_B', 'Prod_A', 'Prod_B', 'Prod_A'],
    'Quantità': [10, 20, 15, 25, 18],
    'Città': ['Roma', 'Milano', 'Roma', 'Milano', 'Napoli'],
    'Data': ['2024-07-01', '2024-07-01', '2024-07-02', '2024-07-02', '2024-07-03']
}

data_costi = {
    'Prodotto': ['Prod_A', 'Prod_B'],
    'Costo per unità': [100, 120]
}

# Creiamo i dataframe da questi dati
df_vendite = pd.DataFrame(data_vendite)
df_costi = pd.DataFrame(data_costi)

# unione dei due dataframe su Prodotto
df_merge = pd.merge(df_vendite, df_costi, on='Prodotto', how='left')

# creazione tablla pivot
pivot_table= pd.pivot_table(df_merge, values='Quantità', index='Prodotto', columns='Città', aggfunc='sum', fill_value=0)

print("Tabella Pivot delle venidte tot per prodotto e città \n", pivot_table)