# Import the required library
from geopy.geocoders import Nominatim
import requests
import json

# Initialize Nominatim API

cities = []
with open('Cities_and_Dates2.csv') as f:
    for line in f:
        cities.append(line.split(',')[-1])

for city in cities[1:]:
    try:
        geolocator = Nominatim(user_agent="MyApp")
        print(city)
        
        location = geolocator.geocode(city)
        
        # print(location)
        url = f"https://api.opentopodata.org/v1/srtm90m?locations={location.latitude},{location.longitude}&interpolation=cubic"
        
        response = requests.get(url)
        data = response.json()
        # add a column in the json
        data['city'] = city
        
        # write a file
        with open('elevationdata.json', 'a') as f:
            json.dump(data, f)
    except Exception as e:
        continue

#  api.opentopodata.org/v1/srtm90m?locations=-43.5,172.5|27.6,1.9&interpolation=cubic


with open('elevationdata.json', 'w') as f:
    json.dump(data, f)
