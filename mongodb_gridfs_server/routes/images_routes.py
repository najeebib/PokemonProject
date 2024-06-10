from fastapi import APIRouter
from models.pokemons import PokemonsList

router = APIRouter()


@router.get('/images/{pokemon_name}')
def get_pokemon_image(pokemon_name: str):
    pass

@router.post('/images')
def insert_pokemons_images(pokemons: PokemonsList):
    pass