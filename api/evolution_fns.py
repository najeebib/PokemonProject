import requests
def get_evolution_chain(pokemon_name):
    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    pokemon_response = requests.get(URL).json()

    species_url = pokemon_response['species']['url']

    species_response = requests.get(species_url).json()

    evolution_chain_url = species_response['evolution_chain']['url']

    evolution_chain_response = requests.get(evolution_chain_url).json()

    chain = evolution_chain_response['chain']
    return chain
def get_next_evolution(chain, pokemon_name):
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