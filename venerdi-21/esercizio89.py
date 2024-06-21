# scrivi un programma che chieda all'utente di inserire un numero intero positivo n

# il programma deve poi eseguire le seguenti operazioni: 1 utilizzare un ciclo while per garantire che l'utente inserisca un numero postivo. se l'utente inserisce un numero negativo  a zero, ilk programma deve continare a chiedere un numero fino a quando non viene inserito un numero positvo. 2 utilizzare un ciclo for con range per calcoare e stampare la somma dei numeri pari a 1 a n. 3 utiulizzare un ciclo for per stampare tutti i numeri disapri da 1 a n. 4 utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. il programma deve stampare se n è primo 

# 1 inserimento numero postivo 
while True: 
    n = int(input("Insrisci un numero positivo: "))
    if n > 0:
        break
    else:
        print("il primo nuemro inserito non è positvio")

# 2 utilizzare un ciclo for con range per calcoare e stampare la somma dei numeri pari a 1 a n
somma_pari = 0

for i in range(2, n + 1, 2): 
    somma_pari += i
    print (f"La somma dei numri pari da 1 a {n} è: {somma_pari}")

    # 3 ciclo for per stampa num dispari da 1 a n 
    print(f"i numeri dispari da 1 a {n} sono:")
    for i in range(1, n + 1, 2):
        print(i)

        #Utilizziamo una struttura if per determinare se n è un numero primo

    if n <= 1:
        primo = False
    else: 
        primo = True
        for i in range(2, int(n**0) +1): 
            if n % i == 0:
                primo = False
                break

            if primo:
                print (f" il numero {n} è primo ")
            else:
                print (f"il nuemro {n} non è primo")
