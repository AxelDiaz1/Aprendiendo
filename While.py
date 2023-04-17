''' x = 0
 while x < 10:
     print("El valor de x es:", x)
     x += 1'''
    
'''numero = int(input("Ingresa un numero positivo"))
while numero <0:
    print("Error, ingrese un numero positivo")
    numero = int(input("Ingresa un numero positivo"))
print("El numero es ", numero)'''

#EJEMPLO DE MENU
num = int(input("Menu: 1(ver numeros), 0(salir)"))
while num != 0:
    x = 0
    while x < 10:
        print("El valor de x es" , x)
        x += 1
        
    print("Saliendo...")
    num = int(input("Menu: 1(ver numeros), 0(salir)"))

print ("GRACIAS")