# Eliminar filas y columnas con valores faltantes en un DataFrame de Pandas

import pandas as pd

archivo = 'empleados.csv'
df_empleados = pd.read_csv(archivo, delimiter=",")

print("Dataframe original:")
print(df_empleados)

df_empleados = df_empleados.drop(columns=['Estado_Civil'])
print("Dataframe sin estado civil:")
print(df_empleados)

df_empleados = df_empleados.drop(df_empleados.index[0])
print("Dataframe después de eliminar el primer registro:")
print(df_empleados)
