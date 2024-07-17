# numpy.linalg.solve:

# Questa funzione viene utilizzata per risolvere un sistema lineare di equazioni della forma Ax=BAx = BAx=B, dove AAA è una matrice quadrata e BBB è un vettore o una matrice.

import numpy as np

# Creazione della matrice A e del vettore B
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])

# Risoluzione del sistema di equazioni Ax = B
x = np.linalg.solve(A, B)
print("Soluzione x:", x)  # Output: [2. 3.]



# numpy.fft.fft
# Questa funzione calcola la Trasformata di Fourier Discreta (DFT) di un array. La DFT è uno strumento potente per analizzare le frequenze dei segnali.

import numpy as np

# Creazione di un segnale
t = np.linspace(0, 1, 400)
sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)

# Calcolo della Trasformata di Fourier
fft_sig = np.fft.fft(sig)

# Frequenze associate
freqs = np.fft.fftfreq(len(fft_sig))

print("Trasformata di Fourier:", fft_sig)
print("Frequenze associate:", freqs)