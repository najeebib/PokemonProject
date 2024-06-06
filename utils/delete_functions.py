from data.database import mongo_api
from bson import ObjectId

def delete_pokemon(pokemon_id: str):
    print(pokemon_id)
    pokemon_oid = ObjectId(pokemon_id)
    response = mongo_api.pokemon_collection.delete_one({"_id": pokemon_oid})
    output = {'Status': 'Successfully Deleted',
                  'Document_ID': pokemon_id}
    return output

def delete_trainer(trainer_id: str):
    trainer_oid = ObjectId(trainer_id)
    mongo_api.trainers_collection.delete_one({"_id": trainer_oid})
    output = {'Status': 'Successfully Deleted',
                  'Document_ID': trainer_id}
    return output