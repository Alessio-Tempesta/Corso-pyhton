# Consegna:

# Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
# Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
# Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
# Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
# Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
# Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.

# Obiettivo:

# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi.


import numpy as np 

#1- Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
matrice = np.random.randint(1, 101, size=(6, 6))
print("Matrice origniale: ", matrice)

#2- Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
sotto_matrice = matrice[1:5, 1:5]
print("\n la sotto matrice centrale 4x4: ", sotto_matrice)

#3- Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
inverti_sotto_matrice = np.flipud(sotto_matrice)
print("\ninversione sotto matrice", inverti_sotto_matrice)

#4- Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
diagonale = np.diag(inverti_sotto_matrice)
print("\n Diagonale delle matrice invertita", diagonale)

#5- Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
sotto_mat_inv_multipli_di_3 = np.where(inverti_sotto_matrice % 3 == 0, -1, inverti_sotto_matrice)
print("\n La sottomatrice con i multipli di di 3 ", inverti_sotto_matrice)



print("\nMatrice originale:\n", matrice)
print("\nSotto-matrice centrale estratta:\n", sotto_matrice)
print("\nMatrice invertita:\n", inverti_sotto_matrice)
print("\nDiagonale principale della matrice invertita:\n", diagonale)