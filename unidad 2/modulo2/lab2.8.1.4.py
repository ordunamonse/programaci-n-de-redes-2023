'''
nombre:Monserat Orduña Basaldua
descripcion:lab 2.8.1.4
Fecha:05/11/2023
'''
def read_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value
            else:
                print(f"Error: el valor no está dentro del rango permitido ({min}..{max})")
        except ValueError:
            print("Error: entrada incorrecta")

v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)
print("El número es:", v)
