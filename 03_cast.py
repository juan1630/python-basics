# 03-casting de types
# transformar un tipo de número a otro
# python no hace la conserción de tipado automatica ya que es de tipado fuerte


print("Casting de tipos")

print(type(int('100')))

#print( 2 + '100')
print(2 + int('100')) # de esta forma se puede hacer la suma, de un strig + un int
print( int('100') + 2 )


print(bool(3))
print((bool(0))) # el unico número con valor falsy es el 0
print(bool(-1))  # imprime True


print(bool("")) # false
print(bool(" ")) # true
print(bool("False"))


print(int(2.5)) # 2 -> no hace el redondeo