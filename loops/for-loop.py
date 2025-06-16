#permite ejecutar un bloque de codigo repetidamente  mientras itera un iterble

# diferencia del bucle while que recibe una condicion de salida, el bucle for iteramos sobre algo

print('\n For loop')


frutas = ['manzana', 'pera', 'sandia', 'durazno']

#iteramos la lista de frutas

for fruta in frutas:
    print(fruta)


#hay varios tipos de iterables que se pueden iterar con el for loop, en este caso los strings tambien son iterables

name = 'Juan'

for character in name:
    print(character)

#para acceder al index de los elementos se usa la funcion enumerate
#al usar el enumerate siempre regresa en la primera posicion el indice y en la segunda el valor
for index, fruta in enumerate(frutas):
    print( f' {fruta} en la posicion {index} ')

#Bucles anidados

letras = ['A','B','C','S']
numeros = [1,2,3,4,]


for letra in letras:
    for numero in numeros:
        print( f'{letra}{numero}' )

#break


animales = ['loro', 'canario',  'pez', 'perro', 'raton']
for idx,animal in enumerate(animales):
    if animal == 'perro':
        print(f'El perro esta escondido en el idice: {idx}' )
        break

#continue
print('\n Continue')
for idx,animal in enumerate(animales):
    if animal == 'perro': continue
        #continue
        #salta la vuelta del perro
    print(animal)


#Compresion de listas
animales = ['loro', 'canario',  'pez', 'perro', 'raton']
animales_mayus = [animal.upper() for animal in animales]

print(animales_mayus)

#muestra los numero pares de una lista

print('\n numeros enteros ejercicio')
numero_enteros = [1,2,3,4,5,6,7,8]

for numero in numero_enteros:
    if numero % 2 == 0:
        print(numero)

numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares)