from fastapi import APIRouter, HTTPException
from classes.requests_handler import requests_handler
import api.evolution_fns as evolve_functions

router = APIRouter()

@router.put('/evolution')
def evolve(trainer_name: str, pokemon_name: str):
    try:
        if type(trainer_name) == str and type(pokemon_name) == str:
            chain = evolve_functions.get_evolution_chain(pokemon_name)
            next_evolution = evolve_functions.get_next_evolution(chain, pokemon_name)

            return requests_handler.evolution(trainer_name, pokemon_name, next_evolution)
        raise HTTPException(400, detail="Ivalid pokemon or trainer name")
    except Exception:
        raise HTTPException(500, detail="Server error")
