from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data.database import get_db
from models.pokemon import Pokemon
import utils.sql_queries as check_functions
import utils.get_queries as select_functions
import utils.insert_queries as insert_functions

router = APIRouter()

@router.get('/pokemon')
def get_pokemon(pokemon_name: str, db: Session = Depends(get_db)):
    """
    Get pokemon from the database

    Parameters:
    - pokemon_name: the pokemon name.
    """
    return select_functions.select_pokemon(db, pokemon_name)

@router.post('/pokemon')
def add_pokemon(pokemon: Pokemon, db: Session = Depends(get_db)):
    """
    Post new pokemon to the database

    Parameters:
    - pokemon: the pokemon object.
    """
    if not check_functions.is_pokemon_in_table(db, pokemon.name):
        insert_functions.insert_into_pokemons_table(db,name=pokemon.name, height=pokemon.height, weight=pokemon.weight)
    else:
        raise HTTPException(409, detail="Pokemon already exists")
    if not check_functions.is_type_in_table(db, pokemon.type):
        insert_functions.insert_into_types_table(db, [pokemon.type])

    pokemon_obj = select_functions.select_pokemon(db, pokemon.name)
    pokemon_id = pokemon_obj.pokemon_id

    type_obj = select_functions.select_type(db, pokemon.type)
    type_id = type_obj.types_id

    if not check_functions.is_in_pokemontype(db, pokemon_id, type_id):
        insert_functions.insert_into_PokemonTypes_table(db, pokemon_id, type_id)
        return {f"Status code: {status.HTTP_201_CREATED}","pokemon was added to the database"}

@router.get('/pokemons/type')
def get_pokemon_by_type(type: str,db: Session = Depends(get_db)):
    """
    get pokemons to of the given type

    Parameters:
    - type: the type of the pokemon.
    """
    return select_functions.select_pokemons_by_type(db, type)

@router.get('/pokemons/trainer')
def get_pokemon_by_trainer(trainer_name: str, db: Session = Depends(get_db)):
    """
    get pokemons to of the given trainer

    Parameters:
    - trainer: the trainer of the pokemon.
    """
    return select_functions.slecte_pokemons_by_trainer(db, trainer_name)