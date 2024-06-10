from fastapi import APIRouter
from models.pokemon import Pokemon
from classes.requests_handler import requests_handler
router = APIRouter()

@router.get('/pokemon')
def get_pokemon(pokemon_name: str):
    return requests_handler.get_pokemon(pokemon_name)

@router.post('/pokemon')
def add_pokemon(pokemon: Pokemon):
    status = requests_handler.add_pokemon(pokemon)
    if status == 201:
        return {f"Status code: {status}","pokemon was added to the database"}
    return status
    

@router.get('/pokemons/type')
def get_pokemon_by_type(type: str):
    return requests_handler.get_pokemons_by_type(type)

@router.get('/pokemons/trainer')
def get_pokemon_by_trainer(trainer_name: str):
    return requests_handler.get_pokemons_by_trainer(trainer_name)