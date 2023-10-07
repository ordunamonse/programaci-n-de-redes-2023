'''
nombre:Monserat Orduña Basaldua
Descripcion: Laboratorio 4.3.1.9
Fecha:06/10/2023
'''


def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

# Pruebas
for i in range(1, 20):
    if is_prime(i + 1):
        print(i +  1, end=" ")
print()


