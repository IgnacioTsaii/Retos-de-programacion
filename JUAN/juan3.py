import numpy as np
import pandas as pd
import time

# Inicializo la matriz de distancias

################################################################################
# CODIGO DEL ALUMNO
def calcular_distancias(df_X, df_Y):
    matrix = []
    for i in range(len(df_X)):
        row = []
        for j in range(len(df_Y)):
            distance = np.sqrt((df_X.iloc[i, 0] - df_Y.iloc[j, 0])**2 + (df_X.iloc[i, 1] - df_Y.iloc[j, 1])**2)
            row.append(distance)
        matrix.append(row)
    return np.array(matrix)

# Definir la función para calcular distancias usando la función D
def D(df_X, df_Y):
    matrix = []
    for i in range(len(df_X)):
        row = []
        for j in range(len(df_Y)):
            distance = np.sqrt((df_X.iloc[i, 0] - df_Y.iloc[j, 0])**2 + (df_X.iloc[i, 1] - df_Y.iloc[j, 1])**2)
            row.append(distance)
        matrix.append(row)
    return np.array(matrix, dtype=object)

# Leer los DataFrames df_X y df_Y desde algún lugar
df_X = pd.DataFrame(...)
df_Y = pd.DataFrame(...)

# Empiezo a tomar el tiempo para ver cuánto tarda
start = time.time()

# Calcular la matriz de distancias utilizando la función D
D_funcion = D(df_X, df_Y)

# Calcular la matriz de distancias directamente
D_directo = calcular_distancias(df_X, df_Y)

# Redondear ambas matrices
D_funcion_redondeada = np.round(D_funcion, 2)
D_directo_redondeada = np.round(D_directo, 2)

# Comparar si las matrices redondeadas son iguales
if np.array_equal(D_funcion_redondeada, D_directo_redondeada):
    print("Las matrices son iguales.")
else:
    print("Las matrices no son iguales.")

# Finalizo el tiempo de ejecución y muestro el tiempo total
end = time.time()
print('Tiempo total: ', end - start, 's')
