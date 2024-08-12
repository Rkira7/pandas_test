import pandas as pd
import numpy as np

columnas = ["Alimentos", "Cantidad", "Minutos"]

alimentos = np.random.randint(1, 4, (5000))
cantidad = np.random.randint(1, 10, (5000))
minutos = np.ones((5000))

df = pd.DataFrame((alimentos, cantidad, minutos))
df = df.T
df.columns = columnas

#la columna minutos del df se cambiaran por las filas de la columna minuos donde
# en todas las filas de la columna alimentos sea igual a 1
df["Minutos"] = df["Minutos"].where(df.loc[:, "Alimentos"] == 1) * (df["Cantidad"]*3)

#Asignar a Minutos cuando Minustos sea nulo y alimentos tenga el valor de 2
#Multiplicar por 4
df["Minutos"][(df["Minutos"].isnull()) & (df["Alimentos"] == 2)] = \
    df["Cantidad"][df["Alimentos"] == 2] * 4

df["Minutos"][(df["Minutos"].isnull()) & (df["Alimentos"] == 3)] = \
    df["Cantidad"][df["Alimentos"] == 3] * 6

df.to_csv("dataset_creado.csv", index=False)