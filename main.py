import pymongo
from sensor.utils import get_collection_as_dataframe
import os,sys
from sensor.Entity.config_entity import TrainingPipelineConfig
from sensor.Entity.config_entity import DataIngestionConfig
from sensor.Components import data_ingestion
from sensor import exception
from sensor.Components.data_ingestion import DataIngestion
from sensor.Components.data_validation import DataValdiation
from sensor.Entity import config_entity

if __name__=="__main__":
     try:
          training_pipeline_config=TrainingPipelineConfig()
          data_ingestion_config=DataIngestionConfig(training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion=data_ingestion.DataIngestion(data_ingestion_config=data_ingestion_config)
     
          data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
          data_validation_config=config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
          data_validation=DataValdiation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)

          data_validation_artifact=data_validation.initiate_data_validation()



     except Exception as e:
          raise exception.SensorException(e, sys)

'''
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase = client["neurolabDB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")
'''