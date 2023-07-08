import pymongo
from sensor.utils import get_collection_as_dataframe
import os,sys
from sensor.Entity.config_entity import TrainingPipelineConfig
from sensor.Entity.config_entity import DataIngestionConfig
from sensor.Components import data_ingestion
from sensor import exception
from sensor.Components.data_ingestion import DataIngestion
from sensor.Components.data_validation import DataValdiation
from sensor.Components.data_transformation import DataTransformation
from sensor.Components.model_traininer import ModelTrainer
from sensor.Components.model_evaluation import ModelEvaluation
from sensor.Components.model_pusher import ModelPusher
from sensor.Entity import config_entity

if __name__=="__main__":
     try:
          #data ingestion
          training_pipeline_config=TrainingPipelineConfig()
          data_ingestion_config=DataIngestionConfig(training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion=data_ingestion.DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
          
          #data validation
          data_validation_config=config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
          data_validation=DataValdiation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)
          data_validation_artifact=data_validation.initiate_data_validation()
          #transformation
          data_transformation_config=config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
          data_transformation= DataTransformation(data_transformation_config=data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)
          data_transformation_artifact=data_transformation.initiate_data_transformation()

          # model trainer
          model_trainer_config=config_entity.ModelTrainingConfig(training_pipeline_config=training_pipeline_config)
          model_trainer=ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact=model_trainer.initiate_model_trainer()

          # model evaluator
          model_eval_config=config_entity.ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)
          model_eval= ModelEvaluation(model_eval_config=model_eval_config, data_ingestion_artifact=data_ingestion_artifact, data_transformation_artifact=data_transformation_artifact,
          model_trainer_artifact=model_trainer_artifact)
          model_eval_artifact=model_eval.initiate_model_evaluation()


          #model Pusher
          model_pusher_config=config_entity.ModelPusherConfig(training_pipeline_config=training_pipeline_config)
          model_pusher=ModelPusher(model_pusher_config=model_pusher_config, data_transformation_artifact=data_transformation_artifact,
           model_trainer_artifact=model_trainer_artifact)
          model_pusher_artifact = model_pusher.initiate_model_pusher()


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