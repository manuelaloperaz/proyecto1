import sys

ingresos=[]
egresos=[]
menu=1

while(menu==1):

 print("Ingrese la opcion que desea realiza")
 print("*****Menú****")
 print("opción 1------>Consignar")
 print("opción 2------>Retirar")

 opcion = int(input())
 

 if opcion==1:
     print("valor a consignar")
     ingresos.append(input())
     print(ingresos[0:])
     print("Desea volver al menú principal? si/no")
     volver = input()
     if volver == "si":
        menu = 1  
     else:
        print("Hasta luego")
        sys.exit()
    
if opcion==2:
    print("valor a retirar")
    egresos.append(input())
    print(egresos[0:])
        