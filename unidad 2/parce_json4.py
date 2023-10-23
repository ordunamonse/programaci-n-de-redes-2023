'''
Nombre:Monserrat Orduña Basaldua 
Fecha: 23 de octubre 2023
Descripcion: Invocando  

'''

import urllib.parse
import requests


while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
   #Agregar condicion para dest
   #un mensaje hasta luego
    if dest == "quit" or dest == "q":
      break
    print("Hasta luego ")
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "XxL9wmf7qb4t0P3QY2uB8UpVwoOTaCHV"
    
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()

    #imprimir la URL
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
      print("API Status: " + str(json_status) + " = A successful route call.\n")

      print("=============================================")
      print("Directions from " + (orig) + " to " + (dest))
      print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
      print("Miles:           " + str(json_data["route"]["distance"]))
      #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
      print("=============================================")
      print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    else:
      print("API Status: " + str(json_status) + " = A failuer route call.\n")
      
      

 
