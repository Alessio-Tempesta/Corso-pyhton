# def saluta(nome):
#     print("Ciao,", nome)  # Stampa il saluto con il nome specificato

# saluta("Alessio")
# saluta("MIRKO")
# saluta("MIRKO")


# ESERCIZO BASE: Indovina il numero descrizone. scrvi un programma che genera un numero casuale tra 1 e 100( inclusi ) l'utente deve indovinare quale numero è stato generato. Dopo ogni tentavo, il programma dovrebbe dire all'utente se il numero da indovinare è più alto o piu basso rispetto al numero insierito. il gioco termina quando l'utemte indpvina il numero o decide di uscire.

# import random 

# def gioco_indovina_numero():
#     numero_da_indovinare = random.randint(1, 100)
#     tentativi = 0

#     print("benvenuto al gioco indovina il numero!")
#     print("puoi uscire dal gioco in qualsiasi moemnto digitando 'exit'.")

 
#     while True:
#         tentativo = input("Indovina il numero (1-100): ")

#         if tentativo.lower() == 'exit':
#             print(f"Peccato che tu stia uscendo! Il numero da indovinare era {numero_da_indovinare}.")
#             break 

#         if not tentativo.isdigit():
#             print("Inserisci un numero valido.")
#             continue

#         tentativo = int(tentativo)
#         tentativi += 1

#         if tentativo == numero_da_indovinare:
#             print(f"Complimenti! Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi!")
#             break  
#         elif tentativo < numero_da_indovinare:
#             print("Il numero da indovinare è più alto.")
#         else:
#             print("Il numero da indovinare è più basso.")

# # Esegui il gioco
# gioco_indovina_numero()


# def fibonacci(n):
#     # Inizializzazione dei primi due numeri della sequenza
#     fib_sequence = [0, 1]
    
#     # Calcolo della sequenza fino all'n-esimo numero
#     while len(fib_sequence) < n:
#         next_num = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_num)
    
#     return fib_sequence[:n]

# # Esempio di utilizzo
# n = 10  # Numero di elementi della sequenza di Fibonacci da generare
# fib_sequence = fibonacci(n)
# print(f"Sequenza di Fibonacci con {n} elementi:", fib_sequence)

# esercizio 1 (Facile): Scrivi una funzione chiamata area_triangolo che prenda in input la base e l'altezza di un triangolo e restituisca la sua area. fare la stessa cosa con quadrato e rettagolo e rendere ripetibile salvando in una lista tutti i risultati

# funzione per trovare area triangolo
# def area_triangolo(base, altezza):
#     area = 0.5 * base * altezza
#     return area

# # funzione per trovare area quadrato
# def area_quadrato(lato):
#     area = lato * lato
#     return area

# # funzione per trovare area rettangolo
# def area_rettangolo(base, altezza):
#     area = base * altezza
#     return area

# def calcola_aree():
    
#     aree = []

#  # Input per il triangolo
#     base_triangolo = float(input("Inserisci la base del triangolo: "))
#     altezza_triangolo = float(input("Inserisci l'altezza del triangolo: "))
#     area_tri = area_triangolo(base_triangolo, altezza_triangolo)
#     aree.append(area_tri)
    
#     # Input per il quadrato
#     lato_quadrato = float(input("Inserisci il lato del quadrato: "))
#     area_quad = area_quadrato(lato_quadrato)
#     aree.append(area_quad)
    
#     # Input per il rettangolo
#     base_rettangolo = float(input("Inserisci la base del rettangolo: "))
#     altezza_rettangolo = float(input("Inserisci l'altezza del rettangolo: "))
#     area_ret = area_rettangolo(base_rettangolo, altezza_rettangolo)
#     aree.append(area_ret)
    
#     return aree

# # Eseguire la funzione per calcolare le aree
# lista_aree = calcola_aree()
# print("Lista delle aree calcolate:", lista_aree)