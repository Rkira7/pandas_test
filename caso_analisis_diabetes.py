import pandas as pd

#Crear el dataset a partir del archivo csv
df_completo = pd.read_csv('/datasets/diabetes.csv')
df_completo.head();
texto = 'Completo DataSet'; print('-'*15, texto, '-'*15)
print(df_completo)
texto = 'Cantidad de valores Metodo LEN'; print('-'*15, texto, '-'*15)
print(len(df_completo))
texto = 'Cantidad de valores Metodo COUNT Resultado'; print('-'*15, texto, '-'*15)
print(df_completo['Resultado'].count())

#Definir columnas de dataframe
texto = 'Columnas'; print('-'*15, texto, '-'*15)
columnas = df_completo.columns
print(columnas)

#Imprimir glucosa
texto = 'Glucosa'; print('-'*15, texto, '-'*15)
print(df_completo.Glucosa)
#print(df_completo['Glucosa'])

#Personas con diabetes y sin diabetes
texto = 'Con y sin diabetes'; print('-'*15, texto, '-'*15)
print(df_completo['Resultado'].value_counts())

#10 personas con mayor incide de masa corporal
texto = 'mator indice masa corporal'; print('-'*15, texto, '-'*15)
print(df_completo.BMI.sort_values(ascending=False).head(10))

#Edades con diabetes
texto = 'Candidad de Edades con diabetes'; print('-'*15, texto, '-'*15)
cantidad_personas_p =  df_completo.Edad.where(df_completo['Resultado'] == 1).dropna().value_counts()
cantidad_personas_p = pd.DataFrame({
    'Edad' : cantidad_personas_p.index ,
    'Cantidad' : cantidad_personas_p.values
})
print(cantidad_personas_p)


#Edades sin diabetes
texto = 'Candidad de Edades sin diabetes'; print('-'*15, texto, '-'*15)
cantidad_personas_n =  df_completo.Edad.where(df_completo['Resultado'] == 0).dropna().value_counts()
cantidad_personas_n = pd.DataFrame({
    'Edad' : cantidad_personas_n.index ,
    'Cantidad' : cantidad_personas_n.values
})
print(cantidad_personas_n)