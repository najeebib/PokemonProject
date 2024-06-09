import requests
from models.pokemon import Pokemon
from models.trainer import Trainer

class RequestsHandler:
    def __init__(self):
        pass

    def get_pokemon(self, pokemon_name):
        response = requests.get(f"http://pokemon_api-mypokemonserver-1:5000/pokemon?pokemon_name={pokemon_name}")
        return response.json()
    
    def add_pokemon(self, pokemon: Pokemon):
        response = requests.post("http://pokemon_api-mypokemonserver-1:5000/pokemon", json=pokemon.model_dump())
        return response.json()
    
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
    
    def add_pokemon_to_trainer(trainer_name: str, pokemon_name: str):
        response = requests.post(f"http://pokemon_api-mypokemonserver-1:5000/trainer/{trainer_name}/pokemon?pokemon_name={pokemon_name}")
        return response.json()
    
    def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
        response = requests.delete(f"http://pokemon_api-mypokemonserver-1:5000/trainer/{trainer_name}/pokemon?pokemon_name={pokemon_name}")
        return response.json()
    
    def evolution(trainer_name: str, pokemon_name: str, next_evolution: str):
        response = requests.put(f"http://pokemon_api-mypokemonserver-1:5000/evolution?trainer_name={trainer_name}&pokemon_name={pokemon_name}&next_evolution={next_evolution}")
        return response.json()


requests_handler = RequestsHandler()