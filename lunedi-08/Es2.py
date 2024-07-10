# Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape, genera un array casuale e calcola la somma degli elementi.
# Esercizio:
# Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
# Cambia la forma dell'array a una matrice 3x4.
# Genera una matrice 3x4 di numeri casuali tra 0 e 1.
# Calcola e stampa la somma degli elementi di entrambe le matrici.
# Es2:reshape, linspace, random, sum

import numpy as np
#creare un array di 12 numeri equidtsnatu tra lo 0 e 1 
array_linspace = np.linspace(0, 1, 12)

# cambia froma array ad una matrice 3*4
array_reshape = array_linspace.reshape(3, 4)

# genera una matrice 3*4 di numeir casuali tra 0 e 1 
array_random = np.random.rand(3, 4)

# Calcola e stampa la somma degli elementi di entrambe le matrici
somma_linspace = np.sum(array_reshape)
somma_random = np.sum(array_random)

print(f"Somma degli elementi della matrice linspace: {somma_linspace}")
print(f"Somma degli elementi della matrice random : {somma_random}")