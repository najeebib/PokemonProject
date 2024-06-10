from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data.database import get_db
from models.trainer import Trainer
import utils.sql_queries as check_functions
import utils.get_queries as select_functions
import utils.delete_queries as delete_functions
import utils.insert_queries as insert_functions

router = APIRouter()

@router.get('/trainers/{pokemon_name}')
def get_trainers(pokemon_name: str, db: Session = Depends(get_db)):
    """
    get trainers to of the given pokemon

    Parameters:
    - pokemon_name: the pokemon name.
    """
    return select_functions.select_trainers_by_pokemonName(db, pokemon_name)

@router.post('/trainer')
def add_trainer(trainer: Trainer, db: Session = Depends(get_db)):
    """
    Insert new trainer to the database

    Parameters:
    - trainer: the trainer object.
    """
    if not check_functions.is_trainer_in_table(db, trainer.name):
        insert_functions.insert_into_trainers_table(db, trainer.name, trainer.town)
        return {f"Status code: {status.HTTP_201_CREATED}","trainer was added to the database"}
    else:
        raise HTTPException(409, detail="Trainer already exists")

@router.post('/trainer/{trainer_name}/pokemon')
def add_pokemon_to_trainer(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    """
    Insert new trainer pokemon to the trainer

    Parameters:
    - trainer_name: trainer name.
    - pokemon_name: pokemon name.
    """
    pokemon = select_functions.select_pokemon(db, pokemon_name)
    trainer = select_functions.select_trainer(db, trainer_name)

    if pokemon and trainer:
        pokemon_id, trainer_id = pokemon.pokemon_id, trainer.trainer_id
        if not check_functions.is_in_pokedex(db, pokemon_id, trainer_id):
            insert_functions.insert_into_Pokedex_table(db, pokemon_id, trainer_id)
            return {f"Status code: {status.HTTP_201_CREATED}","pokemon was added to the trainer"}
        else:
             raise HTTPException(403, detail="Trainer already has this pokemon")

@router.delete('/trainer/{trainer_name}/pokemon')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    """
    delete  pokemon from the trainer

    Parameters:
    - trainer_name: trainer name.
    - pokemon_name: pokemon name.
    """
    pokemon = select_functions.select_pokemon(db, pokemon_name)
    trainer = select_functions.select_trainer(db, trainer_name)

    pokemon_id, trainer_id = pokemon.pokemon_id, trainer.trainer_id
    if pokemon and trainer and check_functions.is_in_pokedex(db, pokemon_id, trainer_id):
        delete_functions.delete_from_pokedex(db, pokemon_id, trainer_id)
        return {f"Status code: {status.HTTP_200_OK}","pokemon was deleted from the trainer"}
    else:
        raise HTTPException(404, detail="Trainer doesn't have this pokemon")