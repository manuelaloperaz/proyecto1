import random

vidas=5
puntos=0



while (vidas !=0):

    num=random.randint(0,9)
    
    if num==0:
        vidas-=1
        print(f"vidas:{vidas}")
    else:
        puntos+=1   
        print(f"puntos:{puntos}") 

       #tener dos variables, dos input en uno se recibe las compras y en otro las cuotas, y de imprimirle al cliente el plan de pago mostrando cuanto va bajando el credito y cuanto tiene de cupo


print("Valor de la compra")
compra=int(input())

print ("Número de cuotas")
cuotas=int(input())
contador=1
deuda=compra
print("*******PLAN DE PAGO*******\n")

while (contador<=cuotas):
        
    valor=compra/cuotas
    print("cuota---->"+str(contador)+"="+str(valor))
    contador+=1
    deuda=deuda-valor
    cupo=compra-deuda
    print ("El valor de la deuda es: "+str(deuda))
    print ("El valor del cupo es: "+str(cupo)+"\n")
    if (deuda==0):
        print("Ha terminado de pagar la deuda\n")
        



