# Chieda all'utente di inserire una stringa.
# Conti quante vocali (a, e, i, o, u, sia maiuscole che minuscole) sono presenti nella stringa.
# Stampi il numero di vocali trovate nella stringa.



# funzione conta_vocali che prende in input una stringa e che conti quante vocali ci sono presenti sia maiusc che minusc,

def conta_vocali(stringa):   
    vocali = 'aeiouAEIOU'
    conteggio = 0
    for char in stringa: 
        if char in vocali:
            conteggio += 1
            return conteggio
        
        # La funzione main() chiede all'utente di inserire una stringa
        def main():
            input_stringa = input("Inserisci stringa: ")
            numero_vocali = conta_vocali(input_stringa)
            print( f"Il nuemro di vocali nella stringa ' {input_stringa}' e: '{numero_vocali}")

            if __name__ == "__main__":
                main()