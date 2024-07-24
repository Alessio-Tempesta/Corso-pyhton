# Creare un array unidimensionale con 50 valori compresi tra 1 e 1.000 e dopo dovete eseguire le seguenti operazioni:- calcolo della media;- calcolo della deviazione standard;- t
#trasformarlo in un array 5x10

import numpy as np


# Creare un array unidimensionale con 50 valori compresi tra 1 e 1.000
array = np.random.randint(1, 1001, size=50)

media = np.mean(array)    #calcolo della media
deviazione_std = np.std(array)     #caclocolo della deviazione standard
array_resahped = array.reshape(5, 10)    # Trasformazione in un array 5x10

print("Array originale:", array)
print("\nMedia:", media)
print("Deviazione standard:", deviazione_std)
print("\nArray 5x10:\n", array_resahped)