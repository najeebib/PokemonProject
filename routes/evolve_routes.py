from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data.database import get_db
import utils.sql_queries as fns
import utils.select_queries as select_fns
import utils.delete_queries as delete_fns
import utils.evolution_fns as evolve_fns
import utils.insert_queries as insert_fns

router = APIRouter()

@router.put('/evolution')
def evolve(trainer_name: str, pokemon_name: str, db: Session = Depends(get_db)):
    if fns.is_pokemon_in_table(db, pokemon_name) and fns.is_trainer_in_table(db, trainer_name):
        chain = evolve_fns.get_evolution_chain(pokemon_name)
        next_evolution = evolve_fns.get_next_evolution(chain, pokemon_name)
        if next_evolution:
            old_pokemon = select_fns.select_pokemon(db, pokemon_name)
            pokemon = select_fns.select_pokemon(db, next_evolution)
            trainer = select_fns.select_trainer(db, trainer_name)
            if  fns.is_in_pokedex(db, old_pokemon.pokemon_id, trainer.trainer_id) and not fns.is_in_pokedex(db, pokemon.pokemon_id, trainer.trainer_id):
                delete_fns.delete_from_pokedex(db,old_pokemon.pokemon_id, trainer.trainer_id )
                insert_fns.insert_into_Pokedex_table(db, pokemon.pokemon_id, trainer.trainer_id)
                return {f"Status code: {status.HTTP_200_OK}","Evolution was successfull"}
            else:
                raise HTTPException(409, detail="Cant evolve this pokemon")
        else:
            raise HTTPException(403, detail="No evoilution possible")
    else:
        raise HTTPException(404, detail="Pokemon/Trainer not found")