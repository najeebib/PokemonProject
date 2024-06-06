from data.database import mongo_api
from bson import ObjectId

def add_trainer_to_pokemon(pokemon_name: str, trainer_id: str):
    trainer_oid = ObjectId(trainer_id)
    print("asdasfvasf")
    update_result = mongo_api.pokemon_collection.update_one(
        {"name": pokemon_name},
        {"$addToSet": {"trainers": trainer_oid}}
    )
    print(update_result)
    updated_pokemon = mongo_api.pokemon_collection.find_one({"name": pokemon_name})

    if updated_pokemon and '_id' in updated_pokemon:
        updated_pokemon['_id'] = str(updated_pokemon['_id'])
    if updated_pokemon and 'trainers' in updated_pokemon:
        updated_pokemon['trainers'] = [str(tid) for tid in updated_pokemon['trainers']]
    
    return updated_pokemon

def delete_trainer_to_pokemon(pokemon_name: str, trainer_id: str):
    trainer_oid = ObjectId(trainer_id)
    print("asdasfvasf")
    update_result = mongo_api.pokemon_collection.update_one(
        {"name": pokemon_name},
        {"$pull": {"trainers": trainer_oid}}
    )
    print(update_result)
    updated_pokemon = mongo_api.pokemon_collection.find_one({"name": pokemon_name})

    if updated_pokemon and '_id' in updated_pokemon:
        updated_pokemon['_id'] = str(updated_pokemon['_id'])
    if updated_pokemon and 'trainers' in updated_pokemon:
        updated_pokemon['trainers'] = [str(tid) for tid in updated_pokemon['trainers']]
    
    return updated_pokemon