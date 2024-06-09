from fastapi import APIRouter
from classes.requests_handler import requests_handler

router = APIRouter()

@router.put('/evolution')
def evolve(trainer_name: str, pokemon_name: str):
    return requests_handler.evolution(trainer_name, pokemon_name)
