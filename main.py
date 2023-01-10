from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

class MongoDB:
    def __init__(self) -> None:
        MONGODB_PWD = os.environ.get('MONGODB_PWD')
        connection_string = f'mongodb+srv://elhirano:{MONGODB_PWD}@dataproject.euatmcr.mongodb.net/?retryWrites=true&w=majority'
        self.client = MongoClient(connection_string)

    def list_dbs(self):
        return self.client.list_database_names()
            
    def list_collections(self):
        return self.client.data_project.list_collection_names()

mdb = MongoDB()
print(mdb.list_dbs())
print(mdb.list_collections())