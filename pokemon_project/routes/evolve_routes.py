from fastapi import APIRouter, Depends, HTTPException, status
import requests

router = APIRouter()

@router.put('/evolution')
def evolve(trainer_name: str, pokemon_name: str):
    response = requests.put(f"http://localhost:5000/evolution?trainer_name={trainer_name}&pokemon_name={pokemon_name}")
    return response.json()
