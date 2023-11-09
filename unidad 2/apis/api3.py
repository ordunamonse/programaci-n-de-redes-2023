'''
nombre:Monserat Orduña Basaldua
descripcion:apy 3 canciones 
Fecha:09/11/2023
'''
import requests

while True:
    track_name = input("Ingresa el nombre de una canción para obtener información sobre la canción y el artista (o escribe 'quit' para salir): ")

    if track_name.lower() == 'quit':
        print("¡Hasta luego!")
        break

    api_url = f"https://api.deezer.com/search?q={track_name}"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        tracks = data.get('data', [])
        if tracks:
            track = tracks[0]
            artist_name = track['artist']['name']
            album_name = track['album']['title']
            print(f"Artista: {artist_name}")
            print(f"Canción: {track_name}")
            print(f"Álbum: {album_name}")
        else:
            print(f"No se encontró información para la canción '{track_name}'.")
    else:
        print("No se pudo obtener la información de la API. Inténtalo de nuevo más tarde.")

