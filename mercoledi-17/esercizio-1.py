# # Esercizio 1: Somma e Media di Elementi:
# # Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
# # Calcolare e stampare la somma di tutti gli elementi dell'array.
# # Calcolare e stampare la media di tutti gli elementi dell'array.

import numpy as np

# # Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
# arr = np.random.randint(1, 101, size=15)

# # calcolare la somma di tutti gli elementi dell'array
# somma = np.sum(arr)

# #calcoare e stampare media di tutti gli leemnti dell'array
# media = np.mean(arr)

# print(f"Array di numeri casuali", arr)
# print(f"Somma eleemnti array ", somma)
# print(f"media elementi arr", media)



#Esercizio 2: Manipolazione di Array Multidimensionali
# Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
# Estrarre e stampare la seconda colonna della matrice.
# Estrarre e stampare la terza riga della matrice.
# Calcolare e stampare la somma degli elementi della diagonale principale della matrice.

# Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
matrice = np.arange(1, 26).reshape(5, 5)

# Estrarre e stampare la seconda colonna della matrice.
seconda_col = matrice[:, 1]
print(f"Seconda colonna è", seconda_col)

# Estrarre e stampare la terza riga della matrice.
terza_riga = matrice[2, :]
print("Terza riga della matrice:", terza_riga)

# Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
somma_diagonale = np.trace(matrice)
print("Somma degli elementi della diagonale principale della matrice:", somma_diagonale)


# Esercizio 3: Operazioni con Fancy Indexing
# Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
# Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).
# Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0).
# Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.

# Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
arr = np.random.randint(10, 51, size=(4, 4))
print(f"Array 4 * 4 con num. casuali :", arr)

# Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).

indici = [(0, 1), (1, 2), (2, 2), (3, 0) ]
seleziona_ele = arr[[0, 1, 2, 3], [1, 3, 2, 0]]
print(f"eleemnti specifici :", seleziona_ele)

# Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0).
righe_disp =  arr[1::2, :]
print(f"tutte le righe dispari dell'array :", righe_disp)

# Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
arr[[0, 1, 2, 3], [1, 3, 2, 0]] +=10
print(f"Array dopo aver moficito gli elementi selezionati aggiungneodno 10:" , arr)

