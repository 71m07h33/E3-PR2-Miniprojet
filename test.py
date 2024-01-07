import requests

geo_data = requests.get(
    f"https://geo.api.gouv.fr/communes?code=01001&fields=contour"
).json()

print(geo_data[0]["contour"]["coordinates"])
