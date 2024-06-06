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
    
    trainer_id = trainer['_id']
    trainer_pokemons = get_functions.get_pokemons_by_trainer(trainer_id)
    trainer_has_pokemon = False
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
        raise HTTPException(403, detail="No evoilution possible")
    
    next_pokemon = get_functions.get_pokemon(next_evolution)
    if not next_pokemon:
        insert_functions.insert_pokemon(evolve_functions.get_pokemon_details(next_evolution))
        next_pokemon = get_functions.get_pokemon(next_evolution)
    update_functions.delete_trainer_to_pokemon(pokemon_name, trainer["_id"])
    update_functions.add_trainer_to_pokemon(next_evolution, trainer["_id"])
    return {status.HTTP_200_OK: "Evolution successful"}
    # check if there is a possible evolution, if not return 403
    # get trainer id
    # check if trainer has the next evolution, if he has return 409
    # check if next evolution is in pokemons table, if not add it
    # remove trainer id from pokemon by name and add trainer id to next evolution by name
    """
    #Check if pokemon and trainer exist
    if not check_functions.is_pokemon_in_table(db, pokemon_name) and not check_functions.is_trainer_in_table(db, trainer_name):
        raise HTTPException(404, detail="Pokemon/Trainer not found")
    #Get evolution chain
    chain = evolve_functions.get_evolution_chain(pokemon_name)
    next_evolution = evolve_functions.get_next_evolution(chain, pokemon_name)
    #Check if evolution is possible
    if not next_evolution:
        raise HTTPException(403, detail="No evoilution possible")
    old_pokemon = select_check_functions.select_pokemon(db, pokemon_name)
    pokemon = select_check_functions.select_pokemon(db, next_evolution)
    trainer = select_check_functions.select_trainer(db, trainer_name)
    #Check if pokemon is already in the pokedex
    if  check_functions.is_in_pokedex(db, old_pokemon.pokemon_id, trainer.trainer_id) and not check_functions.is_in_pokedex(db, pokemon.pokemon_id, trainer.trainer_id):
        delete_functions.delete_from_pokedex(db,old_pokemon.pokemon_id, trainer.trainer_id )
        insert_functions.insert_into_Pokedex_table(db, pokemon.pokemon_id, trainer.trainer_id)
        return {f"Status code: {status.HTTP_200_OK}","Evolution was successfull"}
    else:
        raise HTTPException(409, detail="Cant evolve this pokemon")
    """