import math
from tkinter import*
from math import *
import matplotlib.pyplot as plt
import scipy.stats as stats 
from scipy.stats import norm
from matplotlib_venn import venn2,venn2_circles
import numpy as np
import operator
from functools import reduce

while True:
    print("MENU PRINCIPAL")
    print("1-ESTADISTICA")
    print("2-PROBABILIDAD")
    opc = input("SELECCIONA UNA OPCION: ")
    print("")
    print("")
    if opc == "1":


        Cantidad_datos = int(input("Ingresa la cantidad de datos: \n"))
        datos=[]
        print("Ingresa los", Cantidad_datos, "datos")
        for i in range(Cantidad_datos):
            valor = float(input(f"Dato {i}: "))
            datos.append(valor)

        print(datos)
        resultado = log(Cantidad_datos,10)
        #print(resultado)
        clase = 1 + 3.322*resultado
        clase = round(clase)
        print("Tienes un total de: ",clase," clases.")

        def mayor_de_arreglo(datos):
            mayor = datos[0]
            for elemento in datos:
                if elemento > mayor:
                    mayor = elemento
            return mayor 
        def menor_de_arreglo(datos):
            menor = datos[0]
            for elemento in datos:
                if elemento < menor:
                    menor = elemento
            return menor
        mayor = float(mayor_de_arreglo(datos))
        menor = float(menor_de_arreglo(datos))

        datos.sort()
        print(datos)
        print(f"Elemento mayor es: {mayor} \n El elemento menor es: {menor}") 
        rango = (mayor - menor)
        print(f"El rango es de: {rango}")
        amplitud = rango/clase
        print(f"La Amplitud es de: {amplitud}")

        def Tabla():
            aux = menor
            contador=0
            fi_acum=0
            Limite_inf=[]
            acumular_xi=[]
            acumulativa=[]
            for i in range(clase):
                if i>=1:
                    aux = aux+amplitud
                    aux_lim_sup = aux+ amplitud
                    xi= (aux+aux_lim_sup)/2
                    print(f"Clase   | Lim. Inferior   |Lim. Superio     |XI ")
                    print(f"   {i+1}    |  {aux+1}    | {aux_lim_sup}  |{xi}")
                    acumular_xi.append(xi)
                    print(acumular_xi)
                    for j in range(len(datos)):
                        Var=float(datos[j])
                        if(Var > aux and Var <= aux_lim_sup):
                            Limite_inf.append(Var)
                            acumular_xi.append(Var)
                    contador=contador + len(Limite_inf)
                    acumulativa.append(contador)
                    print(f"La Frecuencia absoluta fi es de: {len(Limite_inf)}")
                    print(f"La frecuencia absoluta acumulada Fi es de {contador}")
                    fi=(len(Limite_inf)*100)/Cantidad_datos
                    print(f"La frecuencia Relativa fr es de {fi}%")
                    fi_acum=fi_acum+fi
                    print(f"La frecuencia Relativa acumulada Fr es de {fi_acum}%")
                    print(acumulativa)
                    print("----------------------------------------------------------------")
                    plt.title ("Histograma")
                    plt.hist (Limite_inf, color="yellow", ec = "black")
                    plt.show()
                    plt.title ("Ojiva")
                    plt.plot(acumulativa)
                    plt.show()
                    
                   
                else:
                    lim_sup=aux+amplitud
                    xi= (aux+lim_sup)/2
                    print(f"Clase       | Lim. Inferior         |Lim. Superio              |XI ")
                    print(f"   {i+1}    |  {menor}              | {lim_sup}                 |{xi}")
                    acumular_xi.append(xi)
                    print(acumular_xi)
                    for j in range(len(datos)):
                        Var=float(datos[j])
                        if(Var >=menor and Var <= lim_sup):
                            Limite_inf.append(Var)
                            acumular_xi.append(Var)
                    contador=len(Limite_inf)
                    acumulativa.append(contador)
                    print(f"La Frecuencia absoluta fi es de: {len(Limite_inf)}")
                    print(f"La frecuencia absoluta acumulada Fi es de {contador}")
                    fi=(len(Limite_inf)*100)/Cantidad_datos
                    print(f"La frecuencia Relativa fi es de {fi}%")
                    fi_acum = fi_acum+fi
                    print(f"La frecuencia Relativa acumulada fi es de {fi_acum}%")            
                    print("----------------------------------------------------------------")
                    

            return aux

        def Frecuencia_abs():
            aux = menor
            contador=0
            for i in range(len(datos)):
                aux = aux+amplitud
                aux_lim_sup = aux+ amplitud
                Dato = datos[i]
                if(Dato>= aux and Dato <= aux_lim_sup):
                    contador=+ 1
            print(f"Total de Fi en clase 1 {contador}")
            return contador 


        Tabla()
    elif opc == "2":
        while True:
            print("")
            print("")
            print("BIENVENIDO AL APARTADO DE PROBABILIDAD")
            print("1-CONJUNTOS")
            print("2-DISTRIBUCION NORMAL")
            print("3-PERMUTACION")
            print("4-COMBINACION")
            opcion = input("SELECCIONA UNA OPCION: ")

            if opcion == "1":
                #conjuntoA=[4,5,6,7]
                #conjuntoB=[6,7,8,9]

                datos_A = int(input("Ingresa la cantidad de datos para el conjunto A: \n"))
                conjuntoA=[]
                print("Ingresa los", datos_A, "datos para el conjuntoA ")
                for i in range(datos_A):
                     valores = float(input(f"Dato {i}: "))
                     conjuntoA.append(valores)

                datos_B = int(input("Ingresa la cantidad de datos para el conjunto B: \n"))
                conjuntoB=[]
                print("Ingresa los", datos_B, "datos para el conjuntoB ")
                for i in range(datos_B):
                     valores1 = float(input(f"Dato {i}: "))
                     conjuntoB.append(valores1)

                A=set(conjuntoA)
                B=set(conjuntoB)

                union = A | B
                diferenciaAmenosB = A-B
                diferenciaBmenosA = B-A
                interseccion = A & B

                print("la union de los conjuntos es: ",union)
                print("la diferencia del conjunto A - conjunto B es: ",diferenciaAmenosB)
                print("la diferencia del conjunto B - conjunto A es: ",diferenciaBmenosA)
                print("la interseccion de los conjuntos es:  ",interseccion)



            elif opcion =="2":
                    while True:
                        print("")
                        print("")
                        print("opciones a encontrar")
                        print("1- area < x")
                        print("2- area > x")
                        print("3- area entre dos puntos \n")
                        opciones = int(input("selecciona una opcion: "))

                        if opciones == 1 or opciones == 2:
                            x=float(input("ingresa el valor de x: "))
                            media =float(input("ingresa el valor de la media: "))
                            des = float(input("ingresa la desviacion estandar: "))
                            proba= stats.norm.cdf((x-media)/des)
                            z = (x-media)/des
                            print("su valor z es: ", round(z,4))
                            if opciones == 1:
                                print('su probabilidad fue calculada en: {:.2f}%'.format(proba * 100))
                                x1= np.arange(z,0.0001)
                                x2 = np.arange(-10,10,0.0001)
                                y= norm.pdf(x1,0,1)
                                y2 = norm.pdf(x2,0,1)
                                fig,ax=plt.subplots(figsize=(9,6))
                                plt.style.use("fivethirtyeight")
                                ax.plot(x2,y2)
                                ax.fill_between(x1,y,0,color="g")
                                ax.fill_between(x2,y2,alpha=0.1)
                                ax.set_xlim([-4,4])
                                plt.show()

                            if opciones == 2:
                                resu = 1- proba
                                print('su probabilidad fue calculada en: {:.2f}%'.format(resu * 100))
                                x1= np.arange(z,0.0001)
                                x2 = np.arange(-10,10,0.0001)
                                y= norm.pdf(x1,0,1)
                                y2 = norm.pdf(x2,0,1)
                                fig,ax=plt.subplots(figsize=(9,6))
                                plt.style.use("fivethirtyeight")
                                ax.plot(x2,y2)
                                ax.fill_between(x1,y,0,color="g")
                                ax.fill_between(x2,y2,alpha=0.1)
                                ax.set_title("campana de Gauss")
                                ax.set_xlim([-4,4])
                                plt.show()

                        if opciones == 3:
                            mu = float(input("ingresa el valor de la media: "))
                            desviacion = float(input("ingresa el valor de la desviacion estandar: "))
                            x1 = float(input("ingresa el valor de x1: "))
                            x2= float(input("ingresa el valor de x2: "))
                            proba1= stats.norm.cdf((x1-mu)/desviacion)
                            proba2= stats.norm.cdf((x2-mu)/desviacion)
                            z1 = (x1 - mu)/desviacion
                            z2 = (x2 - mu)/desviacion
                            sum = proba1 + proba2
                            print("su valor Z1 es: ", round(z1,4))
                            print("su valor Z2 es: ", round(z2,4))
                            print('su probabilidad fue calculada en: {:.2f}%'.format(proba1 * 100))
                            print('su probabilidad fue calculada en: {:.2f}%'.format(proba2 * 100))
                            print ("el valor de Z es: ",sum)

                            x1= np.arange(z1,z2,0.0001)
                            x2 = np.arange(-10,10,0.0001)
                            y= norm.pdf(x1,0,1)
                            y2 = norm.pdf(x2,0,1)
                            fig,ax=plt.subplots(figsize=(9,6))
                            plt.style.use("fivethirtyeight")
                            ax.plot(x2,y2)
                            ax.fill_between(x1,y,0,color="g")
                            ax.fill_between(x2,y2,alpha=0.1)
                            ax.set_xlim([-4,4])
                            plt.show()
                             



            elif opcion == "3":
                n = int(input("ingresa cuanto vale N: "))
                r = int(input("ingresa cuanto vale R: "))
                q = int(input("ingresa cuanto vale Q: "))

                def numero_combinaciones(n,r,q):
                    if n < r:
                        return 0
                    else:
                        comb = math.factorial(n) / (math.factorial(q) * math.factorial(r))
                        return comb

                print(numero_combinaciones(n,r,q))


            elif opcion =="4":
                n = int(input("ingresa cuanto vale N: "))
                r = int(input("ingresa cuanto vale R: "))

                def numero_combinaciones(n,r):
                    if n < r:
                        return 0
                    else:
                        comb = math.factorial(n) / (math.factorial(n-r) * math.factorial(r))
                        return comb

                print(numero_combinaciones(n,r))

