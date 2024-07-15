# Es1: ndarray, dtype, shape, arange
# Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.

# Esercizio:
# Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
# Verifica il tipo di dato dell'array e stampa il risultato.
# Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
# Stampa la forma dell'array.


import numpy as np

def crea_array():
    inizio = int(input("Inserisci il numero di partenza dell'array: "))
    fine = int(input("Inserisci il numero finale dell'array: "))
    arr = np.arange(inizio, fine)
    return arr

def cambia_tipo_dato(arr):
    arr_float = arr.astype(np.float64)
    return arr_float

def stampa_info(arr):
    print("\nTipo di dato dell'array:", arr.dtype)
    print("Forma (shape) dell'array:", arr.shape)

def menu():
    while True:
        print("\nMenu:")
        print("1. Crea un nuovo array")
        print("2. Cambia il tipo di dato dell'array a float64")
        print("3. Stampare tipo di dato e forma dell'array")
        print("4. Esci")

        scelta = input("\nSeleziona un'opzione (1/2/3/4): ")

        if scelta == '1':
            arr = crea_array()
            print("Array creato:", arr)

        elif scelta == '2':
            if 'arr' not in locals():
                print("Devi prima creare un array (opzione 1)!")
            else:
                arr = cambia_tipo_dato(arr)
                print("Array con tipo di dato cambiato a float64:", arr)

        elif scelta == '3':
            if 'arr' not in locals():
                print("Devi prima creare un array (opzione 1)!")
            else:
                stampa_info(arr)

        elif scelta == '4':
            print("Arrivederci!")
            break

        else:
            print("Scelta non valida. Riprova.")


menu()
