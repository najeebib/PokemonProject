from sqlalchemy import Column, Integer, String, ForeignKey, Text
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

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_type = Column(String(50), unique=True)
    types = relationship('PokemonTypes', back_populates='types')

class PokemonTypes(base):
    __tablename__ = 'PokemonTypes'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_name = Column(String(50), ForeignKey('Pokemons.name'))
    pokemon_type = Column(String(50), ForeignKey('Types.pokemon_type'))

    pokemon = relationship('Pokemon', back_populates='type_of_pokemon')
    types = relationship('Types', back_populates='types')

class Trainer(base):
    __tablename__ = 'Trainers'

    name = Column(String(50),primary_key=True, unique=True)
    town = Column(String(50))

    pokemons = relationship('Pokedex', back_populates='trainer')

class Pokedex(base):
    __tablename__ = 'Pokedex'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_name = Column(String(50), ForeignKey('Pokemons.name'))
    trainer_name = Column(String(50), ForeignKey('Trainers.name'))

    pokemon = relationship('Pokemon', back_populates='owned_by')
    trainer = relationship('Trainer', back_populates='pokemons')