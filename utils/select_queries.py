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
    return result


def select_pokemons_by_type(db: Session, pokemon_type: str):
    result = db.execute(text(f"SELECT p.name FROM pokemons p JOIN pokemontypes pt ON p.pokemon_id = pt.pokemon_id JOIN types t ON pt.type_id = t.types_id WHERE t.pokemon_type = '{pokemon_type}' ORDER BY p.name")).fetchall()
    pokemons = [row[0] for row in result]
    return pokemons

def select_pokemons_by_type(db: Session, pokemon_type: str):
    pass

def slecte_pokemons_by_trainer(db: Session, trainer_name: str):
    trainer = select_trainer(db, trainer_name)

    trainer_id = trainer.trainer_id
    
    result = db.execute(text(f"SELECT pokemon_id FROM `pokedex` WHERE trainer_id = {trainer_id}")).fetchall()

    pokemon_objs = []
    for row in result:
        pokemon_objs.append(row._mapping)
    
    pokemons = []
    for pokemon_obj in pokemon_objs:
        pokemon = db.execute(text(f"SELECT * FROM `pokemons` WHERE pokemon_id = {pokemon_obj['pokemon_id']}")).fetchone()
        pokemons.append(pokemon._mapping)

    return pokemons

def select_trainers_by_pokemonName(db: Session, pokemon_name: str):
    pokemon = select_pokemon(db, pokemon_name)
    pokemon_id = pokemon.pokemon_id

    result = db.execute(text(f"SELECT trainer_id FROM `pokedex` WHERE pokemon_id = {pokemon_id}")).fetchall()

    trainer_objs = []
    for row in result:
        trainer_objs.append(row._mapping)
    
    trainers = []
    for trainer_obj in trainer_objs:
        trainer = db.execute(text(f"SELECT * FROM `trainers` WHERE trainer_id = {trainer_obj['trainer_id']}")).fetchone()
        trainers.append(trainer._mapping)

    return trainers