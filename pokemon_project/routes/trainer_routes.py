import requests
from fastapi import APIRouter, Depends, HTTPException, status
from models.trainer import Trainer



router = APIRouter()

@router.post('/trainer')
def add_trainer(trainer: Trainer):
    response = requests.post("http://localhost:5000/trainer", json=trainer.model_dump())
    return response.json()

@router.get('/trainers/{pokemon_name}')
def get_trainers(pokemon_name: str):
    response = requests.get(f"http://localhost:5000/trainers/{pokemon_name}")
    return response.json()

@router.post('/trainer/{trainer_name}/pokemon')
def add_trainer(trainer_name: str, pokemon_name: str):
    response = requests.post(f"http://localhost:5000/trainer/{trainer_name}/pokemon?pokemon_name={pokemon_name}")
    return response.json()


@router.delete('/trainer/{trainer_name}/pokemon')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
    response = requests.delete(f"http://localhost:5000/trainer/{trainer_name}/pokemon?pokemon_name={pokemon_name}")
    return response.json()