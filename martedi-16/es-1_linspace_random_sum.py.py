# Linspace, ranodm , sum

# Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape, genera un array casuale e calcola la somma degli elementi.

# Esercizio:
# Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
# Cambia la forma dell'array a una matrice 3x4.
# Genera una matrice 3x4 di numeri casuali tra 0 e 1.
# Calcola e stampa la somma degli elementi di entrambe le matrici.

import numpy as np

# # Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
# array_1 = np.linspace(0, 1, 12)

# # Cambia la forma dell'array a una matrice 3x4. 
# array_1_reshape = array_1.reshape(3, 4)

# #  Genera una matrice 3x4 di numeri casuali tra 0 e 1.
# array_2 = np.random.rand(3, 4)

# # Calcola e stampa la somma degli elementi di entrambe le matrici.
# somma_array_1 = np.sum(array_1_reshape)
# somma_array2 = np.sum(array_2)
# print("Somma degli elementi della prima matrice sono : ",somma_array_1)
# print("Somma elementi della seconda matrice sono: ", somma_array2)


def crea_array():
    array_equi = np.linspace(0, 1, 12)
    matrice_equi= array_equi.reshape(3, 4)
    print(f" Matrice di numeri equidistanti :", matrice_equi)
    
def genera_matrice_ranodm():
    matrice_rand = np.random.rand(3, 4 )
    print(f"Matrice casulare ", matrice_rand)