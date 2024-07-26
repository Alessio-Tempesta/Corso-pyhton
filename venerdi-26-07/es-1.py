# ## Esercizio 1
# Partendo dal dataset al seguente link https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv relativo a campagne di marketing diretto (telefonate) di un istituto bancario portoghese, create il modello più preciso possibile per prevedere se il cliente sottoscriverà (1/0) un deposito a termine(variabile y).

# Nel dataset abbiamo le seguenti colonne:

# #### Variabili di input

# - età (numerico)
# - lavoro: tipologia di lavoro (categoriale: “amministratore”, “operaio”, “imprenditore”, “cameriera”, “dirigente”, “pensionato”, “lavoratore autonomo”, “servizi”, “studente”, “tecnico” ”, “disoccupato”, “sconosciuto”)
# - coniugale: stato civile (categorico: “divorziato”, “sposato”, “celibe”, “sconosciuto”)
# - istruzione (categoriale: “basic.4a”, “basic.6a”, “basic.9a”, “scuola superiore”, “analfabeta”, “corso.professionale”, “laurea.universitaria”, “sconosciuto”)
# - default: ha credito in default? (categorico: “no”, “sì”, “sconosciuto”)
# - alloggio: ha mutuo per la casa? (categorico: “no”, “sì”, “sconosciuto”)
# - prestito: ha prestito personale? (categorico: “no”, “sì”, “sconosciuto”)
# - contatto: tipo di comunicazione del contatto (categoriale: “cellulare”, “telefonico”)
# - mese: mese dell'anno dell'ultimo contatto (categoriale: “gen”, “feb”, “mar”, …, “nov”, “dic”)
# - day_of_week: ultimo giorno di contatto della settimana (categorico: “mon”, “mar”, “mer”, “gio”, “ven”)
# - durata: durata dell'ultimo contatto, in secondi (numerico). Nota importante: questo attributo influisce notevolmente sulla destinazione dell'output (ad esempio, se durata=0 allora y='no'). La durata non è nota prima che venga effettuata una chiamata, inoltre, dopo la fine della chiamata, è ovviamente nota y. Pertanto, questo input dovrebbe essere incluso solo a fini di benchmark e dovrebbe essere scartato se l’intenzione è quella di avere un modello predittivo realistico
# - campagna: numero di contatti eseguiti durante questa campagna e per questo cliente (numerico, include l'ultimo contatto)
# - pdays: numero di giorni trascorsi dall'ultimo contatto del cliente da una campagna precedente (numerico; 999 significa che il cliente non è stato contattato in precedenza)
# - precedente: numero di contatti effettuati prima di questa campagna e per questo cliente (numerico)
# - poutcome: esito della precedente campagna di marketing (categoriale: “fallimento”, “inesistente”, “successo”)
# - emp.var.rate: tasso di variazione dell'occupazione — (numerico)
# - cons.price.idx: indice dei prezzi al consumo — (numerico)
# - cons.conf.idx: indice di fiducia dei consumatori — (numerico)
# - euribor3m: tasso euribor a 3 mesi — (numerico)
# - nr.occupati: numero di dipendenti — (numerico)

# ### Variabile output (obiettivo desiderato):

# - y — il cliente ha sottoscritto un deposito a termine? (binario: “1”, significa “Sì”, “0” significa “No”)


## Valutate se utilizzare tutti i paramentri o solo alcuni di essi:

## - Create il modello e addestratelo;
## - Valutate il modello;
## - Create la matrice di confusione;
## - Create un report di classificazione
## - Create i grafici


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn import linear_model
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import PredictionErrorDisplay



def grafico1():
    sito="https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"

    dati=pd.read_csv(sito)
    diz_dati={"blue-collar": 9,
            "technician": 5,
            "management": 10,
            "services": 7,
            "retired":4,
            "housemaid": 3,
            "admin.": 8,
            "unemployed":1,
            "entrepreneur": 11,
            "self-employed": 6,
            "student":2,
            "unknown": 0}

    diz_dati2={"yes": 2,
            "no": 1}
    diz_dati3={"yes": 2,
            "no": 1}
    dati["job"]= dati["job"].map(diz_dati)

    dati["housing"]= dati["housing"].map(diz_dati2)
    dati["loan"]=dati["loan"].map(diz_dati3)
    dati = dati.dropna(subset=["housing"])
    dati = dati.dropna(subset=["loan"])

    X=dati[["age","job","cons_conf_idx","cons_price_idx","housing","campaign","loan","duration"]]
    y=dati["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modello=linear_model.LogisticRegression(max_iter=1000).fit(X_train,y_train)


    y_pred=modello.predict(X_train)

    y_test_pred = modello.predict(X_test)




    train_accuracy = accuracy_score(y_train, y_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    matrice=confusion_matrix(y_test, y_test_pred)
    #print(train_accuracy,test_accuracy,matrice)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sì'], yticklabels=['No', 'Sì'])
    plt.xlabel('Predizione')
    plt.ylabel('Reale')
    plt.title('Matrice di Confusione')
    plt.show()

def grafico2():
    sito="https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"

    dati=pd.read_csv(sito)
    diz_dati={"blue-collar": 9,
            "technician": 5,
            "management": 10,
            "services": 7,
            "retired":4,
            "housemaid": 3,
            "admin.": 8,
            "unemployed":1,
            "entrepreneur": 11,
            "self-employed": 6,
            "student":2,
            "unknown": 0}

    diz_dati2={"yes": 2,
            "no": 1}
    
    dati["job"]= dati["job"].map(diz_dati)

    dati["housing"]= dati["housing"].map(diz_dati2)
    
    dati = dati.dropna(subset=["housing"])
    

    X=dati[["age","job","cons_conf_idx","cons_price_idx","housing"]]
    y=dati["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modello=linear_model.LogisticRegression(max_iter=1000).fit(X_train,y_train)


    y_pred=modello.predict(X_train)

    y_test_pred = modello.predict(X_test)




    train_accuracy = accuracy_score(y_train, y_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    matrice=confusion_matrix(y_test, y_test_pred)
    #print(train_accuracy,test_accuracy,matrice)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sì'], yticklabels=['No', 'Sì'])
    plt.xlabel('Predizione')
    plt.ylabel('Reale')
    plt.title('Matrice di Confusione')
    plt.show()

def grafico3():

    sito="https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"

    dati=pd.read_csv(sito)
    diz_dati={"blue-collar": 9,
            "technician": 5,
            "management": 10,
            "services": 7,
            "retired":4,
            "housemaid": 3,
            "admin.": 8,
            "unemployed":1,
            "entrepreneur": 11,
            "self-employed": 6,
            "student":2,
            "unknown": 0}

    diz_dati2={"yes": 2,
            "no": 1}
    diz_dati3={"yes": 2,
            "no": 1}
    dati["job"]= dati["job"].map(diz_dati)



    X=dati[["age","job","cons_conf_idx","cons_price_idx"]]
    y=dati["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modello=linear_model.LogisticRegression(max_iter=1000).fit(X_train,y_train)


    y_pred=modello.predict(X_train)

    y_test_pred = modello.predict(X_test)




    train_accuracy = accuracy_score(y_train, y_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    matrice=confusion_matrix(y_test, y_test_pred)
    #print(train_accuracy,test_accuracy,matrice)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sì'], yticklabels=['No', 'Sì'])
    plt.xlabel('Predizione')
    plt.ylabel('Reale')
    plt.title('Matrice di Confusione')
    plt.show()

def grafico4():
    sito="https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv"

    dati=pd.read_csv(sito)
    diz_dati={"blue-collar": 9,
            "technician": 5,
            "management": 10,
            "services": 7,
            "retired":4,
            "housemaid": 3,
            "admin.": 8,
            "unemployed":1,
            "entrepreneur": 11,
            "self-employed": 6,
            "student":2,
            "unknown": 0}

    diz_dati2={"basic.4y": 1,
               "unknown": 0,
               "university.degree": 5,
               "high.school": 4,
               "basic.9y":3,
               "basic.6y": 2,
               "professional.course": 0}


    dati["job"]= dati["job"].map(diz_dati)



    X=dati[["age","job","cons_conf_idx","cons_price_idx"]]
    y=dati["y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modello=linear_model.LogisticRegression(max_iter=1000).fit(X_train,y_train)


    y_pred=modello.predict(X_train)

    y_test_pred = modello.predict(X_test)




    train_accuracy = accuracy_score(y_train, y_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    matrice=confusion_matrix(y_test, y_test_pred)
    #print(train_accuracy,test_accuracy,matrice)
    plt.figure(figsize=(8, 6))
    sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sì'], yticklabels=['No', 'Sì'])
    plt.xlabel('Predizione')
    plt.ylabel('Reale')
    plt.title('Matrice di Confusione')
    plt.show()

grafico1()
grafico2()
grafico3()


#print(dati)
