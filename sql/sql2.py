import pymysql
from geopy.geocoders import Nominatim
import requests
import json

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="world-athletics-world-athletics.h.aivencloud.com",
    password="AVNS_q4qfMZEYhnIhreAFwYi",
    read_timeout=timeout,
    port=24936,
    user="avnadmin",
    write_timeout=timeout,
)

try:
    cursor = connection.cursor()
    cursor.execute("USE worldAthletics")
    
    # take values from table
    cursor.execute("SELECT * FROM City_Details")
    result = cursor.fetchall()
    # print(result)
    
    # add a column in the sql table
    # cursor.execute("ALTER TABLE City_Details ADD COLUMN elevation FLOAT")
    
    # in each row, get the city name and find the elevation
    for row in result:
        city = row["city_name"]
        try:
            geolocator = Nominatim(user_agent="MyApp")
            print(city)
            
            location = geolocator.geocode(city)
            
            # print(location)
            url = f"https://api.opentopodata.org/v1/srtm90m?locations={location.latitude},{location.longitude}&interpolation=cubic"
            response = requests.get(url)
            data = response.json()
            # update the sql table
            cursor.execute("UPDATE City_Details SET longitude = %s, latitude = %s, elevation = %s WHERE city_name = %s", (location.latitude, location.longitude, data['results'][0]['elevation'], city))
            
        except Exception as e:
            continue
            
    
finally:
    connection.commit()
    connection.close()
