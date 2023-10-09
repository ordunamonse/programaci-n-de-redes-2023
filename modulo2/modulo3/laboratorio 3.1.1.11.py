'''
Nombre: Monserrat =rduña Basaldua
Descripcion: Laboratorio 3.1.1.11
fecha:25/09/2023
'''

income = float(input("Introduce el ingreso anual:"))

#
# Escribe tu código aquí.
#

if income <= 85528:
    tax = income * 0.18 -556.02
    
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
