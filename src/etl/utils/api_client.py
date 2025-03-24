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
    
    def fetch_locations(self, local_authority):
        url = f"{self.base_url}/locations?localAuthority={local_authority}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            logger.error(f' Error: {err.response.status_code} Failed to fetch locations')
            return None
        except Exception as err:
            logger.error(f' Error: {err} Failed to fetch locations')
            return None

    def fetch_location_details(self, location_id):
        url = f"{self.base_url}/locations/{location_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            logger.error(f' Error: {err.response.status_code} Failed to fetch location details')
            return None
        except Exception as err:
            logger.error(f' Error: {err} Failed to fetch location details')
            return None
        
    def close(self):
        self.session.close()

