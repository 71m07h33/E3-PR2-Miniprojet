import requests

api_endpoint = "https://geo.api.gouv.fr/communes"

commune_code = "01001"
params = {
    "code": commune_code,
    "fields": "code,nom,centre",
    "format": "json",
}

response = requests.get(api_endpoint, params=params)

print(response.json())
