# Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 
# Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni sulla matrice. Le operazioni disponibili includono:
# Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
# Estrarre e stampare la sotto-matrice centrale.
# Trasporre la matrice e stamparla.
# Calcolare e stampare la somma di tutti gli elementi della matrice.
# Uscire dal programma.

# Parte DUE: Andare a specializzare per aggiungere nuove operazioni:
# Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una seconda matrice delle stesse dimensioni della prima e moltiplicarle elemento per elemento e stampare il risultato.
# Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di tutti gli elementi della matrice.

# EXTRA:
# Determinante della Matrice: Calcolare e stampare il determinante della matrice (solo se la matrice è quadrata).

import numpy as np 

#  Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
def crea_matrice(righe, colonne):
    return np.random.randint(1, 101, size=(righe, colonne))

# Estrarre e stampare la sotto-matrice centrale.
def stampa_sottomatice_centrale(matrice):
    righe, colonne = matrice.shape
    inizio_riga = riga // 4 
    fine_riga = inizio_riga + righe // 2
    inizo_colonna = colonne // 4
    fine_colonna = inizio_colonna + colonne // 2
    sotto_matrice = matrice[inizio_riga:fine_riga, inizo_colonna:fine_colonna]
    print("Sotto_matrice centrale:", sotto_matrice)
    
# # Calcolare e stampare la somma di tutti gli elementi della matrice.
def somma_ele(matrice):
    somma_tot = np.sum(matrice)
    print("La somma Di tutti gli elementi è :" , somma_tot)
    
# Trasporre la matrice e stamparla.
def trasponi_matrice(matrice):
    trasposta = np.transpose(matrice)
    print("Matrice trasposta:\n", trasposta)
    
# Funzione per moltiplicare la matrice per uno scalare e stampare il risultato.
def moltiplica_per_scalare(matrice, scalare):
    risultato = matrice * scalare
    print(f" Matrice moltiplicata per {scalare} :\n" , risultato)
    
    # Funzione per calcolare e stampare il determinante della matrice (solo se è quadrata).
def calcola_e_stampa_determinanate(matrice):
    # verifica se la matrice è quadrata
    if matrice.shape[0] == matrice.shape[1]:
        determinanate = np.linalg.det(matrice)
        print(f"Determinante della matrice:", determinanate)
    else:
        print("LA matrice non è quadrata, impossibile ")