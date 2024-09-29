APIKEY= "G8DJG324M57QK384ZFD2RXC6W"

# url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date1}/{date2}?key={APIKEY}"



import requests
import sys

import json
                
# response = requests.request("GET", "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/delhi?unitGroup=metric&include=current&key=G8DJG324M57QK384ZFD2RXC6W&contentType=json")
# if response.status_code!=200:
#   print('Unexpected Status code: ', response.status_code)
#   sys.exit() 
  
# r2 = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/New York City,NY?unitGroup=metric&key={APIKEY}&contentType=json&elements=datetime,pm1,pm2p5,pm10,o3,no2,so2,co,aqius,aqieur")

# print(response.text)

# # Parse the results as JSON
# jsonData = response.json()

# # store
# with open('data.json', 'w') as f:
#     json.dump(jsonData, f)

with open('final.csv', 'r') as file:
  next(file)
  for line in file.readlines():
      print(line)
      location=line.split(',')[-1]
      date1=line.split(',')[-2]
      url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date1}/{date2}?key={APIKEY}"