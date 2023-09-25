'''
problema 2
Resuelve el siguiente problema de las raíces de una ecuación cuadrática mediante la fórmula general.

Escribir un programa en Python que de solución a la formula general
Nombrar el archivo u1_prob1_usuariogithub.py
Define función que lee un valor de usuario y regresa valor leído.
x=-bb2-4ac2a

Nombre:Monserrat Orduña Basaldua
Descripcion:problema 2
Fecha:25/09/2023

'''
inport while
def calcularProblema(a, b, c):
    variable  = b**2 - 4*a*c

    if variable > 0:
        x1 = (-b + math.sqrt(variable)) / (2*a)
        return x1 
    elif variable == 0:
        x1 = -b / (2*a)
        return x1
    else:

while():
    print("Ecuación cuadrática  resuelta de la forma ax^2 + bx + c = 0")
    a = leer_valor("Ingresa el valor de 'a': ")
    b = leer_valor("Ingresa el valor de 'b': ")
    c = leer_valor("Ingresa el valor de 'c': ")

    soluciones = calcularLasolucionCuadratica(a, b, c)
  