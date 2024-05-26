from sqlalchemy.orm import Session
from sqlalchemy import text
from models.pokemon import Pokemon
from models.trainer import Trainer

def insert_into_pokemons_table(db: Session, pokemon: Pokemon):
    query = text("""
            INSERT INTO `pokemons` 
            (name, type, height, weight) 
            VALUES 
            (:name, :type, :height, :weight)
        """)
    db.execute(
        query,
        {
            "name": pokemon.name,
            "type": pokemon.type,
            "height": pokemon.height,
            "weight": pokemon.weight,
        }
    )
    db.commit()