import pandas as pd

diccionario_empleados = {
    15379 : "Hernan Maldonado",
    15419 : "Carlos Zambrano",
    15420 : "Elena Domínguez",
    46556 : "Teresa Benítez",
    46555 : "Sonia Blanco",
    46559 : "Ernesto García",
    15428 : "Rodrigo Torres",
    15429 : "Roberto Molina",
    47130 : "Nuria Flores",
    32117 : "Patricia Bermúdez",
    32313 : "Clara Ortiz"
}

serie_empleados = pd.Series(diccionario_empleados)

print("Serie:")
print(serie_empleados)

serie_ordenada_valores = serie_empleados.sort_values() # Si queremos ordenar de manera descendente, podemos usar el parámetro ascending=False

print("Serie ordenada por valores:")
print(serie_ordenada_valores)


serie_ordenada_indice = serie_empleados.sort_index()

print("Serie ordenada por índice:")
print(serie_ordenada_indice)