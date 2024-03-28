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
