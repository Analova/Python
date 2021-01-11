import requests
import json

print("Welcome to the pokemon dex cil")

pokemonName = input("Which pokemon do you want to search? ")

data=requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonName}")
data =json.loads(data.text)

print(f"You choose {data['name']}")

action = input("What informtaion would you like to see to see?b(i=info , s=stats) ")

if action == "i" or action == "info":
    print(f"id:{data['id']}")
    print(f"name:{data['name']}")
    print(f"height:{data['height']}")
    print(f"weight:{data['weight']}")
    pokemon_type=""
    for type in data["types"]:
        if data["types"].index(type) == (len(data["types"])-1):
            pokemon_type+= f"{type['type']['name']}"
        else:
            pokemon_type+= f"{type['type']['name']}, "
    print(f"type:{pokemon_type}")   