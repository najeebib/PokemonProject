from fastapi import APIRouter, HTTPException
from classes.requests_handler import requests_handler
import base64
from redis_client.redis import rd
import json

router = APIRouter()


@router.get('/images/{pokemon_name}')
def get_pokemon(pokemon_name: str):
    """
    Send request to mongodb server to get pokemon image from the database

    Parameters:
    - pokemon_name: the pokemon name.
    """
    try:
        if type(pokemon_name) != str:
            raise HTTPException(400, detail="Ivalid pokemon name")
        url_key = f"/image?pokemon_name={pokemon_name}"
        cache = rd.get(url_key)
        if cache:
            return json.loads(cache)
        else:
            response_image =  requests_handler.get_request(f"http://images_server-images-server-1:5002//images/{pokemon_name}")
            image_data = response_image.content
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            rd.set(url_key, json.dumps(encoded_image))
            return response_image
    except Exception:
        raise HTTPException(500, detail="Server error")
