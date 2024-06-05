import json
from data.database import mongo_api
import requests

def load_db():
    """
    Migrate the data from json file to MySQL db
    """
    try:
        with open("./data/pokemons_data.json", "r") as f:
            content = f.read()
            content = json.loads(content)
            for pokemon in content:
                pokemon_id = pokemon["id"]
                pokemon_name = pokemon["name"]
                pokemon_weight = pokemon["weight"]
                pokemon_height = pokemon["height"]
                pokemon_type = pokemon["type"]

                
                types = []
                if isinstance(pokemon_type, list):
                    for type in pokemon_type:
                        types.append(type)
                else:
                    types.append(pokemon_type)

                poke_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
                response = poke_api.json()
                poke_types = response["types"]
                for type in poke_types:
                    if type not in types:
                        types.append(type["type"]["name"])
                

    except FileNotFoundError:
        print(f"File not found.")
        return
