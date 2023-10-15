import phonenumbers
from phonenumbers import geocoder, carrier

# Input phone number in international format (e.g., +1234567890)
phone_number = "+919028850715"

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number, None)

# Get geographical information (country, city, etc.)
geo_info = geocoder.description_for_number(parsed_number, "en")

# Get carrier information
carrier_info = carrier.name_for_number(parsed_number, "en")


# Print the results
print("Phone Number:", phone_number)
print("Location:", geo_info)
print("Carrier:", carrier_info)
