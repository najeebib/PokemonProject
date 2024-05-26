from sqlalchemy.orm import Session
from sqlalchemy import text
from models.pokemon import Pokemon
from models.trainer import Trainer
from data.database import get_db
from sqlalchemy.orm import Session
import json

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


def insert_into_pokemons_table(db: Session, name: str, height: int, weight: int):
    if not is_pokemon_in_table(db, pokemon_name=name):
        query = text("""
                INSERT INTO `pokemons` 
                (name, height, weight) 
                VALUES 
                (:name, :height, :weight)
            """)
        db.execute(
            query,
            {
                "name": name,
                "height": height,
                "weight": weight,
            }
        )
        db.commit()


def insert_into_types_table(db: Session, types: list):
    for pokemon_type in types:
        if not is_type_in_table(db, pokemon_type):
            query = text("""
                    INSERT INTO `types` 
                    (pokemon_type) 
                    VALUES 
                    (:pokemon_type)
                """)
            db.execute(
                query,
                {
                    "pokemon_type": pokemon_type,
                    
                }
            )
            db.commit()

def insert_into_trainers_table(db: Session, name: str, town: str):
    if not is_trainer_in_table(db, trainer_name=name):
        query = text("""
                INSERT INTO `trainers` 
                (name, town) 
                VALUES 
                (:name, :town)
            """)
        db.execute(
            query,
            {
                "name": name,
                "town": town
            }
        )
        db.commit()

def insert_into_PokemonTypes_table(db: Session, pokemon_name: str, types: list):
    for pokemon_type in types:
        query = text("""
                    INSERT INTO `pokemontypes` 
                    (pokemon_name, pokemon_type) 
                    VALUES 
                    (:pokemon_name, :pokemon_type)
                """)
        db.execute(
            query,
            {
                "pokemon_name": pokemon_name,
                "pokemon_type": pokemon_type
            }
        )
        db.commit()

def insert_into_Pokedex_table(db: Session, pokemon_name: str, trainer_name: str):
    query = text("""
                INSERT INTO `pokedex` 
                (pokemon_name, trainer_name) 
                VALUES 
                (:pokemon_name, :trainer_name)
            """)
    db.execute(
        query,
        {
            "pokemon_name": pokemon_name,
            "trainer_name": trainer_name
        }
    )
    db.commit()