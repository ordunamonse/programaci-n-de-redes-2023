'''
nombre:Monserat Orduña Basaldua
descripcion:lab 4.3.1.16
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


recuentos_letras_ordenados = dict(sorted(recuentos_letras.items(), key=lambda x: x[1], reverse=True))


for letra, recuento in recuentos_letras_ordenados.items():
    print(f"{letra} -> {recuento}")


nombre_archivo_hist = nombre_archivo.split('.')[0] + '.hist'
with open(nombre_archivo_hist, 'w') as archivo_hist:
    for letra, recuento in recuentos_letras_ordenados.items():
        archivo_hist.write(f"{letra} -> {recuento}\n")
