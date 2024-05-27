from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.orm import Session
from .sql_queries import is_in_pokedex


def delete_from_pokedex(db: Session, trainer_id: int, pokemon_id: int):
    if is_in_pokedex(db, pokemon_id, trainer_id):
        db.execute(text(f"DELETE FROM `pokedex` WHERE pokemon_id = {pokemon_id} AND trainer_id = {trainer_id}"))
        db.commit()

    else:
        raise Exception("Pokemon not in pokedex")