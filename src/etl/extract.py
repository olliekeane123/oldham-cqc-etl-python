from utils.logger import init_logger
from etl.utils.api_client import CQCClient

logger = init_logger(__name__)


def extract():
    cqc_client = CQCClient()
    final_extract = []
    try:
        data = cqc_client.fetch_providers('Oldham')
        providers = data['providers']

        if not providers:
            logger.error('Error: Failed to extract providers - Stopping ETL')
            return None
        
        


        for provider in providers:
            provider_id = provider['providerId']
            details = cqc_client.fetch_provider_details(provider_id)

            if not details:
                logger.warning(f'Warning: Failed to extract provider details for ID {provider_id}')
            
            final_extract.append(details)
                
        return final_extract
    finally:
        cqc_client.close()















