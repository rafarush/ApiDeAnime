import requests
import os
from animeflv import AnimeFLV

"""
def descargar_archivo(url):
    # Obtener el nombre del archivo de la URL
    nombre_archivo = url.split("/")[-1]
    # Realizar la solicitud GET
    respuesta = requests.get(url, stream=True)

    if respuesta.status_code == 200:
        # Guardar el archivo en modo binario
        with open(nombre_archivo, 'wb') as f:
            for chunk in respuesta.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Video '{nombre_archivo}' descargado exitosamente.")
    else:
        print(f"Error al descargar el video: {respuesta.status_code}")
"""


with AnimeFLV() as api:
    
    elements = api.search(input("Escriba el nombre del anime: "))

    for i, element in enumerate(elements):
        print(f"{i},{element.title}")
    try:
        seriesSelect = int(input("Seleccione una opcion: "))

        info = api.get_anime_info(elements[seriesSelect].id)
        info.episodes.reverse()
        
        for j, episode in enumerate(info.episodes):
            print(f"{j} | Episode - {episode.id}")
        
        episodeSelect = int(input("Seleccione un episodio: "))

        series = elements[seriesSelect].id
        episodeF = info.episodes[episodeSelect].id
        results = api.get_links(series, episodeF)

        for result in results:
            print(f"{result.server} - {result.url}")

        
        """
        option = int(input("Si desea descargar el episodio escriba 1: "))
        if option == 1:
            for k, result in enumerate(results):
                print(f"{k} - {result.server}")

            serverSelect = int(input("Seleccione un servidor:"))
            descargar_archivo(results[serverSelect].url)
        """
        



    except Exception as e:
        print(e)
print()        
input("Presione tecla para salir")


