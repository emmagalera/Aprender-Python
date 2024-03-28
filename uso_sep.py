""" 
Sep se utiliza para indicar el separador entre los diferentes 
elementos que se imprimen con la funcion print

El separador por defecto es el espacio en blanco si no se pone sep

"""

print("patatas", "queso", "carne")
    #Resultado: patatas queso carne

print("patatas","queso", "carne", sep=" & ")
    #Resultado: patatas & queso & carne

print("patatas", "queso", "carne", sep=", ")
    #Resultado: patatas, queso, carne

print("patatas", "queso", "carne", sep="---")
    #Resultado: patatas---queso---carne
