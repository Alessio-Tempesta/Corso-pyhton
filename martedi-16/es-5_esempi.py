import numpy as np
# La funzione linspace genera un array di numeri equidistanti tra un valore iniziale e uno finale.
# Esempio:

arr = np.linspace(0, 1, 5)
print(arr)  # Output: [0.   0.25 0.5  0.75 1.  ]

# Il modulo random di NumPy permette di generare array di numeri casuali.
# Esempio:
random_arr = np.random.rand(3, 3)  
# Matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)



# Sum , mean, std:
# NumPy fornisce diverse funzioni per eseguire operazioni matematiche sugli array.
# Esempio:

arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("Sum:", sum_value)    # Output: Sum: 15
print("Mean:", mean_value)  # Output: Mean: 3.0
print("Standard Deviation:", std_value)  
# Output: Standard Deviation: 1.4142135623730951