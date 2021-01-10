import requests
import json

print("Welcome to the pokemon dex cil")

pokemonName = input("Which pokemon do you want to search? ")

data=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
data =json.loads(data.text)

print(f"You choose {data['name']}")

action = input("What informtaion would you like to see to see?b(i=info , s=stats) ")

print(data["moves"][0]["move"]["name"])