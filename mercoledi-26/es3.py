# # Trasformate il programma che abbiamo creato in
# # precedenza per la gestione dei voti degli alunni in un
# # programma per la gestione di una classe che utilizza un
# # file come database:
# # All’avvio il programma chiede se si vuole leggere l’elenco
# # degli alunni e i loro voti e medie, se si vuole aggiungere un  alunno o un voto, se si vuole eliminare un alunno o un voto.


# def lettura():
#     with open("Giovedì 27/Es3.txt","r") as f:
#         dati =f.read()
#     return dati

# def scrittura(d):
#     with open("Giovedì 27/Es3.txt","w") as f:
#         f.writelines(str(d))

# def pulizia(a):
#     inutili = ["[","]","{","}","'"]
#     for contenuto in inutili:
#         a = a.replace(contenuto,"")
#     a = a.replace(":",",")
#     b = a.split(",")
#     return b


# def conversione(a):
#     dizionario = {}
#     for elemento in a:
#         if elemento.isalpha():
#             dizionario[elemento]= []
#             nome = elemento
#         else:
#             dizionario[nome].append(int(elemento))
#     return dizionario



# database = lettura()

# def lettura():
#     with open("Giovedì 27/Es3.txt","r") as f:
#         dati =f.read()
#     return dati

# def scrittura(d):
#     with open("Giovedì 27/Es3.txt","w") as f:
#         f.writelines(str(d))

# def pulizia(a):
#     inutili = ["[","]","{","}","'"]
#     for contenuto in inutili:
#         a = a.replace(contenuto,"")
#     a = a.replace(":",",")
#     b = a.split(",")
#     return b


# def conversione(a):
#     dizionario = {}
#     for elemento in a:
#         if elemento.isalpha():
#             dizionario[elemento]= []
#             nome = elemento
#         else:
#             dizionario[nome].append(int(elemento))
#     return dizionario



# database = lettura()












# """alunni={}

# while True:
#     v = True
#     nome = input("Inserire nome alunno: ")
#     while not nome.isalpha:
#         nome = input("Inserire nome alunno valido: ")
#     alunni[nome] = []
#     while v:
#         v_materia = input("Inserire voto: ")
#         while not v_materia.isnumeric:
#             v_materia = input("Inserire voto materia valido: ")
#         v_materia_i = int(v_materia)
#         alunni[nome].append(v_materia_i)
#         k = input("Vuoi continuare? (1/0): ")
#         if k == "0":
#             v = False
#     break

# print(alunni)

# scrittura(alunni)"""






# """print("\nGestione Database Studenti")
#         print("1. Visualizza elenco alunni e medie")
#         print("2. Aggiungi nuovo alunno")
#         print("3. Aggiungi voto a un alunno")
#         print("4. Elimina alunno")
#         print("5. Elimina voto di un alunno")
#         print("0. Esci")
# z = input("Indicare scelta: ")



# for alunno in alunni:
#     somma = 0
#     count = 0
#     for materia in alunni[alunno]:
#         somma+= alunni[alunno][materia]
#         count+=1
#     print("La media di", alunno, "è", somma/count)"""

# 1
# NOVITÀ

# DaniFila — Oggi alle 10:21
# database = lettura()
# database = pulizia(database)
# database = conversione(database)


# print("\nGestione Database Studenti")
# print("1. Visualizza elenco alunni e medie")
# print("2. Aggiungi nuovo alunno")
# print("3. Aggiungi voto a un alunno")
# print("4. Elimina alunno")
# print("5. Elimina voto di un alunno")
# print("0. Esci")

# z = input("Inserire opzione: ")

# while True:
#     if z == "1":
#         for alunno in database:
#             somma = 0
#             count = 0
#             for voti in database[alunno]:
#                 somma+= voti
#                 count+=1
#             print("La media di", alunno, "è", somma/count)
#     elif z == "2":
#         v = True
#         nome = input("Inserire nome alunno: ")
#         while not nome.isalpha:
#             nome = input("Inserire nome alunno valido: ")
#         database[nome] = []
#         while v:
#             v_materia = input("Inserire voto: ")
#             while not v_materia.isnumeric:
#                 v_materia = input("Inserire voto materia valido: ")
#             v_materia_i = int(v_materia)
#             database[nome].append(v_materia_i)
#             k = input("Vuoi continuare? (1/0): ")
#             if k == "0":
#                 v = False

#         scrittura(database)

# while True:
#     v = True
#     nome = input("Inserire nome alunno: ")
#     while not nome.isalpha:
#         nome = input("Inserire nome alunno valido: ")
#     database[nome] = []
#     while v:
#         v_materia = input("Inserire voto: ")
#         while not v_materia.isnumeric:
#             v_materia = input("Inserire voto materia valido: ")
#         v_materia_i = int(v_materia)
#         database[nome].append(v_materia_i)
#         k = input("Vuoi continuare? (1/0): ")
#         if k == "0":
#             v = False
#     break











# """alunni={}

# while True:
#     v = True
#     nome = input("Inserire nome alunno: ")
#     while not nome.isalpha:
#         nome = input("Inserire nome alunno valido: ")
#     alunni[nome] = []
#     while v:
#         v_materia = input("Inserire voto: ")
#         while not v_materia.isnumeric:
#             v_materia = input("Inserire voto materia valido: ")
#         v_materia_i = int(v_materia)
#         alunni[nome].append(v_materia_i)
#         k = input("Vuoi continuare? (1/0): ")
#         if k == "0":
#             v = False
#     break

# print(alunni)

# scrittura(alunni)"""






# """print("\nGestione Database Studenti")
#         print("1. Visualizza elenco alunni e medie")
#         print("2. Aggiungi nuovo alunno")
#         print("3. Aggiungi voto a un alunno")
#         print("4. Elimina alunno")
#         print("5. Elimina voto di un alunno")
#         print("0. Esci")
# z = input("Indicare scelta: ")



# for alunno in alunni:
#     somma = 0
#     count = 0
#     for materia in alunni[alunno]:
#         somma+= alunni[alunno][materia]
#         count+=1
#     print("La media di", alunno, "è", somma/count)"""