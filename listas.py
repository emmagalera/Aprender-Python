lista = ["Emma", 22, 10, "Toyota", 13, "Oceano"]

#Añadir al final
lista.append(4)
print(lista)#"Emma", 22, 10, "Toyota", 13, "Oceano", 4

#Indicar la posicion donde se añade
lista.insert(3, "Bocadillo") 
print(lista) #"Emma", 22, 10, "Bocadillo", "Toyota", 13, "Oceano", 4

#cambiar el elemento de una lista
lista[3] = 5 
print(lista) #"Emma", 22, 10, 5, "Toyota", 13, "Oceano", 4

#Contar los elementos que hay en una lista
print(len(lista)) #8

#Eliminar un elemento de la lista
del lista[5] 
print (lista) #"Emma", 22, 10, 5, "Toyota", "Oceano", 4

#Indice negativo = comienza a recorrer la lista de atras a delante
print(lista[-1]) #4
print(lista[-2]) #"Oceano"
print(lista[-3]) #"Toyota"
print(lista[-4]) #5
print(lista[-5]) #10
print("\n")

#Ordenar una lista
#sort() y reverse() ordena la lista en su lugar y no devuelve una nueva lista ordenada
lista_desordenada = [5, 2, 1, 3, 4]
"""Por lo tanto, esto estaria mal
lista_ordenada = lista_desordenada.sort() #Ascendente
lista_ordenada2 = lista_desordenada.reverse #Descendente
"""
#Lo correcto seria
lista_desordenada.sort()
lista_ordenada = lista_desordenadalista = ["Emma", 22, 10, "Toyota", 13, "Oceano"]

#Añadir al final
lista.append(4)
print(lista)#"Emma", 22, 10, "Toyota", 13, "Oceano", 4

#Indicar la posicion donde se añade
lista.insert(3, "Bocadillo") 
print(lista) #"Emma", 22, 10, "Bocadillo", "Toyota", 13, "Oceano", 4

#cambiar el elemento de una lista
lista[3] = 5 
print(lista) #"Emma", 22, 10, 5, "Toyota", 13, "Oceano", 4

#Contar los elementos que hay en una lista
print(len(lista)) #8

#Eliminar un elemento de la lista
del lista[5] 
print (lista) #"Emma", 22, 10, 5, "Toyota", "Oceano", 4

#Indice negativo = comienza a recorrer la lista de atras a delante
print(lista[-1]) #4
print(lista[-2]) #"Oceano"
print(lista[-3]) #"Toyota"
print(lista[-4]) #5
print(lista[-5]) #10
print("\n")

#Ordenar una lista
#sort() y reverse() ordena la lista en su lugar y no devuelve una nueva lista ordenada
lista_desordenada = [5, 2, 1, 3, 4]
"""Por lo tanto, esto estaria mal
lista_ordenada = lista_desordenada.sort() #Ascendente
lista_ordenada2 = lista_desordenada.reverse #Descendente
"""
#Lo correcto seria
lista_desordenada.sort()
lista_ordenada = lista_desordenada
lista_desordenada.reverse()
lista_ordenada2 = lista_desordenada
print(f"Mal: \nLista ordenada 1: {lista_ordenada} \nLista ordenada 2: {lista_ordenada2}\n")
"""EL codigo anterior devolveria la misma lista en el mismo orden, es decir, asi:
    Lista ordenada 1: [5, 4, 3, 2, 1] 
    Lista ordenada 2: [5, 4, 3, 2, 1]
lista_ordenada como lista_ordenada2 son simplemente referencias a la misma lista lista_desordenada 
depues de las operaciones de sort() y reverse. En Python cuando se asigna una lista a una variable,
se hace referencia a la misma lista en memoria, no creando una lista independiente
"""
#Creacion de copias independiente de lista ordenada y revertida
lista_ordenada = sorted(lista_desordenada)
lista_ordenada2 = sorted(lista_desordenada, reverse = True)
print(f"Bien:\nLista ordenada 1: {lista_ordenada} \nLista ordenada 2: {lista_ordenada2}\n")

#Rebanar un lista
lista_elementos = [0, 1, 2, 3, 4, 5]
print(f"Lista ordenada: {lista_elementos}")
print(lista_elementos[1:]) #desde el primer elemento hasta el final: [1, 2, 3, 4, 5]
print(lista_elementos[:3]) #Desde el principio hasta el elemento 3(sin añaduir el elemento 3): [0, 1, 2]
print(lista_elementos[-4:-2]) #Desde el elemento en -2 hasta el elemento en -4: [2, 3]

#Recorrer una lista con bucle for
for element in lista:
    print (element)

contador = 0
for element in lista:
    contador += 1
print(f"Hay {contador} elementos en la lista \n")

#Bucle anidados: por cada iteración del bucle externo, el bucle interno se recorrerá completamente
dias_semana = ["L", "M", "x", "j", "V"] #bucle externo
tareas_semana = ["Beibol", "Danza", "Natación"] #bucle interno
for dia in dias_semana:
    for tarea in tareas_semana:
        print(f"{dia}: {tarea}")
    print("\n")

for dia in dias_semana:
    print(f"{dia}: ")
    for tarea in tareas_semana:
        print(tarea)
    print("\n")
lista_desordenada.reverse()
lista_ordenada2 = lista_desordenada
print(f"Mal: \nLista ordenada 1: {lista_ordenada} \nLista ordenada 2: {lista_ordenada2}\n")
"""EL codigo anterior devolveria la misma lista en el mismo orden, es decir, asi:
    Lista ordenada 1: [5, 4, 3, 2, 1] 
    Lista ordenada 2: [5, 4, 3, 2, 1]
lista_ordenada como lista_ordenada2 son simplemente referencias a la misma lista lista_desordenada 
depues de las operaciones de sort() y reverse. En Python cuando se asigna una lista a una variable,
se hace referencia a la misma lista en memoria, no creando una lista independiente
"""
#Creacion de copias independiente de lista ordenada y revertida
lista_ordenada = sorted(lista_desordenada)
lista_ordenada2 = sorted(lista_desordenada, reverse = True)
print(f"Bien:\nLista ordenada 1: {lista_ordenada} \nLista ordenada 2: {lista_ordenada2}\n")

#Rebanar un lista
lista_elementos = [0, 1, 2, 3, 4, 5]
print(f"Lista ordenada: {lista_elementos}")
print(lista_elementos[1:]) #desde el primer elemento hasta el final: [1, 2, 3, 4, 5]
print(lista_elementos[:3]) #Desde el principio hasta el elemento 3(sin añaduir el elemento 3): [0, 1, 2]
print(lista_elementos[-4:-2]) #Desde el elemento en -2 hasta el elemento en -4: [2, 3]

#Recorrer una lista con bucle for
for element in lista:
    print (element)

contador = 0
for element in lista:
    contador += 1
print(f"Hay {contador} elementos en la lista \n")

#Bucle anidados: por cada iteración del bucle externo, el bucle interno se recorrerá completamente
dias_semana = ["L", "M", "x", "j", "V"] #bucle externo
tareas_semana = ["Beisbol", "Danza", "Natación"] #bucle interno
for dia in dias_semana:
    for tarea in tareas_semana:
        print(f"{dia}: {tarea}")
    print("\n")

for dia in dias_semana:
    print(f"{dia}: ")
    for tarea in tareas_semana:
        print(tarea)
    print("\n")

#Verificar si un elemento esta en una lista o no
print("Beisbol" in tareas_semana) #true
print("Beisbol" not in tareas_semana) #Falsxe
print("Bailar" not in tareas_semana) #True

#Encontrar el mayor valor
lista_numeros = [6, 7, 8, 10, 9]
mayor = lista_numeros[0]
for i in lista_numeros[1:]: 
    if i > mayor:
        mayor = i
print(f"\nEl elemento con mayor valor es: {mayor}")

#El bucle tambien puede ser:
"""
a la varible menor le damos el valor del primer elemento de la lista
En el bucle for el rango es desde 1 hasta el numero  que supone la longitud de la lista
Si elemento de la lista de la posicion actual, en este caso lista_numeros[i] donde i 
es 1 por ejemplo, es menor al valor que tiene la variable actual, entonces
se actualiza el valor de la variable menor, por elemento de la lista de la posicion actual,
es decir, lista_numeros[i]
Nota: empezamos por el 1 para que lista_numeros[i] sea lista_numeros[1] y no lista_numeros[0],
por el valor de lista_numeros[0] ya esta dado a la variable menor
"""
menor = lista_numeros[0]
for i in range(1, len(lista_numeros)):
    if lista_numeros[1] < menor:
        menor = lista_numeros[i]
print(f"\nEl elemento con valor menor es: {menor}\n")

#Encontrar la posicion de un elemento en una lista
#lista_numeros = [6, 7, 8, 10, 9]
encontrar = 9
encontrado = False
for posicion in range(len(lista_numeros)): #la longitud de la lista es 5, entonces se cuenta de 0 a 4
    print(f"Posicion: {posicion} tiene el valor {lista_numeros[posicion]}")
    if lista_numeros[posicion] == encontrar:
        encontrado = True
        break
if encontrado:
    print(f"El numero {encontrar} esta en la posicion {posicion}")
else:
    print(f"No se ha localizado el numero {encontrar} en la lista {lista_numeros}")

#Compresion de lista
"""
Creacion de una lista llamada numeros que contine el numero 1 repetido 3 veces
"""
numeros = [1 for i in range(3)]
print(numeros, "\n")
#El codigo de arriba es lo mismo que
"""
numeros = []
for i in range(3):
    numeros.append(1)
"""

#Aumentar de 2 en 2, empezando a contar desde el 2
#Codigo comprimido: numeros = [2 + i*2 for i in range (10)]
print("Aumentar de 2 en 2, empezando a contar desde el 2")
print("--------------------------------------------------")
numeros = []
for i in range(10):
    numeros.append(2 + i*2)
    print(f"2 + ({i} * 2 = {i*2}) = {numeros[i]}")
print(f"\nResultado: {numeros} \n")

#Aumentar de 1 en 1, comenzando desde el numero 2
#Codigo comprimdo: numeros = [2 + i for i in range(5)]
print("Aumentar de 1 en 1, comenzando desde el numero 2")
print("-------------------------------------------------\n")
numeros = []
for i in range(5):
    numeros.append(2 + 1)
    print(f"2 + {i} =  {2 + i}")
print(f"\nResultado: {numeros}\n")

