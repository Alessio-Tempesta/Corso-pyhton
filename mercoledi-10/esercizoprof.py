import xml.etree.ElementTree as ET

def verifica_db():
    try:
        tree = ET.parse("db_studenti.xml")
        root = tree.getroot()
        studenti = 0
        for studente in root.findall('studente'):
            studenti +=1
        if studenti < 1:
            vuoto = True
        else:
            vuoto = False
    except:
        vuoto = True
        tree = ""
        root= ""
    return vuoto, tree, root

def aggiungi_studente(id, root):
    id = str(id)
    studente = ET.SubElement(root, "studente", attrib={"id":id})
    nome = input("Inserisci nome studente: ")
    nome_studente = ET.SubElement(studente, "nome").text = nome
    corsi = ET.SubElement(studente, "corsi")
    corso = ET.SubElement(corsi, "corso")
    nome_corso = input("Inserisci il nome del corso: ")
    tag_nome_corso = ET.SubElement(corso, "nome").text = nome_corso
    voto_corso = input("Inserisci il voto del corso: ")
    tag_voto_corso = ET.SubElement(corso, "voto").text = voto_corso
    scrivi_xml(root)


def scelta_aggiungi_studente(root, vuoto):
    if vuoto:
        root = ET.Element("Studenti")
        id = 1
        aggiungi_studente(id, root)
    else:
        studenti = 0
        for studente in root.findall('studente'):
            studenti +=1
        id = studenti +1
        aggiungi_studente(id, root)

def scrivi_xml(root):
    tree = ET.ElementTree(root)
    try:
        tree.write("db_studenti.xml")
        print("db scritto")
    except:
        print("errore nella scrittura del db")

def rimuovi_studente(root, vuoto):
    if vuoto:
        print("Nessun studente presente!")
    else:
        nome = input("Inserisci il nome dell'utente da eliminare: ")
        trovato = False
        for studente in root.findall("studente"):
            if studente.find("nome").text == nome:
                root.remove(studente)
                trovato = True
        if trovato:
            print("Alunno eliminato")
            scrivi_xml(root)
        else:
            print("Studente non trovato!")

def modifica_studente(root, vuoto):
    if vuoto:
        print("Nessun studente presente!")
    else:
        nome = input("Inserisci il nome dell'utente da Modificare: ")
        trovato = False
        for studente in root.findall("studente"):
            if studente.find("nome").text == nome:
                nuovo_nome = input("Inserisci il nuovo nome: ")
                studente.find("nome").text = nuovo_nome
                trovato = True
        if trovato:
            print("Alunno modificato")
            scrivi_xml(root)
        else:
            print("Studente non trovato!")


def aggiungi_corso(root, vuoto):
    if vuoto:
        print("Nessuno studente presente")
    else:
        trovato = False
        nome = input("Inserisci nome studente al quale vuoi aggiungere un corso: ")
        for studente in root.findall("studente"):
            if studente.find("nome").text == nome:
                corsi =studente.find("corsi")
                corso = ET.SubElement(corsi, "corso")
                nome_corso = input("Inserisci il nome del corso: ")
                tag_nome_corso = ET.SubElement(corso, "nome").text = nome_corso
                voto_corso = input("Inserisci il voto del corso: ")
                tag_voto_corso = ET.SubElement(corso, "voto").text = voto_corso
                trovato =True
        if trovato:
            scrivi_xml(root)
            print("Corso aggiunto")
        else:
            print("Studente non trovato")


def rimuovi_corso(root, vuoto):
    if vuoto:
        print("Nessuno studente presente")
    else:
        trovato = False
        nome_studente = input("Inserisci nome studente del quale vuoi eliminare un corso: ")
        nome_corso = input("Inserisci il nome del corso da eliminare: ")
        for studente in root.findall("studente"):
            if studente.find("nome").text == nome_studente:
                corsi =studente.find("corsi")
                for corso in corsi.findall("corso"):
                    if corso.find("nome").text == nome_corso:
                        corsi.remove(corso)
                        trovato= True 
        if trovato:
            print("Corso eliminato")
            scrivi_xml(root)
        else:
            print("Corso non trovato!")

def modifica_corso(root, vuoto):
    if vuoto:
        print("Nessuno studente presente")
    else:  
        trovato = False
        nome_studente = input("Inserisci nome studente del quale vuoi eliminare un corso: ")
        nome_corso = input("Inserisci il nome del corso da eliminare: ")
        for studente in root.findall("studente"):
            if studente.find("nome").text == nome_studente:
                corsi =studente.find("corsi")
                for corso in corsi.findall("corso"):
                    if corso.find("nome").text == nome_corso:
                        scelta = input("Vuoi modificare il nome corso o il voto del corso?")
                        if scelta == "nome":
                            corso.find("nome").text = input("Inserisci nuovo nome corso: ")
                        else:
                            corso.find("voto").text = input("Inserisci nuovo voto corso: ")
                        trovato = True
        if trovato:
            print("Corso modificato")
            scrivi_xml(root)
        else:
            print("Corso non trovato!")







vuoto, tree, root = verifica_db()
scelta_aggiungi_studente(root, vuoto)
vuoto, tree, root = verifica_db()
aggiungi_corso(root)
vuoto, tree, root = verifica_db()
rimuovi_corso(root)
vuoto, tree, root = verifica_db()