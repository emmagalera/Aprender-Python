"""
Cada bucle puede tener un bucle anidado dentro del él, esto 
significa que por cada iteracion del bucle externo, el bucle 
externo se ejecutara completamente
"""
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
tareas = ["Gimnasio", "Natación", "Baile", "Cocina"]

for dia in dias_semana:
  for tarea in tareas:
    print(f"{dia}: {tarea}")
  print("\n")

"""
    Resultado:

    Lunes: Gimnasio
    Lunes: Natación
    Lunes: Baile
    Lunes: Cocina


    Martes: Gimnasio
    Martes: Natación
    Martes: Baile
    Martes: Cocina

    etc
"""

for dia in dias_semana:
  print(f"{dia}: ")
  for tarea in tareas:
    print(tarea)
  print("\n")

"""
    Resultado:

    Lunes: 
    Gimnasio
    Natación
    Baile
    Cocina

    Martes: 
    Gimnasio
    Natación
    Baile
    Cocina

    etc
"""


for dia, tarea in zip(dias_semana, tareas):
  print(f"{dia}: {tarea}")

"""
    Resultado:

    Lunes: Gimnasio
    Martes: Natación
    Miercoles: Baile
    Jueves: Cocina
"""

#Bucle for itera por cada palabra de la lista dia
#Y luego hay otro bucle for que imprime cada palabra 2 veces

for dia in dias_semana:
    for i in range(2):
      print(dia)


"""
    Resultado:

    Lunes
    Lunes
    Martes
    Martes
    Miercoles
    Miercoles

    etc
"""
