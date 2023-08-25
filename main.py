from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(STAGE_NAME + " started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(STAGE_NAME + " completed")
except Exception as e:
    logger.exception(e)
    raise e