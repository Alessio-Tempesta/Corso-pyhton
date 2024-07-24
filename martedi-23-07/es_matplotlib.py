# Create un programma che crea un dataframe sulla base dell'imput dell'utente contenente 4 studenti e i loro voti mensili per sei mesi di studio in 4 materie.
# Il programma ci restituirà:
# -Un grafico contenente 4 grafici più piccoli, uno per ogni studente, con andamento delle medie dei voti per ogni mese;
# - Un altro grafico che racchiude tutti gli andamenti di tutti gli studenti

import pandas as pd
import matplotlib.pyplot as plt

# Funzione per ottenere i dati dall'utente e creare il DataFrame
def ottenere_dati_studenti():
    studenti = []
    materie = ['Matematica', 'Storia', 'Inglese', 'Scienze']
    mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno']

    for i in range(4):
        nome = input(f"Inserisci il nome dello studente {i + 1}: ")
        for mese in mesi:
            voti = []
            print(f"Inserisci i voti per {mese} per {nome}:")
            for materia in materie:
                while True:
                    try:
                        voto = float(input(f"  {materia}: "))
                        if 0 <= voto <= 10:
                            voti.append(voto)
                            break
                        else:
                            print("Il voto deve essere tra 0 e 10. Riprova.")
                    except ValueError:
                        print("Input non valido. Inserisci un numero.")
            dati = {
                'Nome': nome,
                'Mese': mese,
                'Matematica': voti[0],
                'Storia': voti[1],
                'Inglese': voti[2],
                'Scienze': voti[3]
            }
            studenti.append(dati)
    
    df = pd.DataFrame(studenti)
    return df, mesi

# Funzione per calcolare le medie mensili per ogni studente
def calcolare_medie_mensili(df):
    # Calcolare la media mensile per ogni studente
    df['Media'] = df[['Matematica', 'Storia', 'Inglese', 'Scienze']].mean(axis=1)
    medie_mensili = df.groupby(['Nome', 'Mese'])['Media'].mean().reset_index()
    return medie_mensili

# Funzione per creare i grafici
def creare_grafici(df, mesi):
    # Grafico con 4 grafici più piccoli (uno per ogni studente)
    studenti = df['Nome'].unique()
    fig, assi = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    assi = assi.flatten()

    for i, studente in enumerate(studenti):
        dati_studente = df[df['Nome'] == studente]
        assi[i].plot(dati_studente['Mese'], dati_studente['Media'], marker='o', label=studente)
        assi[i].set_title(studente)
        assi[i].set_xlabel('Mese')
        assi[i].set_ylabel('Media Voti')
        assi[i].legend()
        assi[i].grid(True)
    
    plt.tight_layout()
    plt.show()

    # Grafico aggregato
    plt.figure(figsize=(12, 6))
    for studente in studenti:
        dati_studente = df[df['Nome'] == studente]
        plt.plot(dati_studente['Mese'], dati_studente['Media'], marker='o', label=studente)

    plt.title('Andamento delle Medie Mensili di Tutti gli Studenti')
    plt.xlabel('Mese')
    plt.ylabel('Media Voti')
    plt.legend()
    plt.grid(True)
    plt.show()

# Funzione principale
def main():
    df, mesi = ottenere_dati_studenti()
    df_medie = calcolare_medie_mensili(df)
    creare_grafici(df_medie, mesi)

# Esegui il programma
if __name__ == "__main__":
    main()
