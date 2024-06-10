from fastapi import APIRouter, Response,status, HTTPException
from models.pokemons_list import PokemonsList
from models.pokemon import Pokemon
import base64
import utils.gridfs_functions as gridfs_functions
router = APIRouter()


@router.get('/image/{pokemon_name}')
def get_pokemon_image(pokemon_name: str):
    try:
        out_data = gridfs_functions.get_pokemon_image(pokemon_name)
        return Response(content=out_data, media_type="image/jpeg")
    except Exception:
        raise HTTPException(500, detail="Server error when getting pokemon image")

@router.post('/image')
def insert_pokemons_image(pokemon: Pokemon):
    try:
        content = pokemon.content
        content = base64.b64decode(content)
        name = pokemon.name
        gridfs_functions.insert_pokemons_image(name, content)
        return {f"Status code: {status.HTTP_201_CREATED}","pokemon image was added to the database"}
    except Exception:
        raise HTTPException(500, detail="Server error when isnerting pokemon image")

@router.post('/images')
def insert_pokemons_images(pokemons: PokemonsList):
    try:
        for pokemon in pokemons.pokemons:        
            content = pokemon["content"]
            content = base64.b64decode(content)
            name = pokemon["name"]
            gridfs_functions.insert_pokemons_image(name, content)
            return {f"Status code: {status.HTTP_201_CREATED}","pokemons were added to the database"}
    except Exception:
        raise HTTPException(500, detail="Server error when isnerting pokemon images")