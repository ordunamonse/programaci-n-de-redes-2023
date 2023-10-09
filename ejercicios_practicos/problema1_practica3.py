'''
Nombre: Monserrat Orduña Basaldua
Asignatura: Programacion de Redes
Descripcion: Ejercicios Practicos 
'''

datos = []

for _ in range(5):
    dato = int(input("Dame un numero entero: "))
    datos.append(dato)
tuplaDatos = tuple(datos)


def mostrar_tupla(tupla):
    print("Contenido de la tupla:", tupla)
