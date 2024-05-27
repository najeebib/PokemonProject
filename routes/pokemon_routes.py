from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
import data.models as models
from data.database import engine, session_local
from sqlalchemy.orm import Session
from data.database import get_db
from sqlalchemy import text
from models.trainer import Trainer
from models.pokemon import Pokemon


router = APIRouter()

@router.post('/addPokemon')
def add_pokemon(pokemon: Pokemon, trainer: Trainer, db: Session = Depends(get_db)):
    # Add a pokemon to the pokemons db

    pass

@router.get('/pokemonByType')
def get_pokemon_by_type(type: str,db: Session = Depends(get_db)):
    # get pokemon by type

    pass

@router.get('/pokemonByTrainer')
def get_pokemon_by_trainer(trainer_name: str, db: Session = Depends(get_db)):
    # get pokemon by trainer

    pass

@router.get('/trainersOfPokemon')
def get_trainers(pokemon_name: str, db: Session = Depends(get_db)):
    # get all trainers by pokemon

    pass

@router.delete('/deletePokemonFromTrainer')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    # delete pokemon from a trainer

    pass

@router.post('/addPokemonToTrainer')
def add_pokemon_from_trainer(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    # add pokemon to a trainer

    pass

@router.put('/evolve')
def evolve(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    # evolve a trainers pokemon

    pass
