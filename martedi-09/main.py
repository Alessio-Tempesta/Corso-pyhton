# import xml.etree.ElementTree as ET

# xml_dati_stu = '''<studenti>
# <studente>
# <nome>Alice</nome>
# <eta>22</eta>
# </studente>
# <studente>
# <nome>Bob</nome>
# <eta>25</eta>
# </studente>
# </studenti>'''

# esercizio 1 
# # scrivere il documento xml su un file
# with open('studenti.xml', 'w') as file:
#     file.write(xml_dati_stu)
    
# # carica il documento del file 
# tree = ET.parse('studenti.xml')
# root = tree.getroot()

# for studente in root.findall('studente'):
#     nome = studente.find('nome').text
#     eta = studente.find('eta').text
#     print(f"il nome è : {nome} e la sua età è : {eta}")


# Scrivere un programma Python che crea un documento XML basato su dati forniti. Ad esempio, considera il seguente elenco di studenti:
# studenti = [
# {'nome': 'Alice', 'eta': '22'},
# {'nome': 'Bob', 'eta': '25'},
# {'nome': 'Charlie', 'eta': '20'}
# ]
# Il programma dovrebbe creare un documento XML che rappresenti questi studenti.

# Infine esportatelo come file.

# import xml.etree.ElementTree as ET

# # Lista degli studenti
# lista_studenti = [
#     {'nome': 'Alice', 'eta': '22'},
#     {'nome': 'Bob', 'eta': '25'},
#     {'nome': 'Charlie', 'eta': '20'}
# ]

# # Funzione per craerae l'elemento xml studenti
# def crea_xml_studenti(studenti):
#     # crea l'elemento
#     root = ET.Element("studenti")
    
#     #aggiung ogni studente in root 
#     for studente in studenti:
#         studente_el = ET.SubElement(root, "studente")
        
#         nome_el = ET.SubElement(studente_el, "nome")
#         nome_el.text = studente["nome"]
#         eta_el = ET.SubElement(studente_el, "eta")
#         eta_el.text = studente["eta"]
        
#     return root
        
# # Creare l'elemento radice del documento XML usando la funzione
# root = crea_xml_studenti(lista_studenti)

# tree = ET.ElementTree(root)
# # salva documento xml su un file
# tree.write('studenti.xml', encoding='utf-8', xml_declaration=True)
# tree = ET.parse('studenti.xml')
# root = tree.getroot()

# for studente in root.findall('studente'):
#     nome = studente.find('nome').text
#     eta = studente.find('eta').text
#     print(f"Il nome è: {nome} e la sua età è: {eta}")


# Scrivere un programma Python che modifica un documento XML esistente.Considera il seguente documento XML:
# <libri>
# <libro>
# <titolo>Python Cookbook</titolo>
# <autore>David Beazley</autore>
# </libro>
# <libro>
# <titolo>Fluent Python</titolo>
# <autore>Luciano Ramalho</autore>
# </libro>
# </libri>
# # Il programma dovrebbe aggiungere un nuovo libro al documento XML e stampare il documento risultante.il libro verra inserito tramite input e poi l'xml verrà salvato su file


# import xml.etree.ElementTree as ET

# xml_dati_libri = '''
# <libri>
#     <libro>
#         <titolo>Python Cookbook</titolo>
#         <autore>David Beazley</autore>
#     </libro>
#     <libro>
#         <titolo>Fluent Python</titolo>
#         <autore>Luciano Ramalho</autore>
#     </libro>
# </libri>
# '''

# root = ET.fromstring(xml_dati_libri)

# new_titolo = input("Inserisci il titolo del nuovo libro :")
# new_autore = input("Inserisci il nuovo autore del nuovo libro :")

# # crea elemento nuovo libro 
# nuovo_libro = ET.Element("Libro")
# titolo_el = ET.SubElement(nuovo_libro, "titolo") 
# titolo_el.text = new_titolo
# autore_el = ET.SubElement(nuovo_libro, "autore")
# autore_el.text = new_autore 

# # aggiungi il nuoivo libro all'xml 
# root.append(nuovo_libro)

# # salva xml aggioranto
# tree = ET.ElementTree(root)
# tree.write('libri_modificati.xml', encoding ='utf-8', xml_declaration=True)
# print(f"Nuovo libro aggiunto e salvato sul 'libri_modificati.xml':", ET.tostring(root, encoding='unicode'))

# # Scrivere un programma Python che ricerca e stampa gli elementi di un documento XML che soddisfano determinati criteri. Considera il seguente documento XML:
# <prodotti>
# <prodotto>
# <nome>Laptop</nome>
# <prezzo>800</prezzo>
# </prodotto>
# <prodotto>
# <nome>Smartphone</nome>
# <prezzo>500</prezzo>
# </prodotto>
# <prodotto>
# <nome>Tablet</nome>
# <prezzo>300</prezzo>
# </prodotto>
# </prodotti>
# Il programma dovrebbe cercare e stampare tutti i prodotti con un prezzo inferiore a 600.


# import xml.etree.ElementTree as ET

# # Definiamo il documento XML come una stringa
# xml_string = '''
# <prodotti>
#     <prodotto>
#         <nome>Laptop</nome>
#         <prezzo>800</prezzo>
#     </prodotto>
#     <prodotto>
#         <nome>Smartphone</nome>
#         <prezzo>500</prezzo>
#     </prodotto>
#     <prodotto>
#         <nome>Smartphone</nome>
#         <prezzo>599.99</prezzo>
#     </prodotto>
#     <prodotto>
#         <nome>Tablet</nome>
#         <prezzo>300</prezzo>
#     </prodotto>
# </prodotti>
# '''
# # parse della stringa xml in un oggetto elementTree
root = ET.fromstring(xml_string)

for prodotto in root.findall('prodotto'):
    nome = prodotto.find('nome').text
    prezzo = prodotto.find('prezzo').text
    prezzo = float(prodotto.find('prezzo').text)
    if prezzo < 600:
        print(f"Nome: {nome} e il prezzo è {prezzo}")





# Database sarà:
# -radice: <studenti>
# Per ogni studente:
# -Elemento <studente> con attributo id
# -Elemento figlio <nome> per il nome dello studente
# - Elemento figlio <corsi> che contiene elementi <corso> per ogni corso seguito dallo studente
# -Elemento figlio <corso> che contiene elementi <voto> per ogni corso seguito dallo studente unisci questo Al primo avvio se il database è presente viene letto, se non è presente risulta database vuoto!
# L'utente può aggiungere, eliminare o modificare uno studente, un corso o un elemento di corso

