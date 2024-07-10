# 1. Creazione e Manipolazione degli Array:
# - Crea un array di 10 elementi, tutti uguali a 5.
# - Cambia la forma dell'array creato in una matrice 2x5.
# - Crea un array di numeri casuali tra 0 e 1 di dimensione 4x4.
import numpy as np
# Crea un array di 10 elementi, tutti uguali a 5.
array_di_5 = np.full(10, 5)
# - Cambia la forma dell'array creato in una matrice 2x5.
array_di_5_con_reshape = array_di_5.reshape(2, 5)
# # - Crea un array di numeri casuali tra 0 e 1 di dimensione 4x4.
array_rand = np.random.rand(4,4)

print(f"array di 10 elementi tutti ugali a 5: ", array_di_5)
print(f"\narray cambaito  a matrice 2*5:",array_di_5_con_reshape)
print(f"\narradi di numeri casuali :",array_rand)


# 2. Operazioni sugli Array:
# - Crea due array di dimensione 3x3 e calcola il loro prodotto elemento per elemento.
# - Calcola la somma di tutti gli elementi di un array 3x3 creato con valori da 1 a 9.
# Crea due array di dimensione 3x3
array_1= np.array([[1, 2, 3], [4,5,6], [7,8,9]])
array_2 = np.array([[9,8,7],[6,5,4],[3, 2, 1] ])

# calcola il loro prodotto elemento per elemento
calcolo_prod = array_1 * array_2

# crea array 3*3
array3 = np.arange(1, 10 ).reshape(3, 3)
# somma elementi array
somma_array = np.sum(array3)

print(f"Array 1 =", array_1)
print(f"\nArray 2 =", array_2)
print(f"calocolo prodotto per ele", calcolo_prod)
print(f"Array 3 = ", array3)
print(f"La somma degli elementi arr =" , somma_array)

# 3. Utilizzo delle Funzioni:
# - Crea un array contenente 20 numeri equidistanti tra 0 e 10.
# - Utilizza `numpy.random` per generare un array di numeri interi casuali tra 1 e 100 di dimensione 5x5.
# Crea un array contenente 20 numeri equidistanti tra 0 e 10.

array_equidist = np.linspace(0, 10, 20)
# genera array di num int casuali tra 1 e 100 di dims. 5*5
array_random_interi = np.random.randint(1, 101, size = (5, 5))
print(f"Array che contiene 20 numeri equidist = ", array_equidist)
print(f"Array du numeri int, casuali tra 1 a 100  = ", array_random_interi)

# 4. Operazioni sugli Array:
# - Crea un array di numeri casuali di dimensione 5x5 e calcola la media dei valori di ciascuna colonna.
# - Crea un array di numeri casuali di dimensione 5x5 e calcola la somma dei valori di ciascuna riga.

# Crea un array di numeri casuali di dimensione 5x5
array_random_5x5 = np.random.rand(5, 5)

# calcolo media dei valori di cisacuna colonna
calcolo_media_colonne = np.mean(array_random_5x5, axis=0)

# crea un altro arraydi num casuli dim.5x5
array_random2_5x5 = np.random.rand(5, 5)
# calcola la somma dei valori di ciascuna riga.
calcolo_somma_riga = np.sum(array_random2_5x5, axis=1)

print(f"array di nu.casulai =", array_random_5x5)
print(f"\n meida dei valori di ciascuna colonna = ", calcolo_media_colonne)
print(f"\n array 2 =", array_random2_5x5)
print(f"\n somma dei valori di ciascuna riga = ", calcolo_somma_riga)

# 5. Manipolazione degli Array:
# - Crea un array 1D con 12 elementi e trasformalo in una matrice 3x4.
# - Estrai la prima colonna dalla matrice creata e sostituiscila con un array di zeri.

# crea un array 1d 
array_1d = np.arange(12)

# trasforamlo in una matrice 3x4
matrice_3x4 = array_1d.reshape(3, 4)

#Estrai la prima colonna dalla matrice creata
prima_colonna = matrice_3x4[:, 0]

# sostituiscila con un array di zeri.
matrice_3x4[:, 0] = 0

print(f"array 1d con 12 elem = ", array_1d)
print(f"\n matrice 3*4 = ", matrice_3x4)
print(f"\n pirma colonna = ", prima_colonna)
print(f"\n matrice 3*4 dopo la sostiuzione con gli zeri = ", matrice_3x4)

# 6. Utilizzo di Funzioni:
# - Utilizza numpy.random per generare un array di numeri interi casuali tra 50 e 100 di dimensione 3x3. Trova il massimo e il minimo valore di questo array.
# - Crea due array 1D di dimensione 5 con numeri casuali e trova il prodotto scalare tra i due.

randoms_arr = np.random.randint(50, 101, size =(3, 3))
print(f"array radnom = ", randoms_arr)

val_max = np.max(randoms_arr)
val_min = np.min(randoms_arr)
print(f"\n il valore massimo array = ", val_max)
print(f"\n il valore minimo dell array = ", val_min)

# Crea due array 1d di dimensione 5 con num.casulai 
array_rand_1 = np.random.rand(5)
array_rand_2 = np.random.rand(5)

print(f"\nprimo array 1d = ", array_rand_1)
print(f"\nSecodno array 1d = ", array_rand_2)

prodotto_scalare = np.dot(array_rand_1, array_rand_2)