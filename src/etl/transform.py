from utils.logger import init_logger
import json
logger = init_logger(__name__)


def transform (providers):

    # cleaned_data = []

    registered_providers = filter_by_registered_providers(providers)

    formatted_providers = format_providers(registered_providers)

    with open('cleaned_data.json', 'w') as f:
        json.dump(formatted_providers, f, indent=4)


def filter_by_registered_providers(providers):
    return [provider for provider in providers if provider["registrationStatus"] != "Deregistered"]

def format_providers(providers: list[dict]):
    formatted_providers = []
    for provider in providers:
        formatted_provider = {
            "name": provider.get("name"),
            # "description": provider.get("regulatedActivities"),
            "telephone": provider.get("mainPhoneNumber"),
            "email": None,
            "address1": provider.get("postalAddressLine1"),
            "address2": provider.get("postalAddressLine2"),
            "address3": provider.get("postalAddressLine3"),
            "postcode": provider.get("postalCode"),
            "coordinates": str(provider.get("onspdLatitude")) + ", " + str(provider.get("onspdLongitude")),
            "website": provider.get("website"),
            "type": provider.get("type"),
            "cqcreport": provider.get("currentRatings", {}).get("overall", {}).get("rating"),
            "cqcdate": provider.get("currentRatings", {}).get("overall", {}).get("reportDate"),
        }
        formatted_providers.append(formatted_provider)
    return formatted_providers