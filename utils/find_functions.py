from data.database import mongo_api

def find_pokemon(pokemon_name: str):
    document = mongo_api.pokemon_collection.find_one({"name": pokemon_name})
    if document and '_id' in document:
            document['_id'] = str(document['_id'])
    return document

def find_trainer(trainer_name: str):
    document = mongo_api.trainers_collection.find_one({"name": trainer_name})
    if document and '_id' in document:
            document['_id'] = str(document['_id'])
    return document