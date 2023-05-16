#Cómo hacer una tabla de frecuencias para variables categóricas
#con datos importados de excel
#author: Alejandra Santos Coz

# importar pandas para la lectura de datos
import pandas as pd 

# leer base de datos y guardarla en variable db (database)
db = pd.read_excel('./Basededatos2023.xlsx')

#Seleccionar una catrgoría y almacenarla en una variable
frec_crr = pd.value_counts(db["Carrera"])
#Almacenamos frecuencia en un dataframe
frec_df = pd.DataFrame(frec_crr)
#Asignamos nombre de columna
frec_df.columns = ["fi"]

#Creamos la columna de frec. rlativa yrealizamos las operaciones numéricas para calcularla
frec_df["hi %"] = 100*frec_df["fi"]/len(db)

