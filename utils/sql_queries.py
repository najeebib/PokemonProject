from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.orm import Session

def is_type_in_table(db: Session, pokemon_type: str):
    result = db.execute(text(f"SELECT * FROM `types` WHERE pokemon_type = '{pokemon_type}'")).fetchone()
    if result:
        return True
    return False

def is_pokemon_in_table(db: Session, pokemon_name: str):
    result = db.execute(text(f"SELECT * FROM `pokemons` WHERE name = '{pokemon_name}'")).fetchone()
    if result:
        return True
    return False

def is_trainer_in_table(db: Session, trainer_name: str):
    result = db.execute(text(f"SELECT * FROM `trainers` WHERE name = '{trainer_name}'")).fetchone()
    if result:
        return True
    return False

def is_in_pokedex(db: Session, pokemon_id: int, trainer_id: int):
    result = db.execute(text(f"SELECT * FROM `pokedex` WHERE pokemon_id = {pokemon_id} AND trainer_id = {trainer_id}")).fetchone()
    if result:
        return True
    return False

def is_in_pokemontype(db: Session, pokemon_id: int, type_id: int):
    result = db.execute(text(f"SELECT * FROM `pokemontypes` WHERE pokemon_id = {pokemon_id} AND type_id = {type_id}")).fetchone()
    if result:
        return True
    return False