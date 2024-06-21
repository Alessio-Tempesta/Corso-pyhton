# def saluta(nome):
#     print("Ciao,", nome)  # Stampa il saluto con il nome specificato

# saluta("Alessio")
# saluta("MIRKO")
# saluta("MIRKO")


# ESERCIZO BASE: Indovina il numero descrizone. scrvi un programma che genera un numero casuale tra 1 e 100( inclusi ) l'utente deve indovinare quale numero è stato generato. Dopo ogni tentavo, il programma dovrebbe dire all'utente se il numero da indovinare è più alto o piu basso rispetto al numero insierito. il gioco termina quando l'utemte indpvina il numero o decide di uscire.

import random 

def gioco_indovina_numero():
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0

    print("benvenuto al gioco indovina il numero!")
    print("puoi uscire dal gioco in qualsiasi moemnto digitando 'exit'.")

 
    while True:
        tentativo = input("Indovina il numero (1-100): ")

        if tentativo.lower() == 'exit':
            print(f"Peccato che tu stia uscendo! Il numero da indovinare era {numero_da_indovinare}.")
            break 

        if not tentativo.isdigit():
            print("Inserisci un numero valido.")
            continue

        tentativo = int(tentativo)
        tentativi += 1

        if tentativo == numero_da_indovinare:
            print(f"Complimenti! Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi!")
            break  
        elif tentativo < numero_da_indovinare:
            print("Il numero da indovinare è più alto.")
        else:
            print("Il numero da indovinare è più basso.")

# Esegui il gioco
gioco_indovina_numero()