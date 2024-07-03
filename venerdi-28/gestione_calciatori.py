# import csv

# # Nome del file di database
# db_file = 'soccer_team.csv'

# # Inizializzare la squadra
# team = []

# # Carica la squadra dal file di database
# def load_team():
#     global team
#     try:
#         with open(db_file, 'r', newline='') as file:
#             reader = csv.reader(file)
#             team = [row for row in reader]
#     except FileNotFoundError:
#         save_team()

# # Salva la squadra nel file di database
# def save_team():
#     with open(db_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(team)

# # Aggiungi un giocatore alla squadra
# def add_player(nome, ruolo):
#     valid_roles = ['portieri', 'difensori', 'centrocampisti', 'attaccanti']
#     if ruolo not in valid_roles:
#         print("Ruolo non valido.")
#         return
#     limits = {'portieri': 3, 'difensori': 8, 'centrocampisti': 8, 'attaccanti': 6}
#     count = sum(1 for player in team if player[1] == ruolo)
#     if count >= limits[ruolo]:
#         print(f"Non puoi aggiungere più di {limits[ruolo]} {ruolo}.")
#         return
#     team.append([nome, ruolo])
#     save_team()
#     print(f"{nome} aggiunto come {ruolo}.")

# # Rimuovi un giocatore dalla squadra
# def remove_player(nome, ruolo):
#     for player in team:
#         if player[0] == nome and player[1] == ruolo:
#             team.remove(player)
#             save_team()
#             print(f"{nome} rimosso dai {ruolo}.")
#             return
#     print(f"{nome} non trovato tra i {ruolo}.")

# # Visualizza tutti i giocatori della squadra
# def view_team():
#     valid_roles = ['portieri', 'difensori', 'centrocampisti', 'attaccanti']
#     for ruolo in valid_roles:
#         print(f"{ruolo.capitalize()}:")
#         for player in team:
#             if player[1] == ruolo:
#                 print(f" - {player[0]}")
#         print()

# # Menu di gestione della squadra
# def menu():
#     while True:
#         print("\nMenu:")
#         print("1. Aggiungi giocatore")
#         print("2. Rimuovi giocatore")
#         print("3. Visualizza squadra")
#         print("4. Esci")
#         scelta = input("Seleziona un'opzione: ")

#         if scelta == '1':
#             nome = input("Nome del giocatore: ")
#             ruolo = input("Ruolo (portieri, difensori, centrocampisti, attaccanti): ").lower()
#             add_player(nome, ruolo)
#         elif scelta == '2':
#             nome = input("Nome del giocatore: ")
#             ruolo = input("Ruolo (portieri, difensori, centrocampisti, attaccanti): ").lower()
#             remove_player(nome, ruolo)
#         elif scelta == '3':
#             view_team()
#         elif scelta == '4':
#             break
#         else:
#             print("Opzione non valida. Riprova.")

# # Carica la squadra dal file e avvia il menu
# load_team()
# menu()














# '''Create un gestionale per la vostra squadra di calcio, 
# siete gli allenatori quindi potete aggiungere massimo 25 calciatori:
# 3 portieri;
# 8 difensori;
# 8 centrocampisti;
# 6 attaccanti;
# per ogni calciatore nome e ruolo.
# Nel menù potete aggiungerli, eliminarli o visualizzarli, 
# tutto verrà salvato in un database .txt'''
# def leggi_db_calciatori():
#     with open("fantacalcio.csv", "r") as file:
#         db_calciatori = file.read()
#     return db_calciatori

# def aggiungi_calciatori():
#     nome = input("inserisci nome calciatore ")
#     ruolo = input("inserisci ruolo calciatore ")
#     nome_ruolo = "\n" + nome + "," + ruolo 
#     with open("fantacalcio.csv", "a") as file:
#         file.write(nome_ruolo)

# def elimina_calciatori():
#     contenuto =leggi_db_calciatori()
#     print(contenuto)
#     nome = input("inserisci nome calciatore ")
#     ruolo = input("inserisci ruolo calciatore ")
#     nome_ruolo = nome + "," + ruolo 
#     contenuto = contenuto.split("\n")
#     if nome_ruolo in contenuto:
#         contenuto.remove(nome_ruolo)
#     contenuto ="\n".join(contenuto)
#     with open("fantacalcio.csv", "w") as file:
#         file.write(contenuto)

# db = leggi_db_calciatori()

# def conto_ruoli():

#     if 
#         db.count("portiere")  3:


# print(db.count("difensore"))



sqaudra_calcio = []