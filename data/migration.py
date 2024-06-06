import json
from data.database import mongo_api
import requests
import utils.insert_functions as insert_functions
import utils.update_functions as update_functions
import utils.get_functions as get_functions
def load_db():
    """
    Migrate the data from json file to MySQL db
    """
    try:
        with open("./data/pokemons_data.json", "r") as f:
            content = f.read()
            content = json.loads(content)
            for pokemon in content:
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
                pokemon_dict = {"name": pokemon_name, "weight": pokemon_weight, "height": pokemon_height, "types": types}
                insert_functions.insert_pokemon(pokemon_dict)

                trainers = pokemon["ownedBy"]
                for trainer in trainers:
                    if get_functions.get_trainer_by_name(trainer["name"]) == None:
                        insert_functions.insert_trainer({"name": trainer["name"], "town": trainer["town"]})
                    trainer_obj = get_functions.get_trainer_by_name(trainer["name"])
                    update_functions.add_trainer_to_pokemon(pokemon_name, trainer_obj["_id"])
                

                

    except FileNotFoundError:
        print(f"File not found.")
        return
