from utils.logger import init_logger
from etl.utils.api_client import CQCClient
import json
logger = init_logger(__name__)


def extract():
    cqc_client = CQCClient()
    final_extract = []
    try:
        data = cqc_client.fetch_providers('Oldham')

        if not data:
            logger.error('Error: Failed to extract providers - Stopping ETL')
            return None
        
        providers = data['providers']


        for provider in providers[:20]:
            provider_id = provider['providerId']
            details = cqc_client.fetch_provider_details(provider_id)
            if details:
                # final_extract.append(details)
                logger.info(f'Success: Extracted provider details for ID {provider_id}')
                with open (f'src/mock_api/dummy_data/provider_details/provider_{provider_id}.json', 'w') as f:
                    json.dump(details, f)
                logger.info(f'Success: Saved provider details for ID {provider_id}')
            else:
                logger.warning(f'Warning: Failed to extract provider details for ID {provider_id}')
                
        return final_extract
    finally:
        cqc_client.close()















