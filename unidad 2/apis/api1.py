'''
nombre:Monserat Orduña Basaldua
descripcion:apy 1 chistes 
Fecha:09/11/2023
'''
import requests

while True:
    input("Presiona Enter para obtener un chiste (o escribe 'quit' para salir)")

    main_api = "https://v2.jokeapi.dev/joke/Any"

    response = requests.get(main_api)

    if response.status_code == 200:
        data = response.json()

        if data['type'] == 'single':
            print("Chiste: " + data['joke'])
        elif data['type'] == 'twopart':
            print("Pregunta: " + data['setup'])
            print("Respuesta: " + data['delivery'])
    else:
        print("No se pudo obtener el chiste. Inténtalo de nuevo más tarde.")

    user_input = input("¿Quieres otro chiste? (y/n): ")
    if user_input.lower() != 'y':
        print("¡Hasta luego!")
        break
