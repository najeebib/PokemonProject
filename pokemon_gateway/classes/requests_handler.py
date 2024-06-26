import requests
from models.pokemon import Pokemon
from models.trainer import Trainer
from api.evolution_fns import get_pokemon_details
import base64

class RequestsHandler:
    def __init__(self):
        pass
    # get the pokemon properties and image from databases servers
    def get_pokemon_by_id(self, pokemon_id: int):
        response = requests.get(f"http://pokemon_api-pokemon-api-1:5001/pokemons/{pokemon_id}")
        pokemon_properties = response.json()
        response_image  = requests.get(f"http://images_server-images-server-1:5002/images/{pokemon_properties['name']}")
        image_data = response_image.content
        encoded_image = base64.b64encode(image_data).decode('utf-8')
        response_data = {
            "properties": pokemon_properties,
            "image": encoded_image
        }
        return response_data

    def get_pokemon_by_name(self, pokemon_name):
        response = requests.get(f"http://pokemon_api-pokemon-api-1:5001/pokemons/{pokemon_name}")
        pokemon_properties = response.json()
        response_image  = requests.get(f"http://images_server-images-server-1:5002/images/{pokemon_name}")
        image_data = response_image.content
        encoded_image = base64.b64encode(image_data).decode('utf-8')
        response_data = {
            "properties": pokemon_properties,
            "image": encoded_image
        }
        return response_data
    # add the pokemon and image to databases servers
    def add_pokemon(self, pokemon: Pokemon):
        response = requests.post("http://pokemon_api-pokemon-api-1:5001/pokemons", json=pokemon.model_dump())

        res = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon.name).json()
        image_url = res["sprites"]["front_default"]
        response = requests.get(image_url)
        content = response.content
        # encode the image to send it to server
        encoded_image = base64.b64encode(content).decode('utf-8')
        pokemon = {"name": pokemon.name, "content": encoded_image}

        added_response = requests.post("http://images_server-images-server-1:5002/images", json=pokemon)
        return added_response.json()
    
    # send get request to the server to get data 
    # i have done this like this to avoid repeated code when sending requests to get (pokemons by type/trainer name and get trainers by pokemon name)
    def get_request(self, url):
        response = requests.get(url )
        return response.json()
    # add traienr to database
    def add_trainer(self, trainer: Trainer):
        response = requests.post("http://pokemon_api-pokemon-api-1:5001/trainers", json=trainer.model_dump())
        return response.json()
    # add pokemon to trainer  
    def add_pokemon_to_trainer(self, trainer_name: str, pokemon_name: str):
        response = requests.post(f"http://pokemon_api-pokemon-api-1:5001/trainers/{trainer_name}/pokemons?pokemon_name={pokemon_name}")
        return response.json()
    # delete pokemon from trainer
    def delete_pokemon_from_trainer(self,trainer_name: str, pokemon_name: str):
        response = requests.delete(f"http://pokemon_api-pokemon-api-1:5001/trainers/{trainer_name}/pokemons/{pokemon_name}")
        return response.json()
    # evolve the pokemon of a certain trainer
    def evolution(self,trainer_name: str, pokemon_name: str, next_evolution: str):
        next_pokemon = requests.get(f"http://pokemon_api-pokemon-api-1:5001/pokemon?pokemon_name={next_evolution}")
        if next_pokemon.status_code == 404:
            pokemon_details = get_pokemon_details(next_evolution)
            pokemon = Pokemon(pokemon_details["name"], pokemon_details["type"], pokemon_details["weight"], pokemon_details["height"])
            self.add_pokemon(pokemon)
        response = requests.put(f"http://pokemon_api-pokemon-api-1:5001/evolution?trainer_name={trainer_name}&pokemon_name={pokemon_name}&next_evolution={next_evolution}")
        return response.json()
    # migrate the data fro json file to sql database and get each pokemons image from poke api and save it in gridfs mongodb server
    def data_migration(self):
        response = requests.get("http://pokemon_api-pokemon-api-1:5001/migration")
        pokemons_names = response.json()
        # get each pokemon's image from poke api
        pokemons_list = []
        for name in pokemons_names:
            res = requests.get("https://pokeapi.co/api/v2/pokemon/" + name).json()
            image_url = res["sprites"]["front_default"]
            response = requests.get(image_url)
            content = response.content
            # encode the image to send it to server
            encoded_image = base64.b64encode(content).decode('utf-8')
        
            pokemon = {"name": name, "content": encoded_image}
            pokemons_list.append(pokemon)

        pokemons = {"pokemons": pokemons_list}
        mongo_server_response = requests.post("http://images_server-images-server-1:5002/images/migration", json=pokemons)
        return mongo_server_response.json()

requests_handler = RequestsHandler()