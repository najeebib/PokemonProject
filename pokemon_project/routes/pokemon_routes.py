from fastapi import APIRouter, HTTPException
from models.pokemon import Pokemon
from classes.requests_handler import requests_handler
router = APIRouter()

@router.get('/pokemon')
def get_pokemon(pokemon_name: str):
    try:
        if type(pokemon_name) == str:
            return requests_handler.get_pokemon(pokemon_name)
        raise HTTPException(400, detail="Ivalid pokemon name")
    except Exception:
        raise HTTPException(500, detail="Server error")

@router.post('/pokemon')
def add_pokemon(pokemon: Pokemon):
    try:
        status = requests_handler.add_pokemon(pokemon)
        if status == 201:
            return {f"Status code: {status}","pokemon was added to the database"}
        return status
    except Exception:
        raise HTTPException(500, detail="Server error")
    

@router.get('/pokemons/type')
def get_pokemon_by_type(type: str):
    try:
        if type(type) == str:
            return requests_handler.get_pokemons_by_type(type)
        raise HTTPException(400, detail="Ivalid pokemon type")
    except Exception:
        raise HTTPException(500, detail="Server error")

@router.get('/pokemons/trainer')
def get_pokemon_by_trainer(trainer_name: str):
    try:
        if type(trainer_name) == str:
            return requests_handler.get_pokemons_by_trainer(trainer_name)
        raise HTTPException(400, detail="Ivalid trainer name")
    except Exception:
        raise HTTPException(500, detail="Server error")