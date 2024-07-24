# Grafico a Barre
# import matplotlib.pyplot as plt

# categories = ['A', 'B', 'C', 'D', 'E']
# values = [3, 7, 2, 5, 8]

# plt.figure(figsize=[12, 8], facecolor='#f2e6ff')
# plt.bar(categories, values)
# plt.title('Grafico a Barre Personale')
# plt.xlabel('Categorie ')
# plt.ylabel('Valori')
# plt.show()




# # Istogramma:
# import numpy as np
# import matplotlib.pyplot as plt

# data = np.random.randn(1000)

# # Dimensioni e colore di sfondo della figura
# plt.figure(figsize=[10, 6], facecolor='purple')   

# # istogramma
# plt.hist(data, bins=30, color='red', edgecolor='black')  # Colore delle barre e bordo

# plt.grid(axis='y', linestyle='--')

# plt.title('Istogramma')
# plt.xlabel('Valori')
# plt.ylabel('Frequenza')
# plt.show()


# Scatter Plot:
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.random.rand(50)
# y = np.random.rand(50)
# # colori cas. per i punti
# colors = np.random.rand(50)
# sizes = 100 * np.random.rand(50) 

# plt.figure()
# plt.scatter(x, y)
# plt.title('Scatter Plot')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt

# # Dati casuali
# x = np.random.rand(50)
# y = np.random.rand(50)
# colors = np.random.rand(50)  # Colori casuali per i punti
# sizes = 50 * np.random.rand(50)  # Dimensioni casuali per i punti

# # Dimensioni e colore di sfondo della figura
# plt.figure(figsize=[12, 8], facecolor='#f2e6ff')  

# # Creazione dello scatter plot
# plt.scatter(x, y, c=colors, s=sizes, edgecolor='black')  # Colori, dimensioni

# # Titolo e etichette
# plt.title('Scatter Plot', pad=20, fontweight='bold', fontsize=24)
# plt.xlabel('X Axis', labelpad=15, fontweight='bold', fontsize=18)
# plt.ylabel('Y Axis', labelpad=15, fontweight='bold', fontsize=18)

# # Barra dei colori
# plt.colorbar(label='Color Scale')

# # Modifica del colore di sfondo degli assi
# plt.gca().set_facecolor('#e6ccff')

# # Modifica delle etichette assi
# plt.xticks(fontsize=14, fontweight='bold')
# plt.yticks(fontsize=14, fontweight='bold')

# # Mostrare il grafico
# plt.show()


