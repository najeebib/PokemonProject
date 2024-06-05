from data.database import mongo_api

def insert_pokemon(pokemon: dict):
    response = mongo_api.pokemon_collection.insert_one(pokemon)
    output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
    return output

def insert_trainer(trainer: dict):
    response = mongo_api.trainers_collection.insert_one(trainer)
    output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
    return output
