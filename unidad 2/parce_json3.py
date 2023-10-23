'''
Fecha: 23 de octubre 2023
Descripcion: Invocando
Nombre:Monserrat Orduña Basaldua   
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
    print ("Hasta luego ")
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
    elif json_status == 0:
      print("API Status: " + str(json_status) + " = A failuer route call.\n")