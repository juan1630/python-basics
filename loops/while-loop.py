#permite ejecutar un bloque de condigo de forma repetida


print('\n While loop ')


count = 0


#while count <= 5:
#    print(count)
#    count+=1

print('Fin del while')

#la palabra break es uan forma de salir de un bucle una vez se haya cumplido una condicion

#while True:
#    print(count)
#    count += 1
#    if count ==5:
#        break # sale del bucle al cumplir la condicion


while count <= 100:
    print(count)
    count += 1
    if count % 5 == 0:
        print('El numero es divisible entre', count)
        break

print('\n Palabra continue')
#lo que hace es saltar la iteracion y continua con el bucle



contador =0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)


print('\n Bucle while con else')

contador = 0

while contador < 5:
    print(contador)
    contador += 1
else:
    # es util cuando te quieres asegurar que se ha cumplido la condicion, si se agrega el break entonces nunca pasara al else
    print('El bucle while ha terminado...')


numero = -1

#while numero < 0:
#    numero = int(input('Ingresa un numero positivo...'))
#    if numero < 0:
#       print('Ingresa un numero mayor')

#print(f'El numero que ingresaste es {numero}')



while numero < 0:
    try:
        numero = int(input('Ingresa un numero positivo...'))
        if numero < 0:
            print('Ingresa un numero mayor')
    except:
        print('el dato ingresado debe de ser un numero')

print(f'El numero que ingresaste es {numero}')