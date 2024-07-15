"""create un gestionale scolastico basato su un database mysql, l'utente può inserire per ogni studente, nome, cognome, e 3 voti, uno per italiano, uno per matematica e uno per storia.
Se esistono già studenti si possono modificare le informazioni o eliminare"""
import mysql.connector

def connessione_server():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password = "root",
        )
        print(mydb)
        print("connessione ok")
        return mydb
    except:
        print("connessione non avvenuta")

def connessione_database():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = 'gestionale_scolastico'
        )
        
        return mydb
    except:
        print("Connessione non avvenuta!")



def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS studenti (
            IDStudente INT AUTO_INCREMENT PRIMARY KEY,
            Nome VARCHAR(255),
            Cognome VARCHAR(255),
            VotoItaliano INT,
            VotoMatematica INT,
            VotoStoria INT
        )
    """)
    print("Hai creato la tabella")

def insert_studente(cursor, nome, cognome, voto_italiano, voto_matematica, voto_storia):
    cursor.execute("""
        INSERT INTO studenti (Nome, Cognome, VotoItaliano, VotoMatematica, VotoStoria)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, cognome, voto_italiano, voto_matematica, voto_storia))
    
    print("Hai inserito i dati dello studente")

def update(cursor, nome, cognome, voto_italiano, voto_matematica, voto_storia,IDStudente):
    
    cursor.execute("""UPDATE studenti 
                   SET Nome = %s, Cognome= %s, VotoItaliano = %s, VotoMatematica = %s, VotoStoria=%s
                   WHERE IDStudente = %s
    """,(nome, cognome, voto_italiano, voto_matematica, voto_storia,IDStudente))
    
    print("Hai aggiornato i dati dello studente")
    
def elimina_studente (cursor,IDStudente):
    query = "DELETE FROM studenti Where IDStudente = %s"
    cursor.execute(query, (IDStudente,))
    mydb.commit()
    print("studente eliminato!!")

def vista (cursor):
    cursor.execute("SELECT * FROM Studenti")
    for elemento in cursor.fetchall():
        print(elemento)



mydb =connessione_server()
cursor = mydb.cursor()

#cursor.execute("CREATE DATABASE gestionale_scolastico")
cursor.execute("USE gestionale_scolastico")
connessione_database()
#create_table(cursor)
"""insert_studente(cursor,'Artuto','Verdi',2,3,4)
mydb.commit()"""

"""update(cursor,'Paolo','Gialli',7,10,9,1)
mydb.commit()"""
elimina_studente(cursor,2)