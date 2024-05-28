from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data.database import get_db
from models.pokemon import Pokemon
import utils.sql_queries as fns
import utils.select_queries as select_fns
import utils.insert_queries as insert_fns

router = APIRouter()

@router.post('/pokemon')
def add_pokemon(pokemon: Pokemon, db: Session = Depends(get_db)):
    if not fns.is_pokemon_in_table(db, pokemon.name):
        insert_fns.insert_into_pokemons_table(db,name=pokemon.name, height=pokemon.height, weight=pokemon.weight)
    else:
        raise HTTPException(403, detail="Pokemon already exists")
    if not fns.is_type_in_table(db, type=pokemon.type):
        insert_fns.insert_into_types_table(db, [pokemon.type])

    pokemon_obj = select_fns.select_pokemon(db, pokemon.name)
    pokemon_id = pokemon_obj.pokemon_id

    type_obj = select_fns.select_type(db, pokemon.type)
    type_id = type_obj.types_id

    if not fns.is_in_pokemontype(db, pokemon_id, type_id):
        insert_fns.insert_into_PokemonTypes_table(db, pokemon_id, type_id)
        return {f"Status code: {status.HTTP_201_CREATED}","pokemon was added to the database"}

@router.get('/by-type/{type}')
def get_pokemon_by_type(type: str,db: Session = Depends(get_db)):
    return select_fns.select_pokemons_by_type(db, type)

@router.get('/by-traienr/{trainer_name}')
def get_pokemon_by_trainer(trainer_name: str, db: Session = Depends(get_db)):
    return select_fns.slecte_pokemons_by_trainer(db, trainer_name)