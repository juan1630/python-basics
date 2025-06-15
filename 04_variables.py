#04 - variables
# Las variables sriven para guaradr datos en memoria

my_name = 'Juan'

print(my_name)

#Tipado dinamico, el tipo de dato se determina en tiempo de ejecución
age = 32
print(age)

age = 29

print(age)

#Python no se conversiones de datos de forma automatica, ya que es de tipado fuerte

#Formated string Literals
print(f"Hola {my_name}, mi edad es: {age} ")


#no recomendado
name, age, city = 'juan' , 29, 'CDMX'

#Convseciones de variables
mi_nombre_de_variable = 'ok'
nombre =  'ok'

miNombreDeVariable = 'ko'
minombredevariable = 'ko'

mi_nombre_de_variable_123= 'ok'


#python no tiene constantes, se pueden simular pero no las tiene



MI_CONSTANTE = 'HOLA'


MI_CONSTANTE = 20


print(MI_CONSTANTE)



# no se puede usar

#nombres no validos
# 123variable = 'ko'
# mi-variable = 'ko'
# mi variable = 'ko'
# no usar las palabras reservadas como nombre de variables




#types anotation, solo se hace una anotación del tipo de dato de la variable
is_user_logged_in: bool = True
print(is_user_logged_in)


is_user_logged_in = 42
print(is_user_logged_in)


