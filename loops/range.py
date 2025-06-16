#permite crear una secuencia o rango de numeros puede ser util para el for

print('\n range:')
#range(0,10)
nums = range(10)
#range no crea una lista, puede aceptar un parametro para inicializar desde donde a donde queremos el rango range(0,5)  range(3,6)
#por defecto inicia en el 0 si solo se pone un solo numero
#crea el rango bajo demanda

for num in nums:
    print(num)

for num in range(5, 15):
    print(num)

#el tercer parametro es el step, crea el rango pero deja el step o brinco
#range(inicio, fin, paso)
for num in range(0, 10, 2):
    print(num)

#numero negativos
for num in range(-5, 0):
    print(num)

#decrementando, una cuenta regresiva
for num in range(10, 0, -1):
    print(num)

nums = range(0, 10)
list_of_nums = list(nums)

print(list_of_nums)
