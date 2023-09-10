#Las listas son estructuras de datos lineales
#Se crean usando brackes ej: my_list[]
#Las listas son ordenadas (orden de insersion), esto quiere decir que el último dato ingresado ocuparála ultima posicion
#Emplea métodos para manipular los items de la misma
#Colo los array la primera posiicon inicia en 0
#Permite items duplicados
#Las listas son mutables, es decir podemos agregar, actulizar o remover items
#Puede contener distintos tipo s de datos

nombres=["Pepito","Andres","Juan","Maria","Pedro"]
edades=[25,19,21,33,40]
estaturas=[1.80,1.65,1.74,1.66,1.54]
casados=[False, False, False, True, True]
usuario=["Pepito",25,1.80,False]

print(len(nombres))
print (nombres[0],edades[0],estaturas[0],casados[0])

print (type(nombres))
print (type(edades))
print (type(estaturas))
print (type(casados))
print (type(usuario))

#Slice---Rangos en la lista

print(usuario[0:3])

print(nombres[1:3])
print(nombres[2:4])
print(nombres[:3])
print(nombres[1:])
print(nombres[:-1])
print(nombres[:4])
print(nombres[-4:-1])
print(nombres[1:4])

#Podemos validar si existe en la lista algun elemento 
#print("ingrese el nombre")
#variable=input()
variable="Maria"
if variable in nombres:
    print("el nombre esta en la lista")
else:
    print("el nombre no esta en la lista")    
    
#Reemplazar un elemento de la lista

usuario[0]="Luis"    
print(usuario[0])

nombres[0:3]="Luis","Pablo","Pipe"
print(nombres[0:])

#Queremos insertar un item en una posición especifica=>insert(i,value)

nombres.insert(0,"Pepito")
print(nombres[0:])

#Podemos agregar con el metodo append() items pero este se agrega al final de la lista
nombres.append("Laura")
print(nombres[0:])

nombres2=["Lis","Ana"]

nombres.extend(nombres2)
print(nombres[0:])

nombres.remove("Pipe")
print(nombres[0:])
nombres.remove("Lis")
print(nombres[0:])

nombres.pop(4)
print(nombres[0:])

#limpiara la lista, pero no la elimina

#nombres.clear()
#print(nombres[0:])

#del nombres
#print(nombres[0:1])

#Recorriendo listas
print("------------")
for i in edades:
    print(i)

#Iterar los index
print("------------")
for i in range(len(estaturas)):
    print(estaturas[i])


#Iterar la lista usando while
print("------------")
i=0

while i<len(usuario):
    print(usuario[i])
    i+=1
    
#list comprehension

print("------------")
[print(x)for x in usuario] 

print("------------")
for i,edad in enumerate(edades):
    print(i,edad)
    
   #Tarea: ingresos y egresos, en listas separadas y al final vaya mostrando el saldo a medida que vamos ingresando o retirando dinero debe mostrar el saldo, y el saldo no puede quedar negativo    
   
    