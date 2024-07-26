# Utilizzate la linear regression per analizzare il dataframe di esempio con Fabbisogno calorico giornaliero di un uomo in base alla sua età, allenate l'algoritmo, testatelo e poi realizzate un grafico.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('Machine-Learning/fabbisogno calorico.csv')
print(df)

X = df[['età']]
y = df[['calories']]   
# Suddividi i dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y)

# modello di regressione lineare
model = LinearRegression()

model.fit(X_train, y_train)     # Allena il modello
# usiamo il predict per fare previsioni sui dati
y_pred = model.predict(X_test)


calc_medio = mean_squared_error(y_test, y_pred)
print(calc_medio)
r2= r2_score(y_test, y_pred)
print(r2)

plt.scatter(df['età'], df['calories'], color='blue', label='Dati Originali')
# Usa il modello per predire i valori per la visualizzazione della retta
x_range = np.linspace(df['età'].min(), df['età'].max(), 100).reshape(-1, 1)
y_range = model.predict(x_range)

plt.plot(x_range, y_range, color='red', linewidth=2, label='Retta di Regressione')
plt.xlabel('Età (anni)')
plt.ylabel('Fabbisogno Calorico (calorie)')
plt.title('Regressione Lineare: Età vs Fabbisogno Calorico')
plt.legend()
plt.show()