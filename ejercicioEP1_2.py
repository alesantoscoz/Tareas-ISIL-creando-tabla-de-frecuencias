# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:44:36 2023

@author: Ale
"""

#Cómo hacer una tabla de frecuencias para variables numéricas discretas
#con datos importados de excel
#author: Alejandra Santos Coz

# importar pandas para la lectura de datos
import pandas as pd 

# leer base de datos y guardarla en variable db (database)
db = pd.read_excel('./Basededatos2023.xlsx')

#Seleccionar almacenarla en variable
frec_nroh = pd.value_counts(db["Número de hermanos"])
#Almacenamos frecuencia en un dataframe
frec_df = pd.DataFrame(frec_nroh)
#Asignamos nombre de columna
frec_df.columns = ["fi"]

#Creamos la columna de frec. rlativa y realizamos las operaciones numéricas para calcularla
frec_df["hi %"] = 100*frec_df["fi"]/len(db)

#Obtenemos las frecuencias acumuladas
#guardamos los valores en una variable
fi_val = frec_df["fi"].values

#creamos array vacío para acumular
acum = []
acum_val = 0 #le damos un valo inicial de 0

#creamos un ciclo for para sumar los valores y acumularlos
for i in fi_val:
    acum_val = acum_val + i
    acum.append(acum_val)

#Creamos la columna Fi con los valores acumulados
frec_df["Fi"] = acum

#Lo mismo aplicamos para acumular frec. relativas
acum_hi = []
acumhi_val = 0 #le damos un valo inicial de 0
hi_val = frec_df["hi %"].values
for i in hi_val:
    acumhi_val = acumhi_val + i
    acum_hi.append(acumhi_val)

frec_df["Hi %"] = acum_hi