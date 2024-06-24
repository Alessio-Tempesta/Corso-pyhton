# Create un programma che richiede all’utente Nome, anno di
# nascita e giorno della settimana (a numero) e stampa in
# maniere formattata oltre al nome, l’età e i giorni che mancano
# al prossimo weekend (sabato):
# Esempio
# ’Il tuo nome è Tommaso, hai 37 anni e mancano 5 giorni al
# weekend’


# import datetime

# # Chiediamo all'utente di inserire il nome, l'anno di nascita e il giorno della settimana

# nome = input("Inserisci il tuo nome: ")
# anno_di_nascita = int(input("Inserisci l'anno di nascita: "))
# giorno_settimana = int(input("Inserisci il giorno della settimana (1 per lunedì, 7 per domenica): "))

# # Calcoliamo l'età dell'utente
# oggi = datetime.date.today()
# eta = oggi.year - anno_di_nascita

# # Calcoliamo i giorni mancanti al prossimo sabato

# oggi_giorno_settimana = oggi.weekday()
# giorni_mancanti_al_sabato = (6 - oggi_giorno_settimana) % 7

# # Creazione della stringa di output
# utente = f"Il tuo nome è {nome}, hai {eta} anni e mancano {giorni_mancanti_al_sabato} giorni al weekend."

# # Stampiamo il risultato
# print(utente)




# Input dell'utente per la prima operazione
# numero1 = float(input("Inserisci il primo numero: "))
# numero2 = float(input("Inserisci il secondo numero: "))
# operazione = input("Scegli l'operazione (+, -, *, /): ")

# # Calcolo e stampa del risultato per la prima operazione
# if operazione == "+":
#     risultato = numero1 + numero2
# elif operazione == "-":
#     risultato = numero1 - numero2
# elif operazione == "*":
#     risultato = numero1 * numero2
# elif operazione == "/":
#     # Gestione della divisione per zero
#     if numero2 != 0:
#         risultato = numero1 / numero2
#     else:
#         risultato = "Errore: divisione per zero"
# else:
#     risultato = "Operazione non valida"

# # Stampare il risultato della prima operazione
# if risultato != "Operazione non valida":
#     print(f"Il risultato di {numero1} {operazione} {numero2} è: {risultato}")
# else:
#     print(risultato)

# # Input dell'utente per la seconda operazione
# numero1 = float(input("Inserisci il primo numero: "))
# numero2 = float(input("Inserisci il secondo numero: "))
# operazione = input("Scegli l'operazione (+, -, *, /): ")

# # Calcolo e stampa del risultato per la seconda operazione
# if operazione == "+":
#     risultato = numero1 + numero2
# elif operazione == "-":
#     risultato = numero1 - numero2
# elif operazione == "*":
#     risultato = numero1 * numero2
# elif operazione == "/":
#     # Gestione della divisione per zero
#     if numero2 != 0:
#         risultato = numero1 / numero2
#     else:
#         risultato = "Errore: divisione per zero"
# else:
#     risultato = "Operazione non valida"

# # Stampare il risultato della seconda operazione
# if risultato != "Operazione non valida":
#     print(f"Il risultato di {numero1} {operazione} {numero2} è: {risultato}")
# else:
#     print(risultato)


# Scrivete un programma che chiede all'utente una lista di parole e restituisce la lunghezza di ogni parola.

#chiediamo ad utente di inserire lista di paorle
# input_parole = input("insersici una lista di parole:")

# # divisone input dell'utente lista parole 
# parole = input_parole.split()

# # utilizziamo ciclo for per iterare ogni parola
# for parola in parole:
#     lunghezza = len(parola)
#     print(f"la parola '{parola} è lunga {lunghezza} caratteri")


# Scrivete una programma che richiede una lista di numeri all’utente e fornisce in output un istogramma basato su questi numeri, usando asterischi
# per disegnarlo.
# Data ad esempio la lista [3, 7, 9, 5], il programma dovrà produrre questa
# sequenza: ***
# *******
# *********
# *****

# Chiediamo all'utente di inserire una lista di numeri separati da spazi
# num_input = input("inserisci una lista di numeri separasti da spazi:")

# # Dividiamo l'input dell'utente in una lista di stringhe e convertiamo ogni stringa in un intero
# numeri = list(map(int, num_input.split()))

# # chiediamo l'input dell'utente in una lista di stringhe e convertiamo ogni stringa in un un intero
# for numero in numeri: 
#     istogramma = "*" * numero
#     print(istogramma)

# Scrivete un programma che chiede una stringa all’utente e
# restituisce un dizionario rappresentante la "frequenza di
# comparsa" di ciascun carattere componente la stringa.
# Esempio:
# Stringa "ababcc",
# Risultato
# {"a": 2, "b": 2, "c": 2}





string_utente = input("inserisci una stringa: ")

# diuzionario vuoto per memorizzare la frequenza dei caratteri
freq_caratteri = {}

# iteriamo attraverso ogni caratteerer nella stringa 
for carattere in string_utente:
    # se è presnete nel dizionario, incrementiamo il suo conteggio
    if carattere in freq_caratteri:
        freq_caratteri[carattere] += 1
        # aggiunta del carattere al dizionario con conteggio iniziale di 1 
    else:
        freq_caratteri[carattere] = 1

        #stampa del dizionario
    print("Frequenza dei caratteri nella stringa:")
    print(freq_caratteri)
