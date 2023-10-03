'''
nombre:Monserat Orduña Basaldua
Descripcion: laboratorio 3.2.1.14
Fecha:2/10/2023
'''

blocks = int(input("Ingresa el número de bloques: "))


height = 0
blocks_utilizados = 0

while blocks_utilizados + height + 1 <= blocks:
    height += 1
    blocks_utilizados += height


print("La altura de la pirámide:", height)