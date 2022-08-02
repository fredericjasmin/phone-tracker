import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phoneNumber = phonenumbers.parse(input("What number do you want to search? (Remember to include the country code with +): "))

Carrier = carrier.name_for_number(phoneNumber, 'en')

Region = geocoder.description_for_number(phoneNumber, 'en')

Timezone = timezone.time_zones_for_number(phoneNumber,)

print(f"PhoneNumber: {phoneNumber}")
print(f"Carrier: {Carrier}")
print(f"Region: {Region}")
print(f"Timezone: {Timezone}")