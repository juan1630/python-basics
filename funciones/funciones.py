


def saludar():
    print('Hola')

saludar()

#funciones con parametros

def saludar_a(user):
    print(f'Hola {user}')


saludar_a('Jose')

#al paremetro es el valor que recibe la funcion
# el argumento es el valor que se la pasa al ser ejecutada



def sumar(a,b):
    sum = a+b
    return sum

print(sumar(3,5))


def restar(a,b):
    """ Resta dos numeros y devuelve el resultado  """
    #Documentamos la funcion usando el docstring
    resta = a-b
    return  resta

print(restar(8,3))


print(restar.__doc__)



help(restar)


#paramentros por defecto

def multiplicar(a,b =2):
    return a*b

#El valor es opcional
print(multiplicar(2))

print(multiplicar(2,3))

#Argumentos  por clave


#parametros por posicion
def describir_persona(nombre, edad , sexo):
    print(f'Hola Soy {nombre} y tengo {edad} y soy {sexo} ')

describir_persona('Juan', '30', 'Hombre')
describir_persona( 'Hombre', 30, 'Juan')

#parametros nombrados
describir_persona( nombre='Juan', sexo='Hombre', edad=30 )