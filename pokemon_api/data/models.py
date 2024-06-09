from sqlalchemy import Column, Integer, String, ForeignKey
from .database import base
from sqlalchemy.orm import relationship

class Pokemon(base):
    __tablename__ = 'pokemons'

    pokemon_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True)
    height = Column(Integer)
    weight = Column(Integer)

    owned_by = relationship('pokedex', back_populates='pokemon')
    type_of_pokemon = relationship('pokemonTypes', back_populates='pokemon')

class Types(base):
    __tablename__ = 'types'

    types_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_type = Column(String(50), unique=True)
    types = relationship('pokemonTypes', back_populates='types')

class PokemonTypes(base):
    __tablename__ = 'pokemontypes'

    pokemon_types_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey('pokemons.pokemon_id'))
    type_id = Column(Integer, ForeignKey('types.types_id'))

    pokemon = relationship('pokemon', back_populates='type_of_pokemon')
    types = relationship('types', back_populates='types')

class Trainer(base):
    __tablename__ = 'trainers'

    trainer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True)
    town = Column(String(50))

    pokemons = relationship('pokedex', back_populates='trainer')

class Pokedex(base):
    __tablename__ = 'pokedex'

    pokedex_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey('pokemons.pokemon_id'))
    trainer_id = Column(Integer, ForeignKey('trainers.trainer_id'))

    pokemon = relationship('pokemon', back_populates='owned_by')
    trainer = relationship('trainer', back_populates='pokemons')