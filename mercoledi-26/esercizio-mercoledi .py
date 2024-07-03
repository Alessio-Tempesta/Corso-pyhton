with open("./file.txt", "r", encoding="utf-8") as file:
    text = file.read()

# suddivisione il testo in parole 
words = text.split()
# suddivisione testo in righe
lines = text.splitlines()
#calcolare il numero fi caratteri
char = len(text)

print(f"Nunero di parole: {len(words)}" )

print(f"Numero di righe: {len(lines)}")

print(f"Numero di caratteri: {char}")
