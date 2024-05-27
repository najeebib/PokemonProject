from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
import data.models as models
from data.database import engine, session_local
from sqlalchemy.orm import Session
from data.database import get_db
from sqlalchemy import text
from models.trainer import Trainer
from models.pokemon import Pokemon
import utils.sql_queries as fns
import utils.select_queries as select_fns
import utils.delete_queries as delete_fns
import utils.evolution_fns as evolve_fns
import requests
router = APIRouter()

@router.post('/addPokemon')
def add_pokemon(pokemon: Pokemon, db: Session = Depends(get_db)):
    if not fns.is_pokemon_in_table(db, pokemon.name):
        fns.insert_into_pokemons_table(db,name=pokemon.name, height=pokemon.height, weight=pokemon.weight )

    if not fns.is_type_in_table(db, type=pokemon.type):
        fns.insert_into_types_table(db, [pokemon.type])

    pokemon_obj = select_fns.select_pokemon(db, pokemon.name)
    pokemon_id = pokemon_obj.pokemon_id

    type_obj = select_fns.select_type(db, pokemon.type)
    type_id = type_obj.types_id

    if not fns.is_in_pokemontype(db, pokemon_id, type_id):
        fns.insert_into_PokemonTypes_table(db, pokemon_id, type_id)

@router.post('/addTrainer')
def add_pokemon(trainer: Trainer, db: Session = Depends(get_db)):
    if not fns.is_trainer_in_table(db, trainer.name):
        fns.insert_into_trainers_table(db, trainer.name, trainer.town)

@router.get('/pokemonByType/{type}')
def get_pokemon_by_type(type: str,db: Session = Depends(get_db)):
    return select_fns.select_pokemons_by_type(db, type)

@router.get('/pokemonByTrainer/{trainer_name}')
def get_pokemon_by_trainer(trainer_name: str, db: Session = Depends(get_db)):
    return select_fns.slecte_pokemons_by_trainer(db, trainer_name)

@router.get('/trainersOfPokemon/{pokemon_name}')
def get_trainers(pokemon_name: str, db: Session = Depends(get_db)):
    return select_fns.select_trainers_by_pokemonName(db, pokemon_name)

@router.delete('/deletePokemonFromTrainer')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    pokemon = select_fns.select_pokemon(db, pokemon_name)
    trainer = select_fns.select_trainer(db, trainer_name)

    pokemon_id, trainer_id = pokemon.pokemon_id, trainer.trainer_id
    if pokemon and trainer and fns.is_in_pokedex(db, pokemon_id, trainer_id):
        delete_fns.delete_from_pokedex(db, pokemon_id, trainer_id)
    else:
        #todo
        pass

@router.post('/addPokemonToTrainer')
def add_pokemon_from_trainer(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    pokemon = select_fns.select_pokemon(db, pokemon_name)
    trainer = select_fns.select_trainer(db, trainer_name)

    if pokemon and trainer:
        pokemon_id, trainer_id = pokemon.pokemon_id, trainer.trainer_id
        if not fns.is_in_pokedex(db, pokemon_id, trainer_id):
            fns.insert_into_Pokedex_table(db, pokemon_id, trainer_id)
        else:
            print("already in")



@router.put('/evolve/{pokemon_name}/{trainer_name}')
def evolve(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    chain = evolve_fns.get_evolution_chain(pokemon_name)
    next_evolution = evolve_fns.get_next_evolution(chain, pokemon_name)
    old_pokemon = select_fns.select_pokemon(db, pokemon_name)
    pokemon = select_fns.select_pokemon(db, next_evolution)
    trainer = select_fns.select_trainer(db, trainer_name)
    if  fns.is_in_pokedex(db, old_pokemon.pokemon_id, trainer.trainer_id) and not fns.is_in_pokedex(db, pokemon.pokemon_id, trainer.trainer_id):
        delete_fns.delete_from_pokedex(db, trainer.trainer_id, old_pokemon.pokemon_id)
        fns.insert_into_Pokedex_table(db, pokemon.pokemon_id, trainer.trainer_id)
    else:
        raise HTTPException(403, detail="Cant evolve this pokemon")
            
