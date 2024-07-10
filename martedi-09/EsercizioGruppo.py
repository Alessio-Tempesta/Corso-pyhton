"""Database sarà:
-radice: <studenti>
Per ogni studente:
-Elemento <studente> con attributo id
-Elemento figlio <nome> per il nome dello studente
- Elemento figlio <corsi> che contiene elementi <corso> per ogni corso seguito dallo studente
-Elemento figlio <corso> che contiene elementi <voto> per ogni corso seguito dallo studente

Al primo avvio se il database è presente viene letto, se non è presente risulta database vuoto!
L'utente può aggiungere, eliminare o modificare uno studente, un corso o un elemento di corso"""

import xml.etree.ElementTree as ET


def crea_db():
    root = ET.Element('studenti')
    tree = ET.Element(root)
    tree.write("database.xml")
    
    