#1 crear una variable:
Hola_mundo = "Hola"
#Variable con valor 
number = 2

#2 suma de variables, concepto: solo tienes que hacer tres variables, las 2 son para hacer las operaciones y la otra estara programada para calcular la operación de las variables 
# CantidadInvertidad = 100

# IngresosAnuales = 100

# AnosRecuperación = CantidadInvertidad + IngresosAnuales

# print(AnosRecuperación)

#3 Variable compleja, concepto: Variables que tienes valores enteros sumados por números al usar el codigo "complex", también puedes programar una variable con valor imaginario solo usa el siguiente codigo "complex(x,y)"
# x = 25
# complex(x) = (25 + 0j)

# y = 10

# complex(x,y) = (25 + 10j)

#4 strings = variable normal
# hola = "hola"

#5 strings = variable multiplicada, concepto: al programar una variable que tenga una string y lo multiplicas sera repetido al valor asignado
# holapor5 = hola * 5
# print(holapor5)

#6 Strings = Multilineal
# Variable = """Hola \n soy homero chino"""
# print(variable)

#7 strings = Hacer oraciones, concepto: programas cada strings y los une con la terminal o con la ventana de python
# 'El\"perro\"de Luis'
# print('El\"perro\"de Luis')

#8 strings = sumas:
# '5'+'5'
# print('5'+'5')

#9 strings = multiplica palabras u oraciones por cualquier digito: es lo mispirque la variable multiplicada, solo que sin ninguna variable
# "Hola" * 5
# print("Hola" * 5)

#10 Que es una lista: Una lista Python te permite tener otras listas que contienen varios elementos del mismo tipo o una combinación de diferentes tipos de datos
# lista = [1, 4, 5]
# type(lista)
# print(lista)

#11 como modificar un elemento
# lista = [1, 4, 5]
# lista[2] = 3

#12 para eliminar el ultimo elemento de la lista
# lista.pop(0)
# print(lista.pop(0))

#13 Como añadir un nuevo elemento a la lista
# lista = [1, 2, 5]
# lista.append(0)

#14 Que es una Tupla: una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo
# tupla = (1, 5, 4)
# type(tupla)
# print(tupla)

#15 para cambiar un valor de la tupla
#tuple_matematicas = ("Minimo cmún multiplo", "División", "Multiplicación")
#y = list(tuple_matematicas)
#y[2] = "suma"
#tuple_matematicas = tuple(y)

#16 para insertar un dato en la tupla
#tuple_a = ('a', 'b', 'c')
#tuple_b = ('d', 'e', 'f')
#tuple_c = tuple_a + tuple_b

#17 Conjuntos: es como una lista pero en conjunto, pone valores sin orden

# Id_conjunto = { elemento1,elemento2,...,elementoN }
# Id_conjunto = set ([elemento1,elemento2,...,elementoN])
# Id_conjunto = frozenset([elemento1,elemento2,...,elementoN])

    #16.1 ejemplos:

# conjunto = [1,1,45,6]

# conjunto_set = set ([54,342,342,56])
# El codigo set hacer que elimine los valores repetidos

#18 contadores de conjuntos
   #18.1 contadores, este contador diferencia un elemento en el conjunto, si hay sera verdadero si no hay será falso

# conjunto_set = set ([54,342,342,56])
# print(54 in conjunto_set)

   #18.2 contaddores, este mide la longitud del conjunto

# conjunto_set = set ([54,342,342,56])
# len(conjunto_set)

#19 Como añadir un nuevo valor en un conjunto

# conjunto_set = {54,342,342,56}
# conjunto_set.add(12) 
# print(conjunto_set)
   
   #19.1 Como se añade una lista en un conjunto

# conjunto_set = {54,342,342,56}

#20 como eliminar elementos

# conjunto_set = {54,342,342,56}
# conjunto_set.remove(56)
# print(conjunto_set)

   #20.1 Como eliminar un número aleatorio

# conjunto_set = {54,342,342,56}
# conjunto_set.pop()

   #20.2 otra forma de eliminar un elemento, usando el metódo "discard"
# conjunto_set = {54,342,342,56}
# conjunto_set.discard(56)
# print(conjunto_set)

   #20.3 Eliminar todos los elementos del conjunto con el método "clear"

# conjunto_set = {54,342,342,56}
# conjunto_set.clear()
# print(conjunto_set)

#21 como unir conjuntos

# a = {83,90,41}
# b = {9,3,5}
# a.union(b)

#Tambien de pueden unir con este otro método

# a|b

#22 entersección del conjunto, sirve para encontrar un elemento en común entre dos conjuntos

# a = {83,90,41}
# b = {9,3,41}
# a.intersection(b)

#24 Como diferenciar un elemento con otro conjunto

# a = {83,90,41}
# b = {9,3,5}
# a.difference(b)

#De todos modos puedes hacer con este método presente

# a-b

#25 Como hacer diferencias simétricas

# a = {83,90,41}
# b = {9,3,5}
# a.symmetric_difference(b)

#Igualmente puedes usar este método

# a^b

#26 Como saber que hay un conjunto con un valor mayor, recibe un conjunto como parámetro mayor

# a = {83,90,41}
# b = {9,3,5}
# a.issuperset(b)

#Tambien hay otro método más facil

# a >= b

#27 como saber si hay un conjunto menor, que recibe un conjunto como parametro menor 

# a = {83,90,41}
# b = {9,3,5}
# a.issubset(b)

#Tambien puedes usar otro método

# a <= b

#28 Como saber si hay elementos comunes entre 2 conjuntos

# a = {83,90,41}
# b = {9,3,5,7}
# a.isdisjoint(b)

#29 Diccionarios: Son fuentes de colección, que no se ordenan como los conjuntos ni como las tuplas, el orden le da el programa de Python

# diccionario_clases = {123:"Matemáticas", 450:"Física", 320:"Química", 34:"Programación" }

   #29.1 Crear un diccionario pero con la función dict

# dicionario = dict(a=1, b=2, c=3)

#30 Como acceder a los valores del diccionario

# diccionario_clases = {123:"Matemáticas", 450:"Física", 320:"Química", 34:"Programación" }

# diccionario_clases[123]

#31 Como agregar nuevos valores

# dicionario_clases = {123:"Matemáticas", 450:"Física", 320:"Química", 34:"Programación" }

# dicionario_clases[90] = "Literatura"

#Tambien con la función dict

# diccionario = dict()
# diccionario['Arma2'] = "Guadaña"

#32 Como modificar valores
# dicionario_clases = {123:"Matemáticas", 450:"Física", 320:"Química", 34:"Programación" }

# dicionario_clases[320] = "Música"

# Tambien podemos modificar los valores con la función dict

# dicionario = dict(a=1, b=2, c=3)
# dicionario['c'] = -3

#33 Como detectar claves: Si la clave del valor no exista el resultado será falso y si es viceversa es verdadero

# dicionario = dict(a=1, b=2, c=3)

# 'c' in dicionario

# Tambien sirve con el diccionario normal

# dicionario_clases = {123:"Matemáticas", 450:"Física", 320:"Química", 34:"Programación" }

# 450 in dicionario_clases

#34 Como recorrer un diccionario: Sirve para ver el diccionario completo con solo usar unas lineas de código

# diccionario = {123:"Matemáticas", 450:"Física", 320:"Química", 34:"Programación" }

# for clave in diccionario:
#    print (clave, diccionario[clave])

#35 Como recorrer una tupla: Es lo mismo que recorrer un diccionario solo cambia las variables

# diccionario = dict(a=1, b=2, c=3)
# for valor in diccionario.items():
#    print (valor)

# Tambien hay un método para que los valores no salga como una tupla o como un diccionario 

# diccionario = dict(a=1, b=2, c=3)

# for clave, valor in diccionario.items():
#    print(clave,valor)

#36 Como hacer una pila: Una pila es un tipo de coleccionos que tiene una valor encima del otro

# from cmath import pi
# from collections import deque

# numericos = deque()

#37 El bucle While: Este código muy importante hacer una función por siempre a cambio de una condición, si es positiva avanza el bucle si no, no avanza

# n = int(input("Ingrese la cantidad de números:"))
# s = 0
# i = 1
# while i <= n:
#    c = i**2
#    s += c
#    i += c
# print("la suuma es:",s)

#38 Bucle for: Este código hace que una variable en un iterable, asi como una tupla o una lista, haga acciones con los diferentes elementos de la lista hasta llegar al ultimo
 
# for n in[1,2,3,4,5]:
#    c=n*n
#    print(n,c)

#39 Bucle for-in range: El bucle for - in range sirve para poner valores con un limite

# for n in range(10):
#    c=n**2
#    print(n,c)

# 40 Instruccione Break: Esta condición sirve para cerrar condiciones como el bucle while y el bucle for
  # En while:

# i = 0
# while True :
#    if i >= 10:
#       break
#    print(i)
#    i = i+1
   # En for
# colección = [2,4,5,7,8,9,3,4]
# for num in colección:
#    if num == 7:
#       break
#    print(num)

# 41 La Instrucción continue: Esta intrucción es el que evalúa una condición, si la condición es correcta puede seguir el bucle
  # En While:

# var = 10 
# while var == 10:
#    var = var -1
#    if var == 5:
#       continue
#    print("Valor actual de var" + str (var))
  # En for:

# colección = [2,4,5,7,8,9,3,4]
# for num in colección:
#    if num %2 != 0:
#       continue
# print(num)

#42 Cadena de caracteres: Sirve para escribir textos
  #42.1: Cadena normal
#text = "Hola un gusto"

  #42.2: Salto de linea
# esc = 'Hola \n mucho \n gusto'
# print(esc)
  #41.3: Tabulador
# tab = 'Hola \t mucho \t gusto'
# print(tab)
  #42.4: Sobre saltar una palabra
# text = "No \"MAMES\" calla la boca"
# print (text)
  #42.5: Concadenar
# text1 = "Soy..."
# text2 = "Diego"
# suma = text1 + text2
# print(suma)
  #42.6 recorrido
# cadena = "python"
# for c in cadena:
#   print(c)
# i=0
# while i < len(cadena):
#   print(i,cadena[i])
#   i=i+1
# for i in range (len(cadena)):
#   print(i,cadena[i])
# for pos in enumerate(cadena):
#   print(pos)
# # for i,c in enumerate(cadena):
  # print(i,cadena[i])

#43 slicing: Es una practica que permite modificar una cadena como cortar cadenas
  #43.1 Rebanando
# cadena = "Ana es muy buena programando"
# cadena[0:4]
  #43.2 slicing con indice negativo
# cadena = "Python lenguage de programación"
# cadena[:-4]
  #43.3 slicing paso a paso: Hace que quiten un caracter según el número de pasos
# cadena = "Yo programo"
# cadena [::2]

#44 Métodos de cadena
  #44.1
# cadena = "programando en python" .capitalize()
# print(cadena.count("o"))
  #43.2
# cadena = "la suma de {0}+{1} es {2}".format(1,2,1+2)
  #44.4
# cadena = "Las {} es una buena fruta".format("Fresa")
# print(cadena)
  #44.5
# cadena = "Pogramando en Cambas"
# cadena.replace("Cambas", "Python")
  #44.6
# cadena = "La formula"
# print(cadena.split(" "))
  #44.7
# cadena = "Hola" , "estas"
# cadena2 = "como"
# añadir = cadena2.join(cadena)
# print(añadir)
  #44.8
# cadena = "BUEN DÍA"
# cadena.lower()

#45 Definiendo una función: Es un segmento de un código que hace una tarea designada
# def Suma (y,x):
#   print(y + x)

 #Otro ejemplo
# def resta (y,x):
#   r = y-x
#   return r

#46 Llamar una función: Esto sirve para que la función creada ejecute
# x = 3
# y = 5
# Suma(x,y)
# print(Suma)

#47 Parametro: es un valor que espera recibir la función

# def Suma (a = 0,b = 0):
#   return a + b

#48 Argumentos: Son expresiones que se utilizan al momento de llamar o invocar a la función
  #48.1 argumentos por posición: Son aquellos que aposicionan las variables según el orden que va
# def suma (a,b):
#   return a + b
# sum = suma(1,2)
# print(sum) 
  #48.2 Argumentos por nombre: Es como argumentos por posición, pero a la posición le asignas un valor 
# def suma (a,b):
#  return a + b
# sum = suma (a = 5, b = 3)
# print(sum)
  #48.3 Argumentos por valor: Se crea una copia local de la variable dentro de la función, sin que su valor externo cambie
# def masapan(numero):
#   numero * 2
#   n = 10
#   masapan(n)
#   print(numero)

  #48.4 Argumentos por referencia: Es como el argumento por valor pero cambia el resultado externo
# A = 5
# A += 2
# print(A)

  #48.5 Argumentos por posición: Asigna un valor a una función por la pocisión
# def incrementa(a):
#   a+=1
#   return a

#   a = 1
#   b = incrementa(a)
#   print("a:", a)
#   print("b:", b)

#49 Funciones sin retorno de valor:No llevan el return, se suelen emplear para imprimir mensajes de salida por pantalla o imprimir información en archivos
# def lista_imprimir (lista_imprimir, *cosas):
#   print("lista de" + lista_imprimir)
#   for cosa in cosas:
#     print(cosa)
# lista_imprimir ("Herramienta","Comida", "Adornos")

#50 Funciones con retorno de valor: Lleva la setencia return, se suelen emplear para realizar calculos
# def suma_cuadrado(*números):
#   cuad=0
#   for num in números:
#     cuad+=num**2

#   return cuad
# sc = suma_cuadrado(1,2,3)
# print("La suma de los primeros N cuadrado es:", sc)

#51 Parametros arbitrios: recibe un número variable de argumentos
# def imprime_liro(nombre_libro, **descripción):
#   print("Libro de" + nombre_libro)
#   for clave in descripción:
#     print(clave,descripción[clave])
# imprime_liro("El ENTE", Autor = "???")

#52 Funciones recursivas: Las funciones recursivas son aquellas que dentro de su algoritmo, hacen referencia a sí misma
# def cuenta_atras(n):
#   if n == 0:
#     print ("Despegando...")
#   else:
#     print("n=", n)
#     cuenta_atras(n-1)
# cuenta_atras(3)