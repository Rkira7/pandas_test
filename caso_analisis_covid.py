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
df_por_pais = df.groupby("pais")[["casos", "muertes"]].sum()
df_por_pais["relacion_mortalidad"] = df_por_pais["muertes"]/df_por_pais["casos"]

datos = df_por_pais["relacion_mortalidad"].sort_values(ascending=False).head(15)
plt.figure(figsize=(15, 10))
plt.bar(datos.index, datos)
plt.title("Top 15 con las mayots tasas de mortalidad")
plt.xlabel("Pais")
plt.ylabel("Casos de mortlidad")
plt.xticks(rotation = 15)
plt.show()


datos2 = df_por_pais["casos"].sort_values(ascending=False).head(10)
plt.figure(figsize=(10,10))
plt.pie(datos2, labels=datos2.index, autopct="%.2f%%")
plt.show()

datos3 = df_por_pais.muertes.sort_values(ascending=False).head(10)
plt.figure(figsize=(15, 10))
plt.bar(datos3.index, datos3)
plt.title("Top 10 paises con mayores muertes por COVID-19 durante el 2020")
plt.xlabel("Paises")
plt.ylabel("Muertes")
plt.xticks(rotation=15)
plt.show

df_por_meses = df.groupby("mes")[["casos", "muertes"]].sum()

figura = plt.figure(figsize=(12,12))
grafica1 = figura.add_subplot(1,2,1)
grafica2 = figura.add_subplot(1,2,2)

grafica1.plot(df_por_meses.casos)
grafica1.set_title("Total de casos mensuales de COVID-19 2020")
grafica1.set_xlabel("Mes")
grafica1.set_ylabel("Cantidad casos por mes")

grafica2.plot(df_por_meses.muertes)
grafica2.set_title("Total de muertes mensuales de COVID-19 2020")
grafica2.set_xlabel("Muertes")
grafica2.set_ylabel("Cantidad muertes por mes")
plt.show()
