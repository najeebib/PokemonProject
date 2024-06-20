from data.database import mongo_api
import requests

def get_pokemon_image(pokemon_name: str):
    # get the image from mongo db
    data = mongo_api.pokemon_images_collection.find_one({"filename": pokemon_name})

    fs_id = data['_id']
    out_data = mongo_api.fs.get(fs_id).read()

    return out_data

def insert_pokemons_image(pokemon_name: str, content: bytes):
    mongo_api.fs.put(content, filename=pokemon_name)