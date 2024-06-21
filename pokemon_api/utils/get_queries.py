from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.orm import Session

def select_type(db: Session, pokemon_type: str):
    result = db.execute(text(f"SELECT * FROM `types` WHERE pokemon_type = '{pokemon_type}'")).fetchone()
    return result

def select_trainer(db: Session, trainer_name: str):
    result = db.execute(text(f"SELECT * FROM `trainers` WHERE name = '{trainer_name}'")).fetchone()
    return result
  
def select_pokemon(db: Session, pokemon_name: str):
    result = db.execute(text(f"SELECT * FROM `pokemons` WHERE name = '{pokemon_name}'")).fetchone()
    return result._mapping

def select_pokemon_by_id(db: Session, pokemon_id: int):
    result = db.execute(text(f"SELECT * FROM `pokemons` WHERE pokemon_id = '{pokemon_id}'")).fetchone()
    return result._mapping



def select_pokemons_by_type(db: Session, pokemon_type: str):
    query = text("""
        SELECT pokemon.name
        FROM pokemons pokemon
        JOIN pokemontypes pokemontype ON pokemon.pokemon_id = pokemontype.pokemon_id
        JOIN types type ON pokemontype.type_id = type.types_id
        WHERE type.pokemon_type = :pokemon_type
        ORDER BY pokemon.name
    """)
    result = db.execute(query, {"pokemon_type": pokemon_type}).fetchall()
    pokemons = [row[0] for row in result]
    return pokemons

def slecte_pokemons_by_trainer(db: Session, trainer_name: str):
    query = text("""
        SELECT pokemon.name
        FROM pokemons pokemon
        JOIN pokedex pd ON pokemon.pokemon_id = pd.pokemon_id
        JOIN trainers trainer ON pd.trainer_id = trainer.trainer_id
        WHERE trainer.name = :trainer_name
        ORDER BY pokemon.name
    """)
    result = db.execute(query, {"trainer_name": trainer_name}).fetchall()
    pokemons = [row._mapping for row in result]
    return pokemons

def select_trainers_by_pokemonName(db: Session, pokemon_name: str):
    query = text("""
        SELECT trainer.name
        FROM trainers trainer
        JOIN pokedex pd ON trainer.trainer_id = pd.trainer_id
        JOIN pokemons pokemon ON pd.pokemon_id = pokemon.pokemon_id
        WHERE pokemon.name = :pokemon_name
        ORDER BY trainer.name
    """)
    result = db.execute(query, {"pokemon_name": pokemon_name}).fetchall()
    trainers = [row._mapping for row in result]
    return trainers