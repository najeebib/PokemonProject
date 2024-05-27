from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.orm import Session
from .sql_queries import is_in_pokedex, is_in_pokemontype, is_trainer_in_table, is_pokemon_in_table, is_type_in_table


def delete_from_pokedex(db: Session,pokemon_id: int, trainer_id: int):
    if is_in_pokedex(db, pokemon_id, trainer_id):
        db.execute(text(f"DELETE FROM `pokedex` WHERE pokemon_id = {pokemon_id} AND trainer_id = {trainer_id}"))
        db.commit()
    else:
        raise Exception("Pokemon not in pokedex")
    
def delete_from_pokemontypes(db: Session,pokemon_id: int, type_id: int):
    if is_in_pokemontype(db, pokemon_id, type_id):
        db.execute(text(f"DELETE FROM `pokemontypes` WHERE pokemon_id = {pokemon_id} AND type_id = {type_id}"))
        db.commit()

    else:
        raise Exception("Pokemontype not in pokemontypes table")
    
def delete_from_pokemons(db: Session,pokemon_name: str):
    if is_pokemon_in_table(db, pokemon_name):
        db.execute(text(f"DELETE FROM `pokemons` WHERE name = '{pokemon_name}'"))
        db.commit()

    else:
        raise Exception("Pokemon not in pokemons table")
    
def delete_from_trainer(db: Session,trainer_name: str):
    if is_trainer_in_table(db, trainer_name):
        db.execute(text(f"DELETE FROM `trainers` WHERE name = '{trainer_name}'"))
        db.commit()

    else:
        raise Exception("Trainer not in trainers table")
    
def delete_from_types(db: Session, type_name: str):
    if is_type_in_table(db, type_name):
        db.execute(text(f"DELETE FROM `types` WHERE pokemon_type = '{type_name}'"))
        db.commit()

    else:
        raise Exception("Type not in types table")