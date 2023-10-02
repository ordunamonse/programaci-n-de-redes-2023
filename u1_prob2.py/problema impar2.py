'''
Nombre: Monserrat =rduña Basaldua
Descripcion: evaluacion
fecha:25/09/2023
'''

'''
Escribir un programa en Python que almacene las asignaturas que un estudiante de
Infraestructura en redes digitales lleva durante el cuarto cuatrimestre 
(por ejemplo, Probabilidad y Estadística, Electrónica para IDC Física, Conexión de redes WAN, 
Administración de servidores I, Programación de Redes e inglés IV), pregunta la nota que ha sacado
en la unidad I de cada asignatura, después las muestre en pantalla con el mensaje “En <asignatura> 
has sacado <nota>” donde asignatura es cada una de las asignaturas de la lista y <nota> cada una de
las correspondientes notas.

'''

asignatura = "Probabilidad y Estadística"
asignatura = "Electrónica para IDC Física"
asignatura = "Conexión de redes WAN"
asignatura = "Administración de servidores I"
asignatura = "Programación de Redes"
asignatura = "Inglés IV"

nota = +0
asignatura = float (input ("Ingresa un valor para asignatura: "))
print ("que nota has obtenido en la unidad 1 ", nota )
nota  = float (input ("Ingresa un valor para nota: "))



for asignatura in asignatura:
    nota = float(input("Ingresa la nota de la unidad I para: ", asignatura))
   
    asignatura = nota

for asignatura, nota in asignatura.items():
    print("En", asignatura, " has sacado ",nota )
