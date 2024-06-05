from fastapi import APIRouter, Depends, HTTPException, status
router = APIRouter()

@router.put('/evolution')
def evolve(trainer_name: str, pokemon_name: str):
    """
    Evolve the given pokemon of the given trainer.

    Parameters:
    - pokemon_name: name of the pokemon.
    - trainer_name: name of the trainer.
    """
    # check if pokemon and trainer exist, return 404 if either doesn't
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