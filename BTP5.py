# import requests
# import csv
# from datetime import datetime

# APIKEY = "G8DJG324M57QK384ZFD2RXC6W"

# def convert_date_format(date_string):
#     input_date = datetime.strptime(date_string.strip(), "%d %b %Y")
#     return input_date.strftime("%Y-%m-%d")

# def fetch_weather_data(location, date):
#     base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
#     params = {
#         "unitGroup": "metric",
#         "key": APIKEY,
#         "contentType": "json",
#         "include": "current"
#     }
    
#     formatted_date = convert_date_format(date)
#     url = f"{base_url}/{location}/{formatted_date}"
    
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         return response.json()
#     except requests.RequestException as e:
#         print(f"Error fetching weather data for {location} on {formatted_date}: {e}")
#         return None

# def fetch_pollution_data(location, date):
#     base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
#     params = {
#         "unitGroup": "metric",
#         "key": APIKEY,
#         "contentType": "json",
#         "elements": "datetime,pm1,pm2p5,pm10,o3,no2,so2,co,aqius,aqieur"
#     }
    
#     formatted_date = convert_date_format(date)
#     url = f"{base_url}/{location}/{formatted_date}"
    
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         return response.json()
#     except requests.RequestException as e:
#         print(f"Error fetching pollution data for {location} on {formatted_date}: {e}")
#         return None

# def extract_important_factors(weather_data, pollution_data):
#     important_factors = {}
    
#     if weather_data and 'currentConditions' in weather_data:
#         current = weather_data['currentConditions']
#         important_factors.update({
#             'temperature': current.get('temp'),
#             'humidity': current.get('humidity'),
#             'wind_speed': current.get('windspeed'),
#             'precipitation': current.get('precip'),
#         })
    
#     if pollution_data and 'days' in pollution_data and pollution_data['days']:
#         pollution = pollution_data['days'][0]
#         important_factors.update({
#             'pm2.5': pollution.get('pm2p5'),
#             'pm10': pollution.get('pm10'),
#             'o3': pollution.get('o3'),
#             'no2': pollution.get('no2'),
#             'so2': pollution.get('so2'),
#             'co': pollution.get('co'),
#             'aqi_us': pollution.get('aqius'),
#         })
    
#     return important_factors

# def process_and_write_csv(input_file, output_file):
#     with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
#         reader = csv.DictReader(infile)
#         fieldnames = ['location', 'date', 'temperature', 'humidity', 'wind_speed', 'precipitation',
#                       'pm2.5', 'pm10', 'o3', 'no2', 'so2', 'co', 'aqi_us']
#         writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#         writer.writeheader()
        
#         for row in reader:
#             location = row['City']
#             date = row['Date']
#             weather_data = fetch_weather_data(location, date)
#             pollution_data = fetch_pollution_data(location, date)
            
#             important_factors = extract_important_factors(weather_data, pollution_data)
#             important_factors['location'] = location
#             important_factors['date'] = date
            
#             writer.writerow(important_factors)
    
#     print(f"Data processed and saved to {output_file}")

# if __name__ == "__main__":
#     input_file = 'Cities_and_dates2.csv'
#     output_file = 'weather_pollution_data.csv'
    
#     process_and_write_csv(input_file, output_file)
import re
from select import poll
import requests
import json
import csv
from datetime import datetime

APIKEY = "G8DJG324M57QK384ZFD2RXC6W"

def convert_date_format(date_string):
    input_date = datetime.strptime(date_string.strip(), "%d %b %Y")
    return input_date.strftime("%Y-%m-%d")

def fetch_weather_data(location, date):
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    params = {
        "unitGroup": "metric",
        "key": APIKEY,
        "contentType": "json",
        "include": "current"
    }
    
    formatted_date = convert_date_format(date)
    url = f"{base_url}/{location}/{formatted_date}"
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data for {location} on {formatted_date}: {e}")
        return None

def fetch_pollution_data(location, date):
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    params = {
        "unitGroup": "metric",
        "key": APIKEY,
        "contentType": "json",
        "elements": "datetime,pm1,pm2p5,pm10,o3,no2,so2,co,aqius,aqieur"
    }
    
    formatted_date = convert_date_format(date)
    url = f"{base_url}/{location}/{formatted_date}"
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching pollution data for {location} on {formatted_date}: {e}")
        return None

def process_csv(file_path):
    results = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            location = row['City']
            date = row['Date']
            # weather_data = fetch_weather_data(location, date)
            weather_data = fetch_weather_data("manali", "23 Oct 2024")
            # pollution_data = fetch_pollution_data(location, date)
            pollution_data = fetch_pollution_data("manali", "15 Oct 2024")
            if weather_data and pollution_data:
                results.append({
                    "location": location,
                    "date": date,
                    "weather_data": weather_data,
                    "pollution_data": pollution_data
                })
            print(results)
    return results

def save_results(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    input_file = 'Cities_and_Dates2.csv'
    output_file = 'weather_pollution_data.json'
    
    results = process_csv(input_file)
    # save_results(results, output_file)
    print(f"Data fetched and saved to {output_file}")