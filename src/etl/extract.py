from utils.logger import init_logger
from etl.utils.api_client import CQCClient

logger = init_logger(__name__)

def extract():
    cqc_client = CQCClient()
    final_extract = []
    try:
        data = cqc_client.fetch_locations('Oldham')
        locations = data['locations']

        if not locations:
            logger.error('Error: Failed to extract locations - Stopping ETL')
            return None
        
        logger.info('Success: Fetch Locations')

        
        for location in locations:
            location_id = location['locationId']
            details = cqc_client.fetch_location_details(location_id)

            if details:
                final_extract.append(details)

            if not details:
                logger.warning(f'Warning: Failed to extract location details for ID {location_id}')

            if len(final_extract) % 50 == 0 and len(final_extract) > 0:
                logger.info('Success: Extracted 50 location details')

        if not final_extract:
            logger.error('Error: Failed to extract location details - Stopping ETL')
            return None
        
        return final_extract
    finally:
        cqc_client.close()















