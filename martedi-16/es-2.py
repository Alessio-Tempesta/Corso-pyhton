# Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
# Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
# Somma i due array elemento per elemento per ottenere un nuovo array.
# Calcola la somma totale degli elementi del nuovo array.
# Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
# Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.

# Obiettivo:

# Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random per creare array di numeri casuali, e sum per eseguire operazioni di somma sugli array, incluso l'uso di condizioni per la somma parziale.

import numpy as np

# funzione con il linspace 
def array_linspace():
    try:
        # Creazione di un array di 50 numeri equidistanti tra 0 e 10
        return np.linspace(0, 10, 50)
    except Exception as e:
        print(f"Errore nella generazione dell'array con linspace: {e}")
        return None
    
# funzione di array random
def array_random():
    try:
        # Creazione di un array di 50 numeri casuali tra 0 e 1
        return np.random.random(50)
    except Exception as e:
        print(f"Errore nella generazione dell'array con random: {e}")
        return None

def somma(array1, array2):
    try:
        # Somma elemento per elemento dei due array
        return array1 + array2
    except Exception as e:
        print(f"Errore nella somma degli array: {e}")
        return None

def calcola_totale(array):
    try:
        # Calcolo della somma totale degli elementi dell'array
        return np.sum(array)
    except Exception as e:
        print(f"Errore nel calcolo della somma totale: {e}")
        return None

def calcola_somma_magg_di_5(array):
    try:
        # Calcolo della somma degli elementi dell'array che sono maggiori di 5
        return np.sum(array[array > 5])
    except Exception as e:
        print(f"Errore nel calcolo della somma degli elementi maggiori di 5: {e}")
        return None

def menu():
    print("\nMenu:")
    print("1. Genera array con linspace")
    print("2. Genera array con random")
    print("3. Somma due array")
    print("4. Calcola la somma totale degli elementi del nuovo array")
    print("5. Calcola la somma degli elementi maggiori di 5 nel nuovo array")
    print("6. Esci")

def main():
    while True:
        try:
            menu()  # Mostra il menu delle opzioni disponibili
            scelta = input("\nSeleziona un'opzione: ")

            if scelta == '1':
                # Opzione 1: Genera un array con linspace
                array_linspaces = array_linspace()
                if array_linspaces is not None:
                    print("Array generato con linspace:\n", array_linspaces)

            elif scelta == '2':
                # Opzione 2: Genera un array con numeri casuali
                array_randoms = array_random()
                if array_randoms is not None:
                    print("Array generato con random:\n", array_randoms)

            elif scelta == '3':
                # Opzione 3: Somma due array generati
                array_linspaces = array_linspace()
                array_randoms = array_random()
                if array_linspaces is not None and array_randoms is not None:
                    somma_array = somma(array_linspaces, array_randoms)
                    if somma_array is not None:
                        print("Array risultante dalla somma:\n", somma_array)

            elif scelta == '4':
                # Opzione 4: Calcola la somma totale degli elementi del nuovo array
                array_linspaces = array_linspace()
                array_randoms = array_random()
                if array_linspaces is not None and array_randoms is not None:
                    somma_array = somma(array_linspaces, array_randoms)
                    if somma_array is not None:
                        total_sum = calcola_totale(somma_array)
                        print("Somma totale degli elementi del nuovo array:", total_sum)

            elif scelta == '5':
                # Opzione 5: Calcola la somma degli elementi maggiori di 5 nel nuovo array
                array_linspaces = array_linspace()
                array_randoms = array_random()
                if array_linspaces is not None and array_randoms is not None:
                    somma_array = somma(array_linspaces, array_randoms)
                    if somma_array is not None:
                        sum_greater_than_5 = calcola_somma_magg_di_5(somma_array)
                        print("Somma degli elementi maggiori di 5 nel nuovo array:", sum_greater_than_5)

            elif scelta == '6':
                # Opzione 6: Uscita dal programma
                print("Uscita dal programma.")
                break

            else:
                # Opzione non valida
                print("Scelta non valida. Riprova.")

        except Exception as e:
            print(f"Errore durante l'esecuzione del programma: {e}")

# Avvio del programma chiamando la funzione main()
main()

