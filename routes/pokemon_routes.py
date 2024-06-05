from fastapi import APIRouter, Depends, HTTPException, status
from models.pokemon import Pokemon

router = APIRouter()

@router.post('/pokemon')
def add_pokemon(pokemon: Pokemon):
    """
    Post new pokemon to the database

    Parameters:
    - pokemon: the pokemon object.
    """
    # find one pokemon by name
    pass
@router.get('/pokemons/type')
def get_pokemon_by_type(type: str):
    """
    get pokemons to of the given type

    Parameters:
    - type: the type of the pokemon.
    """
    #return pokemon by type

    pass

@router.get('/pokemons/trainer')
def get_pokemon_by_trainer(trainer_name: str):
    """
    get pokemons to of the given trainer

    Parameters:
    - trainer: the trainer of the pokemon.
    """
    # get trainer id by poekom name
    # return pokemons by trainer trainer id
    pass