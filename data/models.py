from sqlalchemy import Column, Integer, String, ForeignKey
from .database import base
from sqlalchemy.orm import relationship

class Pokemon(base):
    __tablename__ = 'Pokemons'

    pokemon_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True)
    pokemon_type = Column(String(20))
    height = Column(Integer)
    weight = Column(Integer)

    owned_by = relationship('Pokedex', back_populates='pokemon')


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