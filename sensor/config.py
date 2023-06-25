import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str= os.getenv("MONGO_DB_URL")
env_var=EnvironmentVariable()

mongo_client=pymongo.MongoClient(env_var.mongo_db_url)

# Provide the mongodb localhost url to connect python to mongodb.
#client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")