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

@router.get('/add_pokemon')
def add_pokemon(pokemon: Pokemon, trainer: Trainer):
    # Add a pokemon to a trainer

    pass
