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



# string_utente = input("inserisci una stringa: ")

# # diuzionario vuoto per memorizzare la frequenza dei caratteri
# freq_caratteri = {}

# # iteriamo attraverso ogni caratteerer nella stringa 
# for carattere in string_utente:
#     # se è presnete nel dizionario, incrementiamo il suo conteggio
#     if carattere in freq_caratteri:
#         freq_caratteri[carattere] += 1
#         # aggiunta del carattere al dizionario con conteggio iniziale di 1 
#     else:
#         freq_caratteri[carattere] = 1

#         #stampa del dizionario
#     print("Frequenza dei caratteri nella stringa:")
#     print(freq_caratteri)


# Scrivete un programma che chiede un numero all’utente e
# restituisce un dizionario con il quadrato del numero, se è pari o
# dispari e quante cifre contiene.
# Esempio:
# Numero 12
# Risultato {‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }


# numero = int(input("Inserisci un numero :"))

# # calcolo il quadrato del numero
# quadrato = numero ** 2

# # Capiamo se è pari o dispari
# if numero % 2 == 0:
#     pari_dispari = 'pari'
# else:
#     pari_dispari = 'dispari'

# #Determininamo il numero di cifre del numero convertednolo in stringa e misruandone la lunghezz
# n_cifre = len(str(numero))

# risultato = {
#         'quadrato': quadrato,
#         'pari o dispari': pari_dispari,
#         'n.di cifre': n_cifre
#     }

# print("Risultato: ")
# print(risultato)


# Scrivete un programma che prenda i nomi degli alunni di una
# classe e i loro voti, quando l’utente scrive media il programma
# andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10


# Inizialiazzaione dizionario nomi e voti alunni
# alunni = {}

# # ciclo while per raccoligeir i dati alunni
# while True:
#     nome = input("inserisci il nome dell'alunno oppure la media per calcolo medie:")
#     if nome.lower() == 'media':
#         break

#     # chiediamo i voti separati dagli spazi
#     voti =input(f"Inserisci i voti di {nome} separati da spazi: ")
#     lista_di_voti = list(map(float, voti.split()))

#     # voti alunni nel dizionario
#     alunni[nome] = lista_di_voti

#     print("\nMedie dei voti degli alunni:")
#     for nome, voti in alunni.items():
#         media_voti = sum(voti) / len(voti)
#         print(f"Nome: { nome }, Media: {media_voti:.2f}")

#     print("il programma è terminato ")




# Scrivete un programma che utilizza una funzione che accetta
# """come parametro una stringa passata dall’utente e restituisce in
# risposta se è palindroma o no.
# Esempio:‘I topi non avevano nipoti’ è palindroma‘Ai rimpianti rimediamo Maria’ è palindroma
# ‘Ciao’ non è palindroma"""

# def palindromo(stringa):
#     # funzione verifica se una stringa è palindroma.Restituisce True se la stringa è palindroma, altrimenti False.
#     stringa_senza_spazi = ''.join(stringa.split()).lower()
    
#     # Invertiamo la stringa
#     inverti_stringa = stringa_senza_spazi[::-1]
    
#     #  se la stringa originale è uguale alla sua versione invertita
#     return stringa_senza_spazi == inverti_stringa

# stringa_user = input("Inserisci una frase: ")

# # se la stringa inserita dall'uteente è palindroma
# if palindromo(stringa_user):
#     print(f"'{stringa_user}' è palindroma.")
# else:
#     print(f"'{stringa_user}' non è palindroma.")


# def palindroma(parola):
#     # Calcoliamo l'indice dell'ultimo carattere nella parola
#     indice = (len(parola) -1)
#     nuova_parola = ""

#     # Costruiamo una nuova parola invertendo la parola originale
#     while indice >= 0:
#         nuova_parola += parola[indice]
#         indice -= 1 

#     #  Dopo aver costruito la nuova parola invertita, controlliamo se è uguale alla parola originale
#     if nuova_parola == parola:
#         print(nuova_parola + " : la parola è un palindromo")
#     else:
#         print(nuova_parola + ": la parola non è un palindormo")

# parola1 = "radar"
# parola2 = "i topi non avevano nipoti"
# parola3 = "ciao"

# palindroma(parola2)
# palindroma(parola1)
# palindroma(parola3)




