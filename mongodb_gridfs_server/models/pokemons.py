from pydantic import BaseModel

class PokemonsList(BaseModel):
    pokemons: list[str]



