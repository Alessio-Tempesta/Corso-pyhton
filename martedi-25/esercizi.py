# parole = "La casa è grande, una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde e fiorito."

# duplicati = {}

# for parola in parole.split():
#     if parola in duplicati:
#         duplicati[parola]["Conteggio"] += 1
#     else:

#         duplicati[parola] = {"Conteggio" : 1, "Posizioni": [], "Lunghezza": len(parola) }
#     duplicati[parola]["Posizioni"].append(parole.index(parola))

#     # Stampa i risultati
#     for parola, valori in duplicati.items():
#         print(f"{parola} appare {valori['Conteggio']} volte, lunghezza {valori['Lunghezza']}. Posizioni: {valori['Posizioni']}")


# Scrivete un programma che riceve in input una stringa lunga e verifica se ci sono duplicati, quanti sono, quali sono e
# quanto sono lunghi i duplicati.
# Esempio:
# ‘La casa è grande, una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde
# e fiorito.’
# #outpout
# "La" appare 2 volte, lunghezza 2.



# stringa="La casa è grande, una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde e fiorito."
# punteggiatura="!,.;-"
# for let in punteggiatura:
#     stringa=stringa.replace(let,"")

# lista=list(stringa.lower().split(" "))

# #print(lista)
# par=[]
# rip=[]
# contr=False
# for parola in lista:
#     count=lista.count(parola)
#     print("parola", parola, count)
#     if count>1 and parola not in par:
#             par.append(parola)
#             rip.append(count)
#             contr=True

# #print(rip)
# if contr:
#     for i in par:
#         print(f"La parola {i} è ripetuta {rip[par.index(i)]} volte, di lunghezza {len(i)}")
# else:
#     print("Non c'è alcuna ripetizione")


# Scrivete un programma che utilizza il cifrario di Cesare per criptare una
# parola o decriptarla.
# Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
# ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
# sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
# di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
# una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
# Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
# conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
# di posti corrispondente alla chiave.


# Richiesta input all'utente
messaggio = input("Inserisci il messaggio da criptare o decriptare: ")
chiave = int(input("inserisci la chiave: "))
modalità = input("Vuoi criptare o decriptare il mesaggio? :")

chiave = chiave % 26

# validazione della modalità 
if modalità not in ['cripta', 'decripta']:
    print('Modalità non valida! Incserisci cripta o decripta')
else:
    risultato = ""
    for char in messaggio:
        if char.isalpha(): '''CONTROLLA SE IL CARATTERER è UNA LETTERA'''
        shift = chiave if modalità == 'cripta' else -chiave
        new_char = ord(char) + shift
        
        if char.islower():
                if new_char > ord('z'):
                    new_char -= 26
                elif new_char < ord('a'):
                    new_char += 26
                elif char.isupper():
                    if new_char > ord('Z'):
                        new_char -= 26
                elif new_char < ord('A'):
                    new_char += 26
                    risultato += chr(new_char)
        else:
            risultato += char  # Non modificare caratteri non alfabetici

    print("Risultato:", risultato)

