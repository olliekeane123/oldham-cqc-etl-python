from logger import init_logger
from extract import extract
from transform import transform
from load import load

logger = init_logger(__name__)


def run_etl_pipeline():
    extract()
    transform()
    load()


if __name__ == "__main__":
    logger.info('logger from main')
    run_etl_pipeline()