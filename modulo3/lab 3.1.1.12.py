'''
nombre:Monserat Orduña Basaldua
Descripcion: laboratorio 3.1.1.12
Fecha:2/10/2023
'''

year = int(input("Introduce un año: "))

if year < 1582:
    print("No está dentro del período del calendario ")
else:
    
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        print("Año Común")
    else:
        print("Año Bisiesto")