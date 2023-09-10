age=18
height=151
tipousuario="visitante"

#if simple
if age>=17 and height>=150:
   print ("si puedes ingresar a la atracción")

if age>=13 or height>=150:
   print ("si puedes ingresar")

   #if-else
if tipousuario=="estudiante":
   print ("Permite el ingreso")
else:
   print ("Registre su visita")

   #ejercicio

print("Desea hacer el pago? si/no")
pago=input()

if pago=="si":
   print("Cuál es el valor a pagar?")
   valorpago=int(input())
   print("Desea incluir el servicio? si/no")
   servicio=input()
   if servicio=="si":
     totalpago=valorpago*1.1
     print("El valor total a pagar es--->$"+str(totalpago))
   print("El valor a pagar es--->$"+str(valorpago)) 
else: print("Desea hacer otro servicio?")   

#implementar un login, con un registro, que es login permita validar si la persona agregue el telefono o el email que sea valido y que ingrese la contraseña y validar un capchat(5*2+(3**2)), si se cumple debe decir bienvenido, y si no validar credenciales

print ("-----------REGISTRO---------")

print("telefono------->")
telefono=int(input())
print ("correo-------->")
correo=str(input())
print ("contraseña---->")
contrasena=str(input())
capchat=int(16)

print ("--------LOGIN--------")

print("telefono------->")
telefono1=int(input())
print ("correo-------->")
correo1=str(input())
print ("contraseña---->")
contrasena1=str(input())
print ("Resuelva lo siguient (10*2-4)")
capchat1=int(input())

if telefono==telefono1 or correo==correo1 and contrasena==contrasena1 and capchat==capchat1 :
   print("Bienvenido al sistema de registro")
else: print ("Revise los datos")   
