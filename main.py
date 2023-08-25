from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(STAGE_NAME + " started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(STAGE_NAME + " completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(STAGE_NAME + " started")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(STAGE_NAME + " completed")
except Exception as e:
    logger.exception(e)
    raise e