'''
nombre:Monserat Orduña Basaldua
Descripcion: laboratorio 3.2.1.15
Fecha:2/10/2023
'''

n = int(input("Ingrese un número natural: "))

pasos = 0

while n != 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    pasos += 1

print(1)
print("pasos =", pasos)