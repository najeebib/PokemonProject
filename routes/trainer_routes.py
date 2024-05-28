from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data.database import get_db
from models.trainer import Trainer
import utils.sql_queries as fns
import utils.select_queries as select_fns
import utils.delete_queries as delete_fns
import utils.insert_queries as insert_fns

router = APIRouter()

@router.get('/trainers/pokemon/{pokemon_name}')
def get_trainers(pokemon_name: str, db: Session = Depends(get_db)):
    return {f"Status code: {status.HTTP_201_CREATED}", select_fns.select_trainers_by_pokemonName(db, pokemon_name)}

@router.post('/trainer')
def add_pokemon(trainer: Trainer, db: Session = Depends(get_db)):
    if not fns.is_trainer_in_table(db, trainer.name):
        insert_fns.insert_into_trainers_table(db, trainer.name, trainer.town)
        return {f"Status code: {status.HTTP_201_CREATED}","trainer was added to the database"}
    else:
        raise HTTPException(403, detail="Trainer already exists")

@router.post('/trainer/pokemon')
def add_pokemon_from_trainer(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    pokemon = select_fns.select_pokemon(db, pokemon_name)
    trainer = select_fns.select_trainer(db, trainer_name)

    if pokemon and trainer:
        pokemon_id, trainer_id = pokemon.pokemon_id, trainer.trainer_id
        if not fns.is_in_pokedex(db, pokemon_id, trainer_id):
            insert_fns.insert_into_Pokedex_table(db, pokemon_id, trainer_id)
            return {f"Status code: {status.HTTP_201_CREATED}","pokemon was added to the trainer"}
        else:
             raise HTTPException(403, detail="Trainer already has this pokemon")

@router.delete('/trainer/pokemon')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    pokemon = select_fns.select_pokemon(db, pokemon_name)
    trainer = select_fns.select_trainer(db, trainer_name)

    pokemon_id, trainer_id = pokemon.pokemon_id, trainer.trainer_id
    if pokemon and trainer and fns.is_in_pokedex(db, pokemon_id, trainer_id):
        delete_fns.delete_from_pokedex(db, pokemon_id, trainer_id)
        return {f"Status code: {status.HTTP_200_OK}","pokemon was deleted from the trainer"}
    else:
        raise HTTPException(404, detail="Trainer doesn't have this pokemon")