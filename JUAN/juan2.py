################################################################################
# CODIGO DEL ALUMNO
#print(D[:5])
#print(df_D.head())
rounded_D = np.round(D, 4)
rounded_df = np.round(df_D, 4)

# Convertir a arrays de numpy
matriz_D = np.asarray(rounded_D)
df_array = np.asarray(rounded_df)

print(df_array.shape)
print(matriz_D.shape)

# Comparar si las matrices son iguales
if np.array_equal(matriz_D, df_array):
    print("¡Me dio igual!")
else:
    print("¡Uh no, me equivoqué!")

# Contar las diferencias
diferencias = np.count_nonzero(matriz_D - df_array)
print("Número de diferencias:", diferencias)

###############################################################################
