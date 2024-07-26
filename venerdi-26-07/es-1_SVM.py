## Esercizio 1

# L'obiettivo di questo esercizio è identificare il kernel migliore dell'algoritmo SVM per classificare il tipo di fiore "setosa" e "virginica" del dataset iris.
# Di seguito la base per importare il dataset e le classi specifiche from sklearn import datasets

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# Caricamento del dataset Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Filtraggio delle classi "setosa" (0) e "virginica" (2) e delle prime due caratteristiche
X = X[y != 1, :2]
y = y[y != 1]

# Divisione del dataset in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Visualizzazione del dataset
_, ax = plt.subplots()
scatter = ax.scatter(X[:, 0], X[:, 1], c=y)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
_ = ax.legend(scatter.legend_elements()[0], ['setosa', 'virginica'], loc="lower right", title="Classes")
plt.show()

# Creazione del modello SVC
model = SVC()

# Definizione dei parametri per il GridSearch
param_grid = {'C': [1, 5, 10, 50], 'gamma': [0.0001, 0.0005, 0.001, 0.005]}

# Esecuzione del GridSearch
grid = GridSearchCV(model, param_grid, n_jobs=-1)
grid.fit(X_train, y_train)

# Migliori parametri trovati dal GridSearch
print(f"Best parameters: {grid.best_params_}")

# Predizione e valutazione sul set di test
y_pred = grid.best_estimator_.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))
