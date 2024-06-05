from fastapi import APIRouter, Depends, HTTPException, status
from models.trainer import Trainer

router = APIRouter()

@router.get('/trainers/{pokemon_name}')
def get_trainers(pokemon_name: str):
    """
    get trainers to of the given pokemon

    Parameters:
    - pokemon_name: the pokemon name.
    """
    # get trainers ids by pokemon name
    # get trainers by trainers ids
    pass

@router.post('/trainer')
def add_trainer(trainer: Trainer):
    """
    Insert new trainer to the database

    Parameters:
    - trainer: the trainer object.
    """
    # check if trainer is in table
    #else:
    #    raise HTTPException(409, detail="Trainer already exists")

@router.post('/trainer/{trainer_name}/pokemon')
def add_pokemon_to_trainer(trainer_name: str, pokemon_name: str):
    """
    Insert new trainer pokemon to the trainer

    Parameters:
    - trainer_name: trainer name.
    - pokemon_name: pokemon name.
    """
    # get trainer id by trainer name
    # check if pokemon has that trainer id
    # if it has return 403 else add that trainer id to pokemon's trainers list

@router.delete('/trainer/{trainer_name}/pokemon')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
    """
    delete  pokemon from the trainer

    Parameters:
    - trainer_name: trainer name.
    - pokemon_name: pokemon name.
    """
    # get trainer id by trainer name
    # check if pokemon has that trainer id
    # if it doesn't return 404 else delete that trainer id from pokemon's trainers list