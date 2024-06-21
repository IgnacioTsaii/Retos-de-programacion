import numpy as np
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

# Empiezo a tomar el tiempo para ver cuanto tarda
start = time.time()

D = calcular_distancias(df_X, df_Y)
D_matriz = np.asmatrix(D)
D = np.round(D, 2)
print(type(D))
print(D)

################################################################################

end = time.time()
print('Tiempo total: ', end - start, 's')
