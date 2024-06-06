from fastapi import APIRouter, Depends, HTTPException, status
from models.pokemon import Pokemon
import utils.get_functions as get_functions
import utils.insert_functions as insert_functions
router = APIRouter()

@router.post('/pokemon')
def add_pokemon(pokemon: Pokemon):
    """
    Post new pokemon to the database

    Parameters:
    - pokemon: the pokemon object.
    """
    pokemon_obj = get_functions.get_pokemon(pokemon.name)
    if pokemon_obj:
        raise HTTPException(status_code=400, detail="Pokemon already exists")
    
    insert_functions.insert_pokemon(pokemon.model_dump())
    return {status.HTTP_200_OK: "Pokemon added successfully"}
@router.get('/pokemons/type')
def get_pokemon_by_type(type: str):
    """
    get pokemons to of the given type

    Parameters:
    - type: the type of the pokemon.
    """
    pokemons = get_functions.get_pokemons_by_type(type)
    if not pokemons or len(pokemons) == 0:
        raise HTTPException(status_code=404, detail="Pokemons with this type not found")
    return pokemons

@router.get('/pokemons/trainer')
def get_pokemon_by_trainer(trainer_name: str):
    """
    get pokemons to of the given trainer

    Parameters:
    - trainer: the trainer of the pokemon.
    """
    trainer = get_functions.get_trainer_by_name(trainer_name)
    trainer_id = trainer['_id']
    return get_functions.get_pokemons_by_trainer(trainer_id)
