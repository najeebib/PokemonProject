import json
from .sql_queries import insert_into_pokemons_table, insert_into_types_table, insert_into_trainers_table, insert_into_Pokedex_table, insert_into_PokemonTypes_table
from data.database import get_db
import requests
def load_db():
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

                owners = pokemon["ownedBy"]
                db_generator = get_db()
                db = next(db_generator)

                insert_into_pokemons_table(db, pokemon_name, pokemon_height, pokemon_weight)
                insert_into_types_table(db, types)
                insert_into_PokemonTypes_table(db, pokemon_name, types)
                for trainer in owners:
                    trainer_name = trainer["name"]
                    trainer_town = trainer["town"]
                    insert_into_trainers_table(db, trainer_name, trainer_town)
                    insert_into_Pokedex_table(db, pokemon_name, trainer_name)
    except FileNotFoundError:
        print(f"File not found.")
        return
