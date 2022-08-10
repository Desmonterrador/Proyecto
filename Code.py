import math
from tkinter import *
from math import *
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib_venn import venn2, venn2_circles
import numpy as np
import operator
from functools import reduce

ndatos = int(input("Ingresa la cantidad de datos: "))
ndatos1 = []
for i in range(ndatos):
    valor = float(input(f"Dato {i}: "))
    ndatos1.append(valor)

    print(ndatos1)
    k = log(ndatos,10)
    clase = 1 + 3.322 * k
    clase = round(clase)
    print("El numero de clases es: ",clase)
    
    def nmayor(ndatos1):
        mayor = ndatos1[0]
        for n1 in ndatos1:
            if n1 < mayor:
                mayor = n1
        return mayor 
    def nmenor(ndatos1):
        menor = ndatos1[0]
        for n1 in ndatos1:
            if n1 < menor:
                menor = n1
        return menor
    
    mayor = float(nmayor(ndatos1))
    menor = float(nmenor(ndatos1))

    ndatos1.sort()
    print(ndatos1)
    rango = (mayor - menor)
    print(f"El rango es de: {rango}")
    amplitud = rango / clase
    print(f"La amplitud es de: {amplitud}")

    def tabla():
        aux = menor
        con = 0
        fiAcum = 0
        Li = []
        xiAcum = []
        acum = []
        for i in range(clase):
            if i >= 1:
                aux = aux + amplitud
                auxLs = aux + amplitud
                xi = (aux + auxLs) / 2
                print(f"Clase   | Lim Inf   |Lim Sup    |XI ")
                print(f"    {i+1}   |   {aux+1}     | {auxLs}   |{xi}")
                xiAcum.append(xi)
                print(xiAcum)
                for j in range(len(ndatos1)):
                    v1 = float(ndatos1[j])
                    if(v1 > aux and v1 <= auxLs):
                        Ls.append(v1)
                        xiAcum.append(v1)
                con = con + len(Li)
                acum.append(con)
                print(f"La frecuencia fi es: {len(Li)}")
                print(f"La frecuencia acumulada FI es:  {con}")
                fi=(len(Li)*100)/ndatos
                print(f"La frecuencia relativa fr es: {fi}%")
                fiAcum = fiAcum + fi
                print(f"La frecuencia relaiva acumulada Fr es: {fiAcum}%")
                print(acum)
                print("##############################################################################")
                plt.title("Ojiva")
                plt.plot(acum)
                plt.show()
                plt.title("Histograma")
                plt.hist(Li, color="Red", ec = "black")
                plt.show()
            else:
                Ls = aux + amplitud
                xi = (aux + Ls) / 2
                print(f"Clase       | Lim Inf      |Lim Sup     |XI  ")
                print(f"    {i+1}   |  {menor}     |   {Ls}     | {xi}")
                xiAcum.append(xi)
                print(xiAcum)
                for j in range(len(ndatos1)):
                    v1 = float(ndatos1[j])
                    if(v1 >= menor and v1 <= Ls):
                        Li.append(v1)
                        xiAcum.append(v1)
                con = len(Li)
                acum.append(con)
                print(f"fi es:  {len(Li)}")
                print(f"Fi es: {con}")
                fi=(len(Li) * 100)/ndatos
                print(f"fr es: {fi}%")
                fiAcum =  fiAcum + fi
                print(f"Fr es: {fiAcum}")
                print("################################################################")
    
        return aux

def fi_funcion():
    aux = menor
    con = 0
    for i in range(len(ndatos1)):
        aux = aux + amplitud
        auxLs = aux + amplitud
        Dato = ndatos1[i]
        if(Dato >= aux and Dato <= auxLs):
            con =+ 1
    print(f"Total de Fi en clase 1 es: {con}")
    return con
tabla()

                    
