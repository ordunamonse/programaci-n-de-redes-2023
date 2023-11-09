'''
Nombre:Monserrat Orduña Basaldua 
Fecha: 30 de octubre 2023
Descripcion: Invocando  

'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San ocote "
dest = "San Miguel de allende"
key = "XxL9wmf7qb4t0P3QY2uB8UpVwoOTaCHV"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()

#imprimir la URL
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

elif json_status == 0:
    print("API Status: " + str(json_status) + " = A failuer route call.\n")


