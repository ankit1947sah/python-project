import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Replace with the number you want to check
number = "+915558558955990 "  # Example: country code write +91 for India

# Parse the number
parsed_number = phonenumbers.parse(number)

# Get location (country/region)
location = geocoder.description_for_number(parsed_number, "en")

# Get service provider (carrier)
service_provider = carrier.name_for_number(parsed_number, "en")

# Get timezone(s)
time_zones = timezone.time_zones_for_number(parsed_number)

print("Phone Number:", number)
print("Location:", location)
print("Carrier:", service_provider)
print("Time Zones:", time_zones)
