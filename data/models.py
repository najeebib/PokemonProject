from sqlalchemy import Column, Integer, String, ForeignKey
from .database import base
from sqlalchemy.orm import relationship

class Pokemon(base):
    __tablename__ = 'Pokemons'

    pokemon_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True)
    height = Column(Integer)
    weight = Column(Integer)

    owned_by = relationship('Pokedex', back_populates='pokemon')
    type_of_pokemon = relationship('PokemonTypes', back_populates='pokemon')

class Types(base):
    __tablename__ = 'Types'

    types_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_type = Column(String(50), unique=True)
    types = relationship('PokemonTypes', back_populates='types')

class PokemonTypes(base):
    __tablename__ = 'PokemonTypes'

    pokemon_types_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey('Pokemons.pokemon_id'))
    type_id = Column(Integer, ForeignKey('Types.types_id'))

    pokemon = relationship('Pokemon', back_populates='type_of_pokemon')
    types = relationship('Types', back_populates='types')

class Trainer(base):
    __tablename__ = 'Trainers'

    trainer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50),primary_key=True, unique=True)
    town = Column(String(50))

    pokemons = relationship('Pokedex', back_populates='trainer')

class Pokedex(base):
    __tablename__ = 'Pokedex'

    pokedex_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id = Column(Integer, ForeignKey('Pokemons.pokemon_id'))
    trainer_id = Column(Integer, ForeignKey('Trainers.trainer_id'))

    pokemon = relationship('Pokemon', back_populates='owned_by')
    trainer = relationship('Trainer', back_populates='pokemons')