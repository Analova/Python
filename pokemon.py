import requests

data=requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(data.json())