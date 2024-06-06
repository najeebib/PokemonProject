from fastapi import APIRouter, Depends, HTTPException, status
from models.trainer import Trainer
import utils.get_functions as get_functions
import utils.insert_functions as insert_functions
import utils.update_functions as update_functions
router = APIRouter()

@router.get('/trainers/{pokemon_name}')
def get_trainers(pokemon_name: str):
    """
    get trainers to of the given pokemon

    Parameters:
    - pokemon_name: the pokemon name.
    """
    pokemon = get_functions.get_pokemon(pokemon_name)
    print(type(pokemon))
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    pokemon_trainers = pokemon['trainers']

    all_trainers = []
    for trainer in pokemon_trainers:
        all_trainers.append(get_functions.get_trainer_by_id(str(trainer)))
    return all_trainers

@router.post('/trainer')
def add_trainer(trainer: Trainer):
    """
    Insert new trainer to the database

    Parameters:
    - trainer: the trainer object.
    """
    trainer_obj = get_functions.get_trainer_by_name(trainer.name)
    if trainer_obj:
        raise HTTPException(status_code=409, detail="Trainer already exists")
    
    insert_functions.insert_trainer(trainer.model_dump())
    return {status.HTTP_200_OK: "Trainer added successfully"}

@router.post('/trainer/{trainer_name}/pokemon')
def add_pokemon_to_trainer(trainer_name: str, pokemon_name: str):
    """
    Insert new trainer pokemon to the trainer

    Parameters:
    - trainer_name: trainer name.
    - pokemon_name: pokemon name.
    """
    pokemon = get_functions.get_pokemon(pokemon_name)
    trainer = get_functions.get_trainer_by_name(trainer_name)
    if not pokemon or not trainer:
        raise HTTPException(status_code=404, detail="Pokemon or Trainer not found")
    
    trainer_id = trainer['_id']
    trainer_pokemons = get_functions.get_pokemons_by_trainer(trainer_id)
    for poke in trainer_pokemons:
        if poke["_id"] == pokemon["_id"]:
            raise HTTPException(status_code=409, detail="Trainer already has this pokemon")
        
    
    update_functions.add_trainer_to_pokemon(pokemon_name, trainer_id)
    return {status.HTTP_200_OK: "Pokemon added to trainer successfully"}

@router.delete('/trainer/{trainer_name}/pokemon')
def delete_pokemon_from_trainer(trainer_name: str, pokemon_name: str):
    """
    delete  pokemon from the trainer

    Parameters:
    - trainer_name: trainer name.
    - pokemon_name: pokemon name.
    """
    pokemon = get_functions.get_pokemon(pokemon_name)
    trainer = get_functions.get_trainer_by_name(trainer_name)
    if not pokemon or not trainer:
        raise HTTPException(status_code=404, detail="Pokemon or Trainer not found")
    
    trainer_id = trainer['_id']
    trainer_pokemons = get_functions.get_pokemons_by_trainer(trainer_id)
    trainer_has_pokemon = False
    for poke in trainer_pokemons:
        if poke["_id"] == pokemon["_id"]:
            trainer_has_pokemon = True
    if not trainer_has_pokemon:
        raise HTTPException(status_code=404, detail="Trainer does not have this pokemon")
    
    update_functions.delete_trainer_to_pokemon(pokemon_name, trainer_id)
    return {status.HTTP_200_OK: "Pokemon deleted from trainer successfully"}
