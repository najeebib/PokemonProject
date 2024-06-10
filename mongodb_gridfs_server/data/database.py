from pymongo import MongoClient
class MongoAPI:
    def __init__(self) -> None:
        self.client = MongoClient("mongodb://localhost:27017/")

        database = "pokemon-service"
        pokemon_collection_name = "pokemon-images"

        cursor = self.client[database]

        self.pokemon_images_collection = cursor[pokemon_collection_name]
    
mongo_api = MongoAPI()