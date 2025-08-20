import os
import logging
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.cursor import Cursor
from data_loader.soldier import Soldier

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



class DataLoader:
    
    def __init__(self) -> None:
        """Initialize database connection parameters."""
        self.MONGO_HOST:str = os.getenv("MONGO_HOST", "localhost") 
        self.MONGO_PORT:str = os.getenv("MONGO_PORT", "27017")
        self.MONGO_DATABASE:str = os.getenv("MONGO_DATABASE", "enemy_soldiers") 
        self.MONGO_COLLECTION:str = os.getenv("MONGO_COLLECTION", "soldier_details")
        self.client_con = self.client()
        logger.debug(f"Database connection parameters set: DB_HOST:{self.MONGO_HOST}, MONGO_DATABASE:{self.MONGO_DATABASE}")

    def client(self) -> MongoClient:
        """
        Create a MongoDB client.
        """
        client_string = f"mongodb://{self.MONGO_HOST}:{ self.MONGO_PORT}"
        client:MongoClient = MongoClient(client_string)
        return client
    
    def get_database(self) -> Database:
        """
        Create a database connection.
        """ 
        db: Database = self.client_con[self.MONGO_DATABASE]
        logger.debug("Database connection successful.")
        return db

    def get_collection(self) -> Collection:
        """
        Fetch all records from the specified table.
        """
        logger.debug(f"Fetching all records from collection: {self.MONGO_COLLECTION}")

        db: Database = self.get_database()
        collection: Collection = db[self.MONGO_COLLECTION]
        return collection
    
    def insert(self, soldier:Soldier) -> bool:
        """Insert a new soldier into the database."""
        collection:Collection = self.get_collection()
        insert = collection.insert_one(soldier.__dict__)
        return insert.acknowledged
    
    def update(self, soldier_id: int, update_dict: dict) -> bool:
        """Update an existing soldier in the database."""
        collection:Collection = self.get_collection()
        update = collection.update_one(filter={"_id":soldier_id}, update={"$set":update_dict})
        return update.acknowledged
    
    def delete(self, soldier_id: int) -> bool:
        """Delete a soldier from the database."""
        collection:Collection = self.get_collection()
        delete = collection.delete_one(filter={"_id":soldier_id})
        return delete.acknowledged
    
    def get(self, soldier_id=None) -> Cursor:
        """Fetch soldier/s from the database."""
        collection:Collection = self.get_collection()
        if not soldier_id: return collection.find({})
        return collection.find({"_id":soldier_id})
    
    


