from fastapi import APIRouter, HTTPException
from models.trainer import Trainer
from classes.requests_handler import requests_handler
from redis_client.redis import rd
import json

router = APIRouter()

@router.post('/trainer')
def add_trainer(trainer: Trainer):
    """
    Send request to pokemon server to add trainer to db

    Parameters:
    - trainer: the Trainer object.
    """
    if type(trainer) == Trainer:
        return requests_handler.add_trainer(trainer)
    raise HTTPException(400, detail="Ivalid trainer")

@router.get('/trainers')
def get_trainers(pokemon_name: str):
    """
    Send request to pokemon server to get trainers by pokemon name from the database

    Parameters:
    - trainer: the trainer object.
    """
    if type(pokemon_name) != str:
        raise HTTPException(400, detail="Ivalid pokemon name")
    url_key = f"/trainers?pokemon_name={pokemon_name}"
    cache = rd.get(url_key)
    if cache:
        return json.loads(cache)
    else:
        response = requests_handler.get_request("http://pokemon_api-mypokemonserver-1:5000/trainers", pokemon_name=pokemon_name)
        rd.set(url_key, json.dumps(response))
        return response

@router.post('/trainer/pokemon')
def add_trainer_to_pokemon(trainer_name: str, pokemon_name: str):
    """
    Send request to pokemon server to insert new trainer pokemon to the trainer

    Parameters:
    - trainer_name: trainer name.
    - pokemon_name: pokemon name.
    """
    
    try:
        if type(trainer_name) == str and type(pokemon_name) == str:
            response = requests_handler.add_pokemon_to_trainer(trainer_name, pokemon_name)
            trainers_url = f"/trainers?pokemon_name={pokemon_name}"
            pokemon_url = f"/pokemons/trainer?trainer_name={trainer_name}"
            rd.delete(trainers_url)
            rd.delete(pokemon_url)
            return response
        raise HTTPException(400, detail="Ivalid pokemon or trainer name")
    except Exception:
        raise HTTPException(500, detail="Server error")


@router.delete('/trainer/pokemon')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
    """
    Send request to pokemon server to delete  pokemon from the trainer

    Parameters:
    - trainer_name: trainer name.
    - pokemon_name: pokemon name.
    """
    if type(trainer_name) == str and type(pokemon_name) == str:
        response = requests_handler.delete_pokemon_from_trainer(trainer_name, pokemon_name)
        trainers_url = f"/trainers?pokemon_name={pokemon_name}"
        pokemon_url = f"/pokemons/trainer?trainer_name={trainer_name}"
        rd.delete(trainers_url)
        rd.delete(pokemon_url)
        return response
    raise HTTPException(400, detail="Ivalid pokemon or trainer name")
