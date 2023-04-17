'''
Imprimir TRUE si la edad de Axel es par
y no es mayor a 24
'''
edad = 22
condicion1 = edad%2 == 0
condicion2 = not(edad>24)
print(condicion1 and condicion2)