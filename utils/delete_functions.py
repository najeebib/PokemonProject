from data.database import mongo_api

def delete_pokemon(pokemon_id: str):
    response = mongo_api.pokemon_collection.delete_one({"name": pokemon_id})
    output = {'Status': 'Successfully Deleted',
                  'Document_ID': pokemon_id}
    return output

def delete_trainer(trainer_id: str):
    mongo_api.trainers_collection.delete_one({"name": trainer_id})
    output = {'Status': 'Successfully Deleted',
                  'Document_ID': trainer_id}
    return output