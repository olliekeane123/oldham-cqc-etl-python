from extract import extract
from transform import transform
from load import load


def run_etl_pipeline():
    extract()
    transform()
    load()


if __name__ == "__main__":
    print(__name__)
    run_etl_pipeline()