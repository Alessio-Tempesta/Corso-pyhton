# Partendo dal dataset a questo link https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction , utilizzate i dati sugli anni delle case e la distanza dalla stazione metro per prevedere quanto queste caratteristiche influiscono sul costo delle case.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def carica_file():
    # Carica il file CSV
    df = pd.read_csv('Machine-Learning/Real estate.csv') 
    print(df.head())
    return df

def prepara_dati(df):
    # Seleziona le colonne per le feature e il target
    X = df[['X2 house age', 'X3 distance to the nearest MRT station']]
    y = df['Y house price of unit area'] 
    return X, y

def suddividi_dati(X, y):
    # Suddivide i dati in training e test set
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test

def crea_modello(X_train, y_train):
    # Crea e addestra il modello di regressione lineare
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def valuta_modello(model, X_test, y_test):
    # Valuta il modello e calcola le previsioni
    y_pred = model.predict(X_test)
    err_quad = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Errore Quadratico Medio: {err_quad}")
    print(r2)
    return y_pred

def visualizza(df, X_test, y_pred):
    plt.figure(figsize=(14, 6))

    # Grafico dell'età della casa vs prezzo
    plt.subplot(1, 2, 1)
    plt.scatter(df['X2 house age'], df['Y house price of unit area'], color='blue', label='Dati Originali')
    plt.scatter(X_test['X2 house age'], y_pred, color='red', label='Previsioni')
    plt.xlabel('Età della Casa')
    plt.ylabel('Prezzo per Unità')
    plt.title('Età della Casa vs Prezzo per Unità')
    plt.legend()

    # Grafico distanza dalla metro vs prezzo
    plt.subplot(1, 2, 2)
    plt.scatter(df['X3 distance to the nearest MRT station'], df['Y house price of unit area'], color='blue', label='Dati Originali')
    plt.scatter(X_test['X3 distance to the nearest MRT station'], y_pred, color='red', label='Previsioni')
    plt.xlabel('Distanza dalla Metro')
    plt.ylabel('Prezzo per Unità')
    plt.title('Distanza dalla Metro vs Prezzo per Unità')
    plt.legend()

    plt.show()

# Esecuzione del flusso
df = carica_file()
X, y = prepara_dati(df)
X_train, X_test, y_train, y_test = suddividi_dati(X, y)
model = crea_modello(X_train, y_train)
y_pred = valuta_modello(model, X_test, y_test)
visualizza(df, X_test, y_pred)