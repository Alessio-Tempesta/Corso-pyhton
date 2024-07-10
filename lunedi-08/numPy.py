# esercizio ndarray. dtype. shape, arange crea un array numpy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell' array 1 utilizza la funzione np.arange per creare un array di numeri nteri da 10 a 49 2 verifica i l tipo di dato dell'array e stampa il risultato. 3 cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato. 4 stampa la froma dell'array 

import numpy as np

# array di numeir interi da 10 a 49
array = np.arange(15, 50)
# verifica del tipo di dato che si trova all'interno delle array np.arange()
dtype_initial = array.dtype
print(f"il tipo di dato iniziale e : {dtype_initial}")
# cambiare il tipo di dato all'interno dell'array
array_float = array.astype(np.float64)
cambia_d_type = array_float.dtype
print(f"Tipo d i dato dopo la conversione: {cambia_d_type} ")

# stampa forma dell'array
shape_array = array.shape
print(f"la forma dell'array : {shape_array}")