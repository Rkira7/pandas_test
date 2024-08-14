import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/List_of_2018_box_office_number-one_films_in_France"
peticion = requests.get(url)
datos = pd.read_html(StringIO(peticion.text))
#print(datos)
dataframe = datos[0]

#5 elementos
print(dataframe.head())

#informacion de las columnas
print(dataframe.info())
#Eliminar caracteres
dataframe["Gross"] = dataframe["Gross"].str.replace("US$","").str.replace(",","")
print(dataframe.head())

#Cambiar el tipo de la columna a int
dataframe["Gross"] = dataframe["Gross"].astype("int64")

#Cambiar el tipo de a columna a datetime
dataframe["Date"] = dataframe["Date"].astype("datetime64[s]")

#Agregar la columna Month con el mes de la columna Date
dataframe["Month"] = pd.DatetimeIndex(dataframe["Date"]).month

#Eliminar columnas # y Note
dataframe.drop(["#", "Notes"], axis=1, inplace=True)

df_1 = dataframe[["Film", "Gross"]].sort_values(ascending=False, by="Gross")

#Grafica
plt.figure(figsize=(10,6))
plt.bar(df_1["Film"].head(), df_1["Gross"].head(), color=["orange", "pink", "red", "yellow", "blue"])
plt.title("Top 5 Peliculas por ingresos")
plt.ylabel("Ingresos")
plt.xlabel("Peliculas")
plt.xticks(rotation=5)
plt.show()

#Grafica pie
plt.figure(figsize=(10,6))
plt.pie(df_1["Gross"].head(10), labels=df_1["Film"].head(10), autopct="%0.2f%%")
plt.show()

#Media de ingresos
df_2 = dataframe.groupby("Month")["Gross"].mean()
plt.figure(figsize=(10,6))
plt.plot(df_2)
plt.title("Media de ingresos por mes")
plt.ylabel("Mes")
plt.xlabel("Ingresos")
plt.show()