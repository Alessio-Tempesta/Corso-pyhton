import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]

# y = [2, 3, 5, 7, 11]

# plt.rcParams['figure.facecolor'] = 'd4e4bc'  # Colore di sfondo della figura
# plt.rcParams['grid.color'] = '#cccccc' 

# plt.rcParams['grid.linestyle'] = '--'         # Stile della griglia
# plt.rcParams['axes.titlesize'] = 16           # Dimensione del titolo

# plt.figure()

# plt.plot(x, y)

# plt.title('Grafico a Linee Mio Personale', pad=20, fontweight='bold')

# plt.xlabel('X Axis')

# plt.ylabel('Y Axis')

# plt.show()



import matplotlib.pyplot as plt

# Dati degli smartphone più venduti
smartphones = ['iPhone 15', 'Samsung Galaxy S24Ultra', 'Xiaomi Mi 13', 'OnePlus 10', 'Google Pixel 7a']
sales = [200, 150, 120, 100, 90]  # Milioni di unità vendute

# Configurazione del grafico
plt.figure(figsize=[10, 6], facecolor='orange')  # Dimensioni e colore di sfondo della figura
plt.bar(smartphones, sales, color='dodgerblue')  # Grafico a barre con colore delle barre

# Titolo e etichette
plt.title('Smartphone Più Venduti', pad=20, fontweight='bold', fontsize=16)
plt.xlabel('Modello di Smartphone', labelpad=15, fontweight='bold', fontsize=14)
plt.ylabel('Unità Vendute (milioni)', labelpad=15, fontweight='bold', fontsize=14)

# Etichettare i valori sopra le barre
for i, v in enumerate(sales):
    plt.text(i, v + 5, str(v), ha='center', fontweight='bold', fontsize=12)

# Mostrare il grafico
plt.show()