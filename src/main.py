from utils.logger import init_logger
from etl.extract import extract
from etl.transform import transform
from etl.load import load
import datetime

logger = init_logger(__name__)


def run_etl_pipeline():
    extract()
    """  if extraction:
        transformation = transform(extraction) """
    

    


if __name__ == "__main__":
    start = datetime.datetime.now()
    logger.info('ETL pipeline started')
    run_etl_pipeline()
    end = datetime.datetime.now()
    logger.info(f'ETL pipeline finished in {end-start}')