# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 08:31:57 2018

@author: Tiago Ibacache
"""
archivo = open("ListaDeTelefono.txt", "w")
archivo.write("blablablablablablaja\n")
archivo.write("sisi")
deps=[]
for i in range (3):
    dep = input("Dep")
    deps.append(dep)
    archivo.write('deps=%s'%deps)
    archivo.close()

"""
import pandas as pd 
ruta = pd.read_csv ('ArchivoLista.csv', header =  0)

print(ruta)
"""