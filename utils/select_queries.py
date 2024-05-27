from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.orm import Session

def select_type(db: Session, pokemon_type: str):
    result = db.execute(text(f"SELECT * FROM `types` WHERE pokemon_type = '{pokemon_type}'")).fetchone()
    return result

def select_trainer(db: Session, trainer_name: str):
    result = db.execute(text(f"SELECT * FROM `trainers` WHERE name = '{trainer_name}'")).fetchone()
    return result

def slecte_pokemons_by_type(db: Session, pokemon_type: str):
    pass

def slecte_pokemons_by_trainer(db: Session, trainer_name: str):
    pass
