# # creare una classe ContoBancario che incapsula le informazioni di un conto e fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.
# Classe ContoBancario:
# Attributi privati:
# __titolare (stringa che rappresenta il nome del titolare del conto)
# __saldo (decimale che rappresenta il saldo del conto)
# Metodi pubblici:
# deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
# preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
# visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
# Gestione dei Metodi e Sicurezza:
# I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
# Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota)



class ContoBancario:
    def __init__(self, titolare, saldo_iniziale = 0.0):
        # titoalre come attributo privato
        #  saldo come att.privato
        self.__titolare = titolare
        self.__saldo = saldo_iniziale 
        
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"deposito di {importo} effettuato. il nuovo saldo :{self.__saldo} ")
        else:
            print("L'importo del deposito deve essere poositivo ")
            
    def preleva(self, importo):
        if importo > 0:
            if self.__saldo >= importo:
                self.__saldo -= importo
                print(f"Prelievo di {importo} effetuato, il nuovo saldo è: {self.__saldo}")
            else:
                print("fondi non sufficenti per effe il prelievo ")
        else:
            print("l'importo del èrelievo deve positivo")
            
    def visualizza_saldo(self):
        return self.__saldo
    
    # test di esempio 
conto_alessio = ContoBancario("Alessio Tempesta", 1500)
print(f"Il titolare del conto :{conto_alessio._ContoBancario__titolare}" )
print(f"Saldo Conto :{conto_alessio.visualizza_saldo()}" )
conto_alessio.deposita(500)
conto_alessio.preleva(200)

