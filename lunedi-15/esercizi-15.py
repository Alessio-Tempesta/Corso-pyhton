# Es1: ndarray, dtype, shape, arange
# Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.

# Esercizio:
# Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
# Verifica il tipo di dato dell'array e stampa il risultato.
# Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
# Stampa la forma dell'array.



import numpy as np

#np.arange per creare un array di num.int  
arr = np.arange(10, 50)

# verificare il tipo di dato con Dtype
print("tipo di dato array : ")
print(arr.dtype)

# cambia tipo di dato dell'array
arr = arr.astype(np.float64)

# verifcia nuovo tipo di dato
print("\ntipo di dato dopo la converisone :")
print(arr.dtype)


# stampa della forma shape dell'array
print("\n la froma (shape) dell'array:")
print(arr.shape)