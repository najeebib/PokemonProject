from pydantic import BaseModel
from models.pokemon import Pokemon
class PokemonsList(BaseModel):
    pokemons: list[dict[str, str]]
