import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)

df = pd.read_csv("datasets/data.csv")

print(df.info())

print(df.describe())

df["dateRep"] = df["dateRep"].astype("datetime64[s]")

# cambiar nombre columnas a español

columnas = ["fechas", "dia", "mes", "anio", "casos", "muertes", "pais", "Codigo_del_pais_dos_letras", "codigo_pais", "poblacion", "continente", "casos_acumulados"]

df.columns = columnas

#Eliminacion de columnas

df.drop(["Codigo_del_pais_dos_letras", "casos_acumulados" ], axis=1, inplace=True)

#Validar valores nulos
#Sumar columnas valores nulos y despues sumar todas las columnas
#Sacar el porcentaje de valores nulos
df.isna().sum().sum()/len(df)

#Eliminar valores nulos
df.dropna(inplace=True)

#Crear Dataframe muertos por pais 
df_por_pais = df.groupby("pais")[["casos"]["muertes"]].sum()