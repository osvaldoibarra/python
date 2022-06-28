'''
Created on 13 jun 2022

@author: osvaldo.hernandez
'''
print("Base de datos alumnos")
"""fichero=open("alumnos.txt", "a")

print("Cuantos alumnos desea agregar? ")
num=int(input())
aux=0
while aux<num:
    print("Nombre:")
    nombre=input()
    print("Matricula:")
    matricula=input()
    print("Carrera:")
    carrera=input()
    print("Promedio:")    
    promedio=float(input())
    
    cadena=str(nombre)+"; "+str(matricula)+"; "+str(promedio)+"; "+str(carrera)+"\n"
    aux +=1
    fichero.write(cadena)
fichero.close()"""

def aprobados():
    x=[]
    fichero=open("C:/Users/osvaldo.hernandez/eclipse-workspace/python/Archivos/Archivos/alumnos.txt", "r")
    fichero2=open("C:/Users/osvaldo.hernandez/eclipse-workspace/python/Archivos/Archivos/alumnos_aprobados.txt","w")
    fichero3=open("C:/Users/osvaldo.hernandez/eclipse-workspace/python/Archivos/Archivos/alumnos_reprobados.txt","w")
    
    lista=fichero.readlines()
    #print(lista)
    fichero.close()
    aux1=0
    while aux1<len(lista):
        txt=lista[aux1]
        x=txt.split("; ")
        print(x)
        prom=float(x[2])
        if prom>=6:
            fichero2.write(txt)
        else:
            fichero3.write(txt)
        aux1 +=1 
    fichero2.close()
    fichero3.close()

aprobados()

print("\nAlumnos aprobados")
fichero4=open("C:/Users/osvaldo.hernandez/eclipse-workspace/python/Archivos/Archivos/alumnos_aprobados.txt","r")
linea=fichero4.readline()
while linea != "":
    print(linea)
    linea=fichero4.readline()
fichero4.close()
print("Alumnos reprobados")
fichero5=open("C:/Users/osvaldo.hernandez/eclipse-workspace/python/Archivos/Archivos/alumnos_reprobados.txt","r")
linea2=fichero5.readline()
while linea2 != "":
    print(linea2)
    linea2=fichero5.readline()
fichero5.close()
