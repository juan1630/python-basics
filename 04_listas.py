# Listas
import os

os.system('cls')

lista1 = [1,2,3,4,5]
lista2 = ['manzanas', 'peras', 'melon']

lista3 = [1, True, 'Pera', 'Comer']
lista_de_listas = [[1,2], [3,4], 'calcetin']


print(lista1)
print(lista2)
print(lista3)
print(lista_de_listas)
print(lista2[-1])
print(lista2[-2])

print(lista_de_listas[1][0])
print(lista_de_listas[2])


# Slicing

print(lista1[1:4]) # 2,3,4,
print(lista1[:3]) #1,2,3
print(lista1[3:]) #4,5
print(lista1[:]) #Devulve una copia
#print(lista1[desde: hasta: paso])

# Revertir la lista

#crea una lista desde el inicio de la lista hasta el fin de la lista pasnado por cada 2 numeros
lista4 = [1,2,3,4,5,6,7,8]
print(lista4[::2]) # 1,3,5,7

print(lista4[::-1])

lista1[0] = 20
print( lista1)


#Concatena una lista, de forma menos eficiente
lista1 + [6,7,8]
print(lista1)
#Crea un espacion en memoria, extra

#Concatena una lista de forma mas eficiente

lista1 += [9,10,11,12]
print(lista1)

#modifica el mismo espacio de memoria

#Recuperar la longitud de una lista
print(len(lista1))