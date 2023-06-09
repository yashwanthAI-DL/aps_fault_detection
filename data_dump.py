import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH='/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME= "aps"
COLLECTION_NAME="sensor"

if __name__ == "__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    #print(df.head())
    print('shape of the data', df.shape) #shape of the data 

    #convert data frame into json to dump in the Mangodb
    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())
    #print("json is converted",json_record[0])

    #insert into mangodb 
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


    
