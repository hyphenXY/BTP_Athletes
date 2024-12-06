import re
from select import poll
import requests
import json
import csv
from datetime import datetime

APIKEY = "W7V6FMF562DFMP4QGF5FAJ8Q4"

def convert_date_format(date_string):
    input_date = datetime.strptime(date_string.strip(), "%d %b %Y")
    return input_date.strftime("%Y-%m-%d")

def fetch_weather_data(location, date):
    formatted_date = convert_date_format(date)
    
    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{formatted_date}/{formatted_date}?key={APIKEY}"
    params = {
        "unitGroup": "metric",
        "key": APIKEY,
        "contentType": "json",
        "include": "current"
    }
    print(base_url)
    
    # url = f"{base_url}/{location}/{formatted_date}"
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data for {location} on {formatted_date}: {e}")
        return None

def fetch_pollution_data(location, date):
    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/New York City,NY?unitGroup=metric&key={APIKEY}&contentType=json&elements=datetime,pm1,pm2p5,pm10,o3,no2,so2,co,aqius,aqieur"
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
            try:
                location = row['City']
                location=location.replace(" ","")
                date = row['Date']
                weather_data = fetch_weather_data(location, date)
                # weather_data = fetch_weather_data("manali", "23 Oct 2024")
                # pollution_data = fetch_pollution_data(location, date)
                # pollution_data = fetch_pollution_data("manali", "15 Oct 2024")
                # if weather_data and pollution_data:
                if weather_data:
                    results.append({
                        "location": location,
                        "date": date,
                        "weather_data": weather_data,
                        # "pollution_data": pollution_data
                    })
                print(results)
                save_results(results, 'weather_pollution_data.json')
            except Exception as e:
                print(f"Error processing row: {e}")
    return results

def save_results(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    input_file = 'Cities_and_Dates1.csv'
    output_file = 'weather_pollution_data.json'
    
    try:
        results = process_csv(input_file)
    except Exception as e:
        print(f"Error processing CSV file: {e}")
    # save_results(results, output_file)
    print(f"Data fetched and saved to {output_file}")