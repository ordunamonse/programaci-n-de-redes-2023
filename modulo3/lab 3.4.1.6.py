'''
nombre:Monserat Orduña Basaldua
Descripcion: laboratorio 3.4.1.6
Fecha:2/10/2023
'''
hat_list = [1, 2, 3, 4, 5]

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.

numero_reemplazo = int(input("Ingresa un número entero para reemplazar el número central: "))

hat_list[2] = numero_reemplazo

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

print("La longitud de la lista es:", len(hat_list))

print(hat_list)
