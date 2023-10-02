'''
Nombre:Monserat Orduña Basaldua 
Fecha: 02de octubre 2023
Descripcion laboratorio 2.6.1.11
'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))


# Escribe tu código aqui.
total_minutos = hour * 60 + mins + dura

nuevas_horas = total_minutos // 60 // 24
nuevos_minutos = total_minutos // 60

print("Tiempo final:", "{:02}:{:02}".format(nuevas_horas, nuevos_minutos))