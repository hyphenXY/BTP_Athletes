# Import the required library
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("delhi")

print("The latitude of the location is: ", location.latitude)
print("The longitude of the location is: ", location.longitude)

import requests
import json

#  api.opentopodata.org/v1/srtm90m?locations=-43.5,172.5|27.6,1.9&interpolation=cubic

url = f"https://api.opentopodata.org/v1/srtm90m?locations={location.latitude},{location.longitude}&interpolation=cubic"

response = requests.get(url)
data = response.json()

with open('elevationdata.json', 'w') as f:
    json.dump(data, f)