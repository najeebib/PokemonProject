from fastapi import APIRouter
from models.trainer import Trainer
from classes.requests_handler import requests_handler


router = APIRouter()

@router.post('/trainer')
def add_trainer(trainer: Trainer):
    return requests_handler.add_trainer(trainer)

@router.get('/trainers/{pokemon_name}')
def get_trainers(pokemon_name: str):
    return requests_handler.get_trainers(pokemon_name)

@router.post('/trainer/{trainer_name}/pokemon')
def add_trainer_to_pokemon(trainer_name: str, pokemon_name: str):
    return requests_handler.add_pokemon_to_trainer(trainer_name, pokemon_name)


@router.delete('/trainer/{trainer_name}/pokemon')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
    return requests_handler.delete_pokemon_from_trainer(trainer_name, pokemon_name)