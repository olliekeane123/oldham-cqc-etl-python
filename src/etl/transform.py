from utils.logger import init_logger
import json
logger = init_logger(__name__)


def transform (locations):

    registered_locations = filter_by_registered_locations(locations)

    formatted_locations = format_locations(registered_locations)

    return formatted_locations


def filter_by_registered_locations(locations):
    return [location for location in locations if location["registrationStatus"] != "Deregistered"]

def format_locations(locations: list[dict]):
    formatted_locations = []
    for location in locations:
        formatted_location = {
            "name": location.get("name"),
            "location_id": location.get("locationId"),
            "description": None,
            "phone_number": location.get("mainPhoneNumber"),
            "email": None,
            "address1": location.get("postalAddressLine1"),
            "address2": location.get("postalAddressLine2"),
            "address3": location.get("postalAddressLine3"),
            "postcode": location.get("postalCode"),
            "coordinates": str(location.get("onspdLatitude")) + ", " + str(location.get("onspdLongitude")),
            "onspd_latitude": location.get("onspdLatitude"),
            "onspd_longitude": location.get("onspdLongitude"),
            "website": get_website(location),
            "type": location.get("type"),
            "cqc_url": f"https://www.cqc.org.uk/location/{location.get('locationId')}",
            "cqc_overall_report": location.get("currentRatings", {}).get("overall", {}).get("rating", 'NO RATINGS'),
            "cqc_report_date": location.get("currentRatings", {}).get("overall", {}).get("reportDate"),
            "provider_id": location.get("providerId"),
        }
        formatted_locations.append(formatted_location)
    return formatted_locations

def get_website(location: dict):
    website = location.get("website")
    if website:
        website = f"https://{website}"
    return website