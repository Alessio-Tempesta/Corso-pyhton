import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print(mydb)

mycursor = mydb.cursor()

# per creare 
# query = "create database testpython"

# per mostrare i database lancio comando 
query = "SHOW DATABASES "

# Per eseguire la query
mycursor.execute(query)

# ciclo for per ottenere i varti DB
for database in mycursor:
    print(database)
    
def connessione_database():
    try:
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            port= "3306",
            database = 'testpython'
        )
        print("connessione ok")
        mycursor = mydb.cursor()
        return mycursor
        except:
        print("Connessione non avvenuta!")
    
mycursor = connessione_database()