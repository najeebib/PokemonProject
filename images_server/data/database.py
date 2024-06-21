from pymongo import MongoClient
import gridfs
class MongoAPI:
    def __init__(self) -> None:
        self.client = MongoClient("mongodb://mymongo_1:27017/")

        database = "pokemon-service"
        pokemon_collection_name = "pokemon-images"
        
        self.cursor = self.client[database]
        self.pokemon_images_collection = self.cursor["pokemon-images.files"]
        self.fs = gridfs.GridFS(self.cursor, collection=pokemon_collection_name)
    
mongo_api = MongoAPI()