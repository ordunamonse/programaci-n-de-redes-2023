'''
nombre:Monserat Orduña Basaldua
descripcion:lab 4.3.1.15
Fecha:08/11/2023
'''
nombre_archivo = input("Introduce el nombre del archivo: ")


recuentos_letras = {}


try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        for letra in contenido:
            if letra.isalpha() and letra.isascii():
                letra = letra.lower()  
                recuentos_letras[letra] = recuentos_letras.get(letra, 0) + 1
except FileNotFoundError:
    print("El archivo no se encuentra.")
except Exception as e:
    print("Error al leer el archivo:", e)

for letra, recuento in sorted(recuentos_letras.items()):
    print(f"{letra} -> {recuento}")
