from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
import data.models as models
from data.database import engine, session_local
from sqlalchemy.orm import Session
from data.database import get_db
from sqlalchemy import text
from models.trainer import Trainer
from models.pokemon import Pokemon


router = APIRouter()

@router.post("/pokemon/", response_model=Pokemon)
def create_pokemon(pokemon: Pokemon, db: Session = Depends(get_db)):
    db_pokemon = Pokemon(name=pokemon.name, type=pokemon.type, height=pokemon.height, weight=pokemon.weight)
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon


@router.get("/pokemon/{pokemon_id}", response_model=Pokemon)
def read_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if db_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return db_pokemon


@router.put("/pokemon/{pokemon_id}", response_model=Pokemon)
def update_pokemon(pokemon_id: int, pokemon: Pokemon, db: Session = Depends(get_db)):
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if db_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    for var, value in vars(pokemon).items():
        setattr(db_pokemon, var, value) if value else None
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon


@router.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if db_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    db.delete(db_pokemon)
    db.commit()
    return {"message": "Pokemon deleted"}


# TODO: 