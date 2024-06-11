import requests
from models.pokemon import Pokemon
from models.trainer import Trainer
import base64

class RequestsHandler:
    def __init__(self):
        pass

    def get_pokemon(self, pokemon_name):
        response = requests.get(f"http://pokemon_api-mypokemonserver-1:5000/pokemon?pokemon_name={pokemon_name}")
        pokemon_properties = response.json()
        response_image  = requests.get(f"http://mongodb_gridfs_server-myreader-1:5002/image/{pokemon_name}")
        image_data = response_image.content
        encoded_image = base64.b64encode(image_data).decode('utf-8')
        response_data = {
            "properties": pokemon_properties,
            "image": encoded_image
        }
        return response_data
    
    def add_pokemon(self, pokemon: Pokemon):
        response = requests.post("http://pokemon_api-mypokemonserver-1:5000/pokemon", json=pokemon.model_dump())

        res = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon.name).json()
        image_url = res["sprites"]["front_default"]
        response = requests.get(image_url)
        content = response.content
        encoded_image = base64.b64encode(content).decode('utf-8')
        pokemon = {"name": pokemon.name, "content": encoded_image}

        added_response = requests.post("http://mongodb_gridfs_server-myreader-1:5002/image", json=pokemon)
        return added_response.json()
    
    def get_pokemons_by_type(self, type):
        response = requests.get(f"http://pokemon_api-mypokemonserver-1:5000/pokemons/type?type={type}")
        return response.json()
    
    def get_pokemons_by_trainer(self, trainer_name):
        response = requests.get(f"http://pokemon_api-mypokemonserver-1:5000/pokemons/trainer?trainer_name={trainer_name}")
        return response.json()
    
    def add_trainer(self, trainer: Trainer):
        response = requests.post("http://pokemon_api-mypokemonserver-1:5000/trainer", json=trainer.model_dump())
        return response.json()
    
    def get_trainers(self, pokemon_name):
        response = requests.get(f"http://pokemon_api-mypokemonserver-1:5000/trainers/{pokemon_name}")
        return response.json()
    
    def add_pokemon_to_trainer(self, trainer_name: str, pokemon_name: str):
        response = requests.post(f"http://pokemon_api-mypokemonserver-1:5000/trainer/{trainer_name}/pokemon?pokemon_name={pokemon_name}")
        return response.json()
    
    def delete_pokemon_from_trainer(self,trainer_name: str, pokemon_name: str):
        response = requests.delete(f"http://pokemon_api-mypokemonserver-1:5000/trainer/{trainer_name}/pokemon?pokemon_name={pokemon_name}")
        return response.json()
    
    def evolution(self,trainer_name: str, pokemon_name: str, next_evolution: str):
        response = requests.put(f"http://pokemon_api-mypokemonserver-1:5000/evolution?trainer_name={trainer_name}&pokemon_name={pokemon_name}&next_evolution={next_evolution}")
        return response.json()
    
    def data_migration(self):
        response = requests.get("http://pokemon_api-mypokemonserver-1:5000/migration")
        pokemons_names = response.json()

        pokemons_list = []
        for name in pokemons_names:
            res = requests.get("https://pokeapi.co/api/v2/pokemon/" + name).json()
            image_url = res["sprites"]["front_default"]
            response = requests.get(image_url)
            content = response.content
            encoded_image = base64.b64encode(content).decode('utf-8')

            pokemon = {"name": name, "content": encoded_image}
            pokemons_list.append(pokemon)

        pokemons = {"pokemons": pokemons_list}
        mongo_server_response = requests.post("http://mongodb_gridfs_server-myreader-1:5002/images", json=pokemons)
        return mongo_server_response.json()


requests_handler = RequestsHandler()