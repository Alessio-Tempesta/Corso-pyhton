import numpy as np
# Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.

# 1- Genraimo un array numpy1d di 20 num.int casuali 
arr = np.random.randint(10, 51, 20)
print(f"array originale",arr)

# 2- Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
# estrai i primi 10 ele dell'array

primi_10 = arr[:10]
print(f"\n i primi 10 elementi sono :", primi_10)

#3- Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
ultimi_5 = arr[-5:]
print(f"\n utlimi 5 elementi sono:", ultimi_5)

# Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).

indice_5_a_14 = arr[5:15]
print(f"\nelementi dall'indicie 5 al 14 : ", indice_5_a_14)

# Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
terzo_ele = arr[::3]
print(f"\n ongi terzo elemento: ", terzo_ele)

# Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
arr[5:10] = 99 
print(f"array con modifica",arr)

