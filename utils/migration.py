import json

def load_db():
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
                owners = pokemon["ownedBy"]
                # add pokemon to sql table
                for trainer in owners:
                    trainer_name = trainer["name"]
                    trainer_town = trainer["town"]
                    # add trainer to trainers table
                    # add pokemon_name and trainer_name to Pokdex table
    except FileNotFoundError:
        print(f"File not found.")
        return
