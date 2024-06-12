from fastapi import APIRouter, HTTPException
from classes.requests_handler import requests_handler
router = APIRouter()


@router.get('/image')
def get_pokemon(pokemon_name: str):
    """
    Send request to mongodb server to get pokemon image from the database

    Parameters:
    - pokemon_name: the pokemon name.
    """
    try:
        if type(pokemon_name) == str:
            return requests_handler.get_request("http://mongodb_gridfs_server-myreader-1:5002/image", pokemon_name=pokemon_name)
        raise HTTPException(400, detail="Ivalid pokemon name")
    except Exception:
        raise HTTPException(500, detail="Server error")
