from fastapi import APIRouter, HTTPException
from models.pokemon import Pokemon
from classes.requests_handler import requests_handler
from redis_client.redis import rd
import json
router = APIRouter()

@router.get('/pokemons/{pokemon_id:int}')
def get_pokemon(pokemon_id: int):
    """
    Check if the user is in the cache if not Send request to pokemon server to get pokemon from the database

    Parameters:
    - pokemon_name: the pokemon name.
    """
    try:
        if type(pokemon_id) != int:
            raise HTTPException(400, detail="Ivalid pokemon name")
        url_key = f"/pokemons/{pokemon_id}"
        cache = rd.get(url_key)
        if cache:
            return json.loads(cache)
        else:
            response = requests_handler.get_pokemon_by_id(pokemon_id)
            rd.set(url_key, json.dumps(response))
            return response
    except Exception:
        raise HTTPException(500, detail="Server error")

@router.get('/pokemons/{pokemon_name:str}')
def get_pokemon(pokemon_name: str):
    """
    Check if the user is in the cache if not Send request to pokemon server to get pokemon from the database

    Parameters:
    - pokemon_name: the pokemon name.
    """
    try:
        if type(pokemon_name) != str:
            raise HTTPException(400, detail="Ivalid pokemon name")
        url_key = f"/pokemons/{pokemon_name}"
        cache = rd.get(url_key)
        if cache:
            return json.loads(cache)
        else:
            response = requests_handler.get_pokemon_by_name(pokemon_name)
            rd.set(url_key, json.dumps(response))
            return response
    except Exception:
        raise HTTPException(500, detail="Server error")

@router.post('/pokemons')
def add_pokemon(pokemon: Pokemon):
    """
    Send request to pokemon server to post new pokemon to the database
    After the pokemon was added to the database, delete the pokemon type from the cache since it's no longer accurate

    Parameters:
    - pokemon: the pokemon object.
    """
    status = requests_handler.add_pokemon(pokemon)
    if status == 201:
        response = {f"Status code: {status}","pokemon was added to the database"}
        pokemon_types_url = f"/pokemons/types/{pokemon.type}"
        rd.delete(pokemon_types_url)
        return response
    return status
    

@router.get('/pokemons/types/{pokemon_type}')
def get_pokemon_by_type(pokemon_type: str):
    """
    Check if the pokemons are in the cache if not Send request to pokemon server to get pokemons by type from the database

    Parameters:
    - pokemon_type: the pokemon type.
    """
    if type(pokemon_type) != str:
        raise HTTPException(400, detail="Ivalid pokemon type")
    url_key = f"/pokemons/types/{pokemon_type}"
    cache = rd.get(url_key)
    if cache:
        return json.loads(cache)
    else:
        response =  requests_handler.get_request(f"http://pokemon_api-pokemon-api-1:5001/pokemons/types/{pokemon_type}")
        rd.set(url_key, json.dumps(response))
        return response

@router.get('/pokemons/trainers/{trainer_name}')
def get_pokemon_by_trainer(trainer_name: str):
    """
    Check if the pokemons are in the cache if not Send request to pokemon server to get pokemons by trainer from the database

    Parameters:
    - trainer_name: the trainer name.
    """
    if type(trainer_name) != str:
        raise HTTPException(400, detail="Ivalid trainer name")
    url_key = f"/pokemons/trainers/{trainer_name}"
    cache = rd.get(url_key)
    if cache:
        return json.loads(cache)
    else:
        response = requests_handler.get_request(f"http://pokemon_api-pokemon-api-1:5001/pokemons/trainers/{trainer_name}")
        rd.set(url_key, json.dumps(response))
        return response