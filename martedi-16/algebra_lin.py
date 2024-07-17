# Esempi di Utilizzo

# Esempio 1: Inversa di una Matrice

import numpy as np

# Creazione di una matrice
# quadrata
A = np.array([[1, 2], [3, 4]])

# Calcolo dell'inversa della
# matrice
A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)


# Esempi di Utilizzo

# Esempio 2: Norma di un Vettore

# Creazione di un vettore
v = np.array([3, 4])

# Calcolo della norma del vettore
norm_v = np.linalg.norm(v)
print("Norma di v:", norm_v)  # Output: 5.0
