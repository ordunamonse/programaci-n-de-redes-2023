'''
Nombre:Monserrat Orduña Basaldua 
Fecha: 23 de octubre 2023
Descripcion: Invocando  

'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "San Miguel de allende"
key = "XxL9wmf7qb4t0P3QY2uB8UpVwoOTaCHV"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()
print(json_data['route']['sessionId'])

#Extrae la distancia  y el tiempo
print(json_data['route']['distance'])
print(json_data['route']['time'])

#Extraer del primer elemento legs el campo formattedtime
print(json_data['route']['formattedTime'])
