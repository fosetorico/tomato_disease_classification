from tomato_disease_classification import logger
from tomato_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from tomato_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from tomato_disease_classification.pipeline.stage_03_training import ModelTrainingPipeline 
from tomato_disease_classification.pipeline.stage_04_evaluation import EvaluationPipeline  


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================================x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Prepare base model"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = PrepareBaseModelTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================================x")
except Exception as e:
   logger.exception(e)
   raise e


STAGE_NAME = "Training"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = ModelTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================================x")
except Exception as e:
   logger.exception(e)
   raise e


STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = EvaluationPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx====================================x")
except Exception as e:
   logger.exception(e)
   raise e