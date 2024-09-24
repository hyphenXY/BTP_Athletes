# import requests

# APIKEY= "G8DJG324M57QK384ZFD2RXC6W"
# location = "Delhi"
# date1 = "2021-01-01"
# date2 = "2021-01-10"

# url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date1}/{date2}?key={APIKEY}"



import requests
import sys

import json
                
response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/delhi?unitGroup=metric&include=current&key=G8DJG324M57QK384ZFD2RXC6W&contentType=json")
if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit() 

print(response.text)

# Parse the results as JSON
jsonData = response.json()

# store
with open('data.json', 'w') as f:
    json.dump(jsonData, f)