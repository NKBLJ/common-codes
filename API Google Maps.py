import requests
import csv
import os

## https://developers.google.com/maps/documentation/places/web-service/search-nearby?hl=pt#maps_http_places_nearbysearch-sh

def buscar_escolas_na_regiao(api_key, latitude, longitude, tag, raio):
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': f'{latitude},{longitude}',
        'radius': raio,
        'keyword': tag,
        'key': api_key,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get('status') == 'OK':
            resultados = data.get('results')
            return resultados
        else:
            print(f'Erro na resposta da API: {data.get("status")}')
    else:
        print(f'Erro na solicitação HTTP: {response.status_code}')

    return []

# Entradas
api_key = os.environ.get("API_KEY")
latitude = -5.083
longitude = -42.08
tag = 'escola'
raio = 50000  # Em metros

resultados = buscar_escolas_na_regiao(api_key, latitude, longitude, tag, raio)

for resul in resultados:
    nome = resul.get('name')
    latitude = resul['geometry']['location']['lat']
    longitude = resul['geometry']['location']['lng']

    # Salva os dados em CSV
    with open("dados.csv", 'a', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, latitude, longitude])
    print(f'Nome: {nome}, Latitude: {latitude}, Longitude: {longitude}')
