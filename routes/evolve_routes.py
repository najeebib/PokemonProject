from fastapi import APIRouter, Depends, HTTPException, status
import utils.get_functions as get_functions
import utils.insert_functions as insert_functions
import utils.update_functions as update_functions
import api.evolution_fns as evolve_functions
router = APIRouter()

@router.put('/evolution')
def evolve(trainer_name: str, pokemon_name: str):
    """
    Evolve the given pokemon of the given trainer.

    Parameters:
    - pokemon_name: name of the pokemon.
    - trainer_name: name of the trainer.
    """
    pokemon = get_functions.get_pokemon(pokemon_name)
    trainer = get_functions.get_trainer_by_name(trainer_name)
    if not pokemon or not trainer:
        raise HTTPException(status_code=404, detail="Pokemon or Trainer not found")
    # get the trainer's pokemons
    trainer_id = trainer['_id']
    trainer_pokemons = get_functions.get_pokemons_by_trainer(trainer_id)
    trainer_has_pokemon = False
    # check if trainer has the pokemon
    for poke in trainer_pokemons:
        if poke["_id"] == pokemon["_id"]:
            trainer_has_pokemon = True
    if not trainer_has_pokemon:
        raise HTTPException(status_code=404, detail="Trainer does not have this pokemon")
    
    chain = evolve_functions.get_evolution_chain(pokemon_name)
    next_evolution = evolve_functions.get_next_evolution(chain, pokemon_name)

    next_pokemon = get_functions.get_pokemon(next_evolution)
    #Check if evolution is possible
    if not next_evolution:
        raise HTTPException(409, detail="No evoilution possible")
    
    next_pokemon = get_functions.get_pokemon(next_evolution)
    if not next_pokemon:
        insert_functions.insert_pokemon(evolve_functions.get_pokemon_details(next_evolution))
        next_pokemon = get_functions.get_pokemon(next_evolution)
    update_functions.delete_trainer_to_pokemon(pokemon_name, trainer["_id"])
    update_functions.add_trainer_to_pokemon(next_evolution, trainer["_id"])
    return {status.HTTP_200_OK: "Evolution successful"}
    