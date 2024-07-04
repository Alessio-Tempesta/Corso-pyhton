# creare una classe base Posto che rappresenta un singolo posto nel teatro. Da questa, deriveranno
# diverse classi per tipi specifici di posti, come PostoVIP e PostoStandard. Sarà inoltre
# necessaria una classe Teatro per gestire tutti i posti e le prenotazioni.

# Classe Posto:
# Attributi privati:
# _numero (intero: numero del posto)
# _fila (stringa: fila in cui si trova il posto)
# _occupato (booleano: stato del posto, se è occupato o meno)
# Metodi:
# prenota(): prenota il posto se non è già occupato.
# libera(): libera il posto se è occupato.
# Getter per numero e fila, e uno stato che indica se il posto è occupato.
# Classi Derivate:
# PostoVIP:
# Aggiunge un attributo per servizi_extra (e.g., accesso al lounge, servizio in posto).
# Sovrascrive il metodo prenota() per includere la gestione dei servizi extra.
# PostoStandard:
# Potrebbe avere un costo aggiuntivo per la prenotazione online o altri servizi meno
# esclusivi.
# Classe Teatro:
# Attributi:
# _posti: lista di tutti i posti nel teatro.
# Metodi:
# prenota_posto(numero, fila): trova e prenota un posto specifico.
# stampa_posti_occupati(): mostra tutti i posti occupati.


# class Posto 
class Posto:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False #stato posto libero 
        
    # Metodo per prenotare il posto    
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila} - {self._numero} prenotato")
        else:
            print(f"Posto {self._fila} - {self._numero} è già occupato")
        
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila} - {self._numero} liberato")
        else:
            print(f"Posto {self._fila} - {self._numero} è già libero")
        
    def get_numero(self):
        return self._numero  
    
    def get_fila(self):
        return self._fila
    
    def se_occupato(self):
        return self._occupato
    
    
class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self._servizi_extra = servizi_extra
            
    def prenota(self):
        if not self.se_occupato():
            self._occupato = True
            print(f"Posto VIP {self._fila} - {self._numero} prenotato con servizi extra: {self._servizi_extra}")
        else:
            print(f"Posto VIP {self._fila} - {self._numero} è già occupato.")
                
    def servizi_extra(self):
        return self._servizi_extra
        
        
class PostoStandard(Posto):
    def __init__(self, numero, fila, costo_aggiuntivo):
        super().__init__(numero, fila)
        self._costo_aggiuntivo = costo_aggiuntivo
            
    def prenota(self):
        if not self.se_occupato():
            self._occupato = True
            print(f"Il posto standard {self._fila} - {self._numero} è stato prenotato con costo aggiuntivo di: {self._costo_aggiuntivo}")
        else:
            print(f"Il posto Standard {self._fila} - {self._numero} è già occupato")
            
            
class Teatro:
    def __init__(self):
        self._posti = []
        
    def aggiungi_posto(self, posto):
        self._posti.append(posto)
        
    def prenota_posto(self, numero, fila):
        posto_trovato = False
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                posto_trovato = True
                break
        if not posto_trovato:
            print(f"Il posto {fila} - {numero} non è stato trovato.")
    
    def stampa_posti_occupati(self):
        print("Posti occupati:")
        for posto in self._posti:
            if posto.se_occupato():
                print(f"{posto.get_fila()} - {posto.get_numero()}")


# Creazione dei posti e del teatro
posto1_standard = PostoStandard(1, "A", "10 EUR aggiuntivi")
posto2_standard = PostoStandard(2, "B", "15 EUR aggiuntivi")
posto3_vip = PostoVIP(10, "C", "Accesso al lounge")

teatro = Teatro()
teatro.aggiungi_posto(posto1_standard)
teatro.aggiungi_posto(posto2_standard)
teatro.aggiungi_posto(posto3_vip)

# Prenotazione dei posti
teatro.prenota_posto(1, "A") 
teatro.prenota_posto(2, "B")  
teatro.prenota_posto(10, "C")  
teatro.prenota_posto(3, "C")  

# Stampa dei posti occupati
teatro.stampa_posti_occupati()