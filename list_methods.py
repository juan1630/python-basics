import os

os.system('cls')

lista1 = [1,2,3,4]

#agregar un elemento a la lista

lista1.append(5)


print(lista1)

#inserta un elemento en la posicion en la que le indiquemos en el primer parametro y empuja los demas elementos a la siguiente posicion
lista1.insert(1, 20)

print(lista1)

##agrega elementos al final de la lista
lista1.extend([5,6,7,8])

print(lista1)

#Eliinar elementos de la lista
#Remove elimina la primera aparicion de un elemento en la lista

lista1.remove(5)

print(lista1)


lista1.pop() #elimina el ultimo elemento de la lista y te devuelve el elemento elimnado
# tambien se le puede pasar el indice del elemento a eliinar

lista1.pop(0)
del lista1[-1]

#Eliminar un rango de elementos
del lista1[1:2]
print(lista1)

#eliminar todos los elementos de la lista

lista1.clear()
print(lista1)

#ordenar listas
numbers = [1,4,2,3,7]

numbers.sort() #modifica la lista original
sorted_nums = sorted(numbers) #crear una copia ordenanda, funciona para strings pero ordena primero las mayusculas


print(numbers)
print(sorted_nums)


animals = ['perro', 'gato', 'oso', 'perro']

#cuenta cuantas veces aparece el animal en la lista
print(animals.count('perro'))

#Comprueba si el animal aparece en la lista
print( 'gato' in animals)
