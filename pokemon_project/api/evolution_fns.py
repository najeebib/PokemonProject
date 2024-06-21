import requests
def get_evolution_chain(pokemon_name):
    """
    Get the evolution chain of the pokemon

    Parameters:
    - pokemon_name: name of the pokemon.

    Returns:
    - The evolution chain of the pokemon.
    """

    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    pokemon_response = requests.get(URL).json()

    species_url = pokemon_response['species']['url']

    species_response = requests.get(species_url).json()

    evolution_chain_url = species_response['evolution_chain']['url']

    evolution_chain_response = requests.get(evolution_chain_url).json()

    chain = evolution_chain_response['chain']
    return chain
def get_next_evolution(chain, pokemon_name):
    """
    Get the next evolution  of the pokemon

    Parameters:
    - chain: The evolution chain of the pokemon.
    - pokemon_name: name of the pokemon.

    Returns:
    - The evolution chain of the pokemon.
    """
    if chain['species']['name'] == pokemon_name:
        if chain['evolves_to']:
            next_evolution = chain['evolves_to'][0]['species']['name']
            return next_evolution
        else:
            return None
    for evolution in chain['evolves_to']:
        next_evolution = get_next_evolution(evolution, pokemon_name)
        if next_evolution:
            return next_evolution
    return None

def get_pokemon_details(pokemon_name: str):
    # get pokemon name, types, weight and height from api
    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    pokemon_response = requests.get(URL).json()

    pokemon_info = {
        "name": pokemon_response["name"],
        "types": [type_data["type"]["name"] for type_data in pokemon_response["types"]],
        "weight": pokemon_response["weight"],
        "height": pokemon_response["height"],
    }
    return pokemon_info