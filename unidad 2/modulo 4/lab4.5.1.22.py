'''
nombre:Monserat Orduña Basaldua
descripcion:lab 4.5.1.22
Fecha:08/11/2023
'''
from datetime import datetime

fecha_hora = datetime(2020, 11, 4, 14, 53, 0)

print(fecha_hora.strftime("%Y/%m/%d %H:%M:%S"))
print(fecha_hora.strftime("%y/%B/%d %H:%M:%S %p"))
print(fecha_hora.strftime("%a, %Y %b %d"))
print(fecha_hora.strftime("%A, %Y %B %d"))
print("Día de la semana:", fecha_hora.strftime("%w"))
print("Día del año:", fecha_hora.strftime("%j"))
print("Número de semana en el año:", fecha_hora.strftime("%U"))
