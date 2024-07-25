# Utilizzate la linear regression per analizzare il dataframe di esempio in cui abbiamo le Calorie bruciate in base al peso della persona che fa esercizio fisico con la montain bike, allenate l'algoritmo, testatelo e poi realizzate un grafico


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('Machine-Learning/calories.csv')
print(df)

# Variabili
X = df[['kg']]
y= df[['calories']]

# modello di regressione lineare
model = LinearRegression()


X_train, X_test, y_train, y_test = train_test_split(X, y)

# alleniamo il modello
model.fit(X_train, y_train)

# facciamo delle previsoni dei dati
y_pred = model.predict(X_test)

errore_quadratico = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"L'errore quadratico", errore_quadratico)
print(f"la previsone perfetta",r2)

# Visualizza i dati originali e la retta di regressione
plt.scatter(X, y, color='blue', label='Dati Originali')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Retta di Regressione')
plt.xlabel('kg')
plt.ylabel('Calorie Bruciate')
plt.title('Regressione Lineare: Peso vs Calorie Bruciate')
plt.legend()
plt.show()