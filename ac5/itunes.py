import requests

def search_track(query):
    url = f"https://itunes.apple.com/search?term={query}&entity=song"
    response = requests.get(url)
    data = response.json()

    if "results" in data:
        track = data["results"][0]
        print("Artista:", track["artistName"])
        print("Música:", track["trackName"])
        print("Álbum:", track["collectionName"])
        print("Preço:", track["trackPrice"])
    else:
        print("Nenhuma faixa encontrada.")

# Exemplo de uso
search_track("Imagine - John Lennon")
