'''
Comparar si el ultimo numero de la variable num1
es diferente al ultimo numero de la variable num2
imprimir TRUE si son diferentes, FALSE en caso contrario.
'''
num1 = 56
num2 = 67

ultimo1 = num1%10
ultimo2 = num2%10

comparar1 = ultimo1 != ultimo2

print(comparar1)
