import requests
from fastapi import APIRouter, Depends, HTTPException, status
from models.pokemon import Pokemon

router = APIRouter()

@router.post('/pokemon')
def add_pokemon(pokemon: Pokemon):
    response = requests.post("http://localhost:5000/pokemon", json=pokemon.model_dump())
    return response.json()

@router.get('/pokemons/type')
def get_pokemon_by_type(type: str):
    response = requests.get(f"http://localhost:5000/pokemons/type?type={type}")
    return response.json()

@router.get('/pokemons/trainer')
def get_pokemon_by_trainer(trainer_name: str):
    response = requests.get(f"http://localhost:5000/pokemons/trainer?trainer_name={trainer_name}")
    return response.json()