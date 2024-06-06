from data.database import mongo_api
from bson import ObjectId

def get_pokemon(pokemon_name: str):
    document = mongo_api.pokemon_collection.find_one({"name": pokemon_name})
    if document and '_id' in document:
            document['_id'] = str(document['_id'])
    return document

def get_trainer_by_name(trainer_name: str):
    document = mongo_api.trainers_collection.find_one({"name": trainer_name})
    if document and '_id' in document:
            document['_id'] = str(document['_id'])
    return document

def get_trainer_by_id(trainer_id: str):
    trainer_oid = ObjectId(trainer_id)
    document = mongo_api.trainers_collection.find_one({"_id": trainer_oid})
    if document and '_id' in document:
            document['_id'] = str(document['_id'])
    return document

def get_pokemons_by_type(type: str):
    documents = list(mongo_api.pokemon_collection.find({"types": type}))
    for document in documents:
        if '_id' in document:
            document['_id'] = str(document['_id'])
    return documents

def get_pokemons_by_trainer(trainer_id: str):
    trainer_oid = ObjectId(trainer_id)
    documents = list(mongo_api.pokemon_collection.find({"trainers": trainer_oid}))
    for document in documents:
        if '_id' in document:
            document['_id'] = str(document['_id'])
        if 'trainers' in document:
            document['trainers'] = [str(trainer) for trainer in document.get('trainers', [])]
    return documents