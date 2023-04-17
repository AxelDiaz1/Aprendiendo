'''numero = int(input("Ingrese un numero"))
resto = numero%2
if resto == 0 and numero > 10:
    print("El numero es par")
else:
    print("El numero es impar")
print("FIN")


#EJEMPLO 
print("Bienvenido a mi programa")
url=input("Ingrese un url:")
if url.startswith("https"):
    print("Es una pagina web segura")
else:
    print("La pagina web no es segura")
print("Fin del programa")'''



'''
Adulto: Si la edad es mayor igual a 18
Adolecente: Si la edad es mayor igual a 12 y menor a 18
Niño: si la edad es mayor igual a 6 y menor a 12
Bebe: Si la edad es menor a 6
'''

edad =int(input("Ingrese su edad: "))
if edad >= 18:
    print("Adulto")
elif edad >= 12 :
    print("Adolecente")
elif edad >= 6 :
    print("Niño")
elif edad < 6:
    print("Es bebe")