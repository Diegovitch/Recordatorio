#1 suma de variables, concepto: simple, solo tienes que hacer tres variables, las 2 son para hacer las operaciones y la otra estara programada para calcular la operación de las variables 
# CantidadInvertidad = 100

# IngresosAnuales = 100

# AnosRecuperación = CantidadInvertidad / IngresosAnuales

# print(AnosRecuperación)

#2 Variable compleja, concepto: Variables que tienes valores enteros sumados por números al usar el codigo "complex", también puedes programar una variable con valor imaginario solo usa el siguiente codigo "complex(x,y)"
# x = 25
# complex(x) = (25 + 0j)

# y = 10

# complex(x,y) = (25 + 10j)

#3 strings = variable normal
# hola = "hola"

#4 strings = variable multiplicada, concepto: al programar una variable que tenga una string y lo multiplicas sera repetido al valor asignado
# holapor5 = hola * 5
# print(holapor5)

#5 Strings = Multilineal
# Variable = """Hola \n soy homero chino"""
# print(variable)

#6 strings = Hacer oraciones, concepto: programas cada strings y los une con la terminal o con la ventana de python
# 'El\"perro\"de Luis'
# print('El\"perro\"de Luis')

#7 strings = sumas:
# '5'+'5'
# print('5'+'5')

#8 strings = multiplica palabras u oraciones por cualquier digito: es lo mispirque la variable multiplicada, solo que sin ninguna variable
# "Hola" * 5
# print("Hola" * 5)

#9 para crear una lista:
# lista = [1, 4, 5]
# type(lista)
# print(lista)

#10 para modificar un elmento de la lista:
# lista[2] = "Yo que se"

#11 para eliminar el ultimo elemento de la lista:
# lista.pop(0)
# print(lista.pop(0))

#12 para recuperar el número de una lista:
# lista[1]
# print(lista[1])

#13 para crear una tupla:
# tupla = (1, 5, 4)
# type(tupla)
# print(tupla)

#14 para cambiar un valor de la tupla
#tuple_matematicas = ("Minimo cmún multiplo", "División", "Multiplicación")
#y = list(tuple_matematicas)
#y[2] = "suma"
#tuple_matematicas = tuple(y)

#15 para insertar un dato en la tupla
#tuple_a = ('a', 'b', 'c')
#tuple_b = ('d', 'e', 'f')
#tuple_c = tuple_a + tuple_b

# 16 Conjuntos, es como una lista, pero en conjunto, pone valores sin orden

# Id_conjunto = { elemento1,elemento2,...,elementoN }
# Id_conjunto = set ([elemento1,elemento2,...,elementoN])
# Id_conjunto = frozenset([elemento1,elemento2,...,elementoN])

    #16.1 ejemplos:

# conjunto = [1,1,45,6]

# conjunto_set = set ([54,342,342,56])
# El codigo set hacer que elimine los valores repetidos

#17 contadores de conjuntos
   #17.1 contadores, este contador diferencia un elemento en el conjunto, si hay sera verdadero si no hay será falso

# conjunto_set = set ([54,342,342,56])
# print(54 in conjunto_set)

   #17.2 contaddores, este mide la longitud del conjunto

# conjunto_set = set ([54,342,342,56])
# len(conjunto_set)

#18 Como añadir un nuevo valor en un conjunto

# conjunto_set = {54,342,342,56}
# conjunto_set.add(12) 
# print(conjunto_set)
   
   #18.1 Como se añade una lista en un conjunto

# conjunto_set = {54,342,342,56}

#19 como eliminar elementos

# conjunto_set = {54,342,342,56}
# conjunto_set.remove(56)
# print(conjunto_set)

   #19.1 Como eliminar un número aleatorio

# conjunto_set = {54,342,342,56}
# conjunto_set.pop()

   #19.2 otra forma de eliminar un elemento, usando el metódo "discard"
# conjunto_set = {54,342,342,56}
# conjunto_set.discard(56)
# print(conjunto_set)

   #19.3 Eliminar todos los elementos del conjunto con el método "clear"

# conjunto_set = {54,342,342,56}
# conjunto_set.clear()
# print(conjunto_set)

#20 como unir conjuntos

# a = {83,90,41}
# b = {9,3,5}
# a.union(b)

#Tambien de pueden unir con este otro método

# a|b

#21 entersección del conjunto, sirve para encontrar un elemento en común entre dos conjuntos

# a = {83,90,41}
# b = {9,3,41}
# a.intersection(b)

#23 Como diferenciar un elemento con otro conjunto

# a = {83,90,41}
# b = {9,3,5}
# a.difference(b)

#De todos modos puedes hacer con este método presente

# a-b

#24 Como hacer diferencias simétricas

# a = {83,90,41}
# b = {9,3,5}
# a.symmetric_difference(b)

#Igualmente puedes usar este método

# a^b

#25 Como saber que hay un conjunto con un valor mayor, recibe un conjunto como parámetro mayor

# a = {83,90,41}
# b = {9,3,5}
# a.issuperset(b)

#Tambien hay otro método más facil

# a >= b

#26 como saber si hay un conjunto menor, que recibe un conjunto como parametro menor 

# a = {83,90,41}
# b = {9,3,5}
# a.issubset(b)

#Tambien puedes usar otro método

# a <= b

#27 como saber si hay elementos comunes entre 2 conjuntos

# a = {83,90,41}
# b = {9,3,5,7}
# a.isdisjoint(b)