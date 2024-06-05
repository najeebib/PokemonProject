from pymongo import MongoClient
class MongoAPI:
    def __init__(self) -> None:
        self.client = MongoClient("mongodb://localhost:27017/")

        database = "pokemon-service"
        pokemon_collection_name = "pokemons"
        trainers_collection_name = "trainers"
        cursor = self.client[database]
        self.pokemon_collection = cursor[pokemon_collection_name]
        self.trainers_collection = cursor[trainers_collection_name]
    
mongo_api = MongoAPI()