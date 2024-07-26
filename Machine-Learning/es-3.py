# Partendo dal dataset a questo link https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression ,
# utilizzate i dati sulle ore di studio e le ore di sonno per prevedere quanto queste caratteristiche influiscono sull'indice di prestazione degli studenti.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def carica_file():
    df = pd.read_csv('Machine-Learning/Student_Performance.csv')
    print(df.head())
    return df

def prepara_dati(df):
    X = df[['Hours Studied', 'Sleep Hours']]
    y = df[['Performance Index']]
    return X,y

def suddividi_dati(X, y ):
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    return X_train, X_test, y_train, y_test,

def crea_modello(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model 

def valuta_modello(model, X_test, y_test):
    y_pred = model.predict(X_test)
    err_quad= mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(err_quad)
    print(r2)
    return y_pred

def visualizza(df, X_test, y_pred):
    plt.figure(figsize=(14, 6))

    # Grafico delle ore di studio vs indice di prestazione
    plt.subplot(1, 2, 1)
    plt.scatter(df['Hours Studied'], df['Performance Index'], color='blue', label='Dati Originali')
    plt.scatter(X_test['Hours Studied'], y_pred, color='red', label='Previsioni')
    plt.xlabel('Ore di Studio')
    plt.ylabel('Indice di Prestazione')
    plt.title('Ore di Studio vs Indice di Prestazione')
    plt.legend()

    # Grafico ore di sonno vs indice di prestazione
    plt.subplot(1, 2, 2)
    plt.scatter(df['Sleep Hours'], df['Performance Index'], color='blue', label='Dati Originali')
    plt.scatter(X_test['Sleep Hours'], y_pred, color='red', label='Previsioni')
    plt.xlabel('Ore di Sonno')
    plt.ylabel('Indice di Prestazione')
    plt.title('Ore di Sonno vs Indice di Prestazione')
    plt.legend()

    plt.show()
    
df = carica_file()
X, y = prepara_dati(df)
X_train, X_test, y_train, y_test = suddividi_dati(X, y)
model = crea_modello(X_train, y_train)
y_pred = valuta_modello(model, X_test, y_test)
visualizza(df, X_test, y_pred)