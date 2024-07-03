
# # 1 chiediamo all'utente un num positivo
# while True:
#     n = int(input("inserisci un nuemro intero positvo"))
#     if n > 0:
#         break
#     else:
#         print("Il nuemro inserito non è positvo")

#     #2 genera lista du numeri casuali:

#         lista_numeri = list((1,n + 1))
#         print(f"Lista di numeri generati: {lista_numeri}")

#         # 3 Calcoliamo e stampiamo la somma dei numeri pari nella lista

#         somma_pari = 0
#         for numero in lista_numeri: 
#             if numero % 2 == 0:
#                 somma_pari += numero
#                 print(f"la somma dei numeri pari nella lista è: {somma_pari}")

#                 # STampiamo tutti i numeri dispri nella lista 
#                 somma_dispari = 1
#         for numero in lista_numeri: 
#             if numero % 2 != 0:
#                 somma_pari += numero
#                 print(f"la somma dei numeri pari nella lista è: {somma_pari}")