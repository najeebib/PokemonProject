from fastapi import APIRouter, HTTPException
from classes.requests_handler import requests_handler
import api.evolution_fns as evolve_functions
from redis_client.redis import rd
router = APIRouter()

@router.put('/evolution')
def evolve(trainer_name: str, pokemon_name: str):
    """
    Send request to the pokemon api to evolve the given pokemon of the given trainer.
    After the pokemon was evolved, delete the pokemons and trainers data from the cache since it's no longer accurate

    Parameters:
    - pokemon_name: name of the pokemon.
    - trainer_name: name of the trainer.
    """
    if type(trainer_name) == str and type(pokemon_name) == str:
        chain = evolve_functions.get_evolution_chain(pokemon_name)
        next_evolution = evolve_functions.get_next_evolution(chain, pokemon_name)
        next_pokemon = evolve_functions.get_pokemon_details(next_evolution)

        response = requests_handler.evolution(trainer_name, pokemon_name, next_evolution)

        trainers_url = f"/trainers/{pokemon_name}"
        pokemon_url = f"/pokemons/trainers/{trainer_name}"
        pokemon_types_url = f"/pokemons/types/{next_pokemon['type']}"
        rd.delete(pokemon_types_url)
        rd.delete(trainers_url)
        rd.delete(pokemon_url)
        
        return response
    raise HTTPException(400, detail="Ivalid pokemon or trainer name")
