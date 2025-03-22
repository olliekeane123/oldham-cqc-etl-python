import requests
from config import settings
from utils.logger import init_logger

logger = init_logger(__name__)

class CQCClient:
    def __init__(self):
        self.base_url = settings.CQC_BASE_URL
        self.api_key = settings.CQC_API_KEY
        self.session = requests.Session()
        self.session.headers.update({
            "Ocp-Apim-Subscription-Key": self.api_key,
            "Accept": "application/json",
            "Content-Type": "application/json", 
            "User-Agent": "Mozilla/5.0"
            })
    
    def fetch_providers(self, local_authority):
        url = f"{self.base_url}/providers?localAuthority={local_authority}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            logger.info('Success: Fetch Providers')
            return response.json()
        except requests.exceptions.HTTPError as err:
            logger.error(f' Error: {err.response.status_code} Failed to fetch providers')
            return None
        except Exception as err:
            logger.error(f' Error: {err} Failed to fetch providers')
            return None

    def fetch_provider_details(self, provider_id):
        url = f"{self.base_url}/providers/{provider_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            logger.info('Success: Fetch Provider Details')
            return response.json()
        except requests.exceptions.HTTPError as err:
            logger.error(f' Error: {err.response.status_code} Failed to fetch provider details')
            return None
        except Exception as err:
            logger.error(f' Error: {err} Failed to fetch provider details')
            return None
        
    def close(self):
        self.session.close()

