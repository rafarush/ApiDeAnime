from animeflv import AnimeFLV


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
    except Exception as e:
        print(e)
input("Presione tecla para salir")
