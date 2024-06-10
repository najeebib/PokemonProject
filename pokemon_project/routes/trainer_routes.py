from fastapi import APIRouter, HTTPException
from models.trainer import Trainer
from classes.requests_handler import requests_handler


router = APIRouter()

@router.post('/trainer')
def add_trainer(trainer: Trainer):
    try:
        if type(trainer) == Trainer:
            return requests_handler.add_trainer(trainer)
        raise HTTPException(400, detail="Ivalid pokemon name")
    except Exception:
        raise HTTPException(500, detail="Server error")

@router.get('/trainer/{pokemon_name}')
def get_trainers(pokemon_name: str):
    try:
        if type(pokemon_name) == str:
            return requests_handler.get_trainers(pokemon_name)
        raise HTTPException(400, detail="Ivalid pokemon name")
    except Exception:
        raise HTTPException(500, detail="Server error")

@router.post('/trainer/{trainer_name}/pokemon')
def add_trainer_to_pokemon(trainer_name: str, pokemon_name: str):
    try:
        if type(trainer_name) == str and type(pokemon_name) == str:
            return requests_handler.add_pokemon_to_trainer(trainer_name, pokemon_name)
        raise HTTPException(400, detail="Ivalid pokemon or trainer name")
    except Exception:
        raise HTTPException(500, detail="Server error")


@router.delete('/trainer/{trainer_name}/pokemon')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
    try:
        if type(trainer_name) == str and type(pokemon_name) == str:
            return requests_handler.delete_pokemon_from_trainer(trainer_name, pokemon_name)
        raise HTTPException(400, detail="Ivalid pokemon or trainer name")
    except Exception:
        raise HTTPException(500, detail="Server error")