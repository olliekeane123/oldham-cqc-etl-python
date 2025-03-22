from utils.logger import init_logger
from etl.extract import extract
from etl.transform import transform
from etl.load import load
import datetime

logger = init_logger(__name__)


def run_etl_pipeline():
    # Step 1: Extract
    extraction = extract()
    if not extraction:
        logger.error('Error: Failed to extract data - Stopping ETL')
        return

    # Step 2: Transform
    transformation = transform(extraction)
    if not transformation:
        logger.error('Error: Failed to transform data - Stopping ETL')
        return

    # Step 3: Load
    load(transformation)
    logger.info('ETL pipeline completed successfully.')
    

    


if __name__ == "__main__":
    start = datetime.datetime.now()
    logger.info('ETL pipeline started')
    
    try:
        run_etl_pipeline()
    except Exception as e:
        logger.error(f'Unhandled error: {e}')
    
    end = datetime.datetime.now()
    logger.info(f'ETL pipeline finished in {end-start}')