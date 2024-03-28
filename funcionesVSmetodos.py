"""
Teoria Cisco Academy:

Las funciones no pertene a ningun tipo de dato => Obtiene datos, crea nuevos datos y produce resultados

Un metodo hace todas esas cosas y además puede cambiar el estado de una entidad seleccionada

Se escribe por ejmeplo el método '.append()',
'.upper()', '.lower()', etc porque son funciones
especificas para cadena de texto
O por ejemplo '.append()', '.pop()' o 'insert()' porque son funciones que solo valos a poder utilizar en listas 

Pero se escribe por ejemplo la funcion 'print()',
len(), 'insert()', 'int()' etc porque son funcion que se pueden utilizae tanto para cadena de texto, enteros, listas,etc


"""

lista = [1, 2, 3, 4]

#Ejemplo de funcion : La funciona toma un argumento, hace algo y devuelve un resultado
print(len(lista)) #Tanto print() como len() es una funcion


#EJemplo de invocar un método: el nombre del metodo esta precedido por el nombre de los datos 
#que posee el metodo. El metodo se comportará como una funcion pero ademas puede cambiar el estado
#interno de los datos
lista.append(5)

