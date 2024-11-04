# import csv
# import pymysql

# timeout = 10
# connection = pymysql.connect(
#     charset="utf8mb4",
#     connect_timeout=timeout,
#     cursorclass=pymysql.cursors.DictCursor,
#     db="defaultdb",
#     host="world-athletics-world-athletics.h.aivencloud.com",
#     password="AVNS_q4qfMZEYhnIhreAFwYi",
#     read_timeout=timeout,
#     port=24936,
#     user="avnadmin",
#     write_timeout=timeout,
# )

# try:
#     cursor = connection.cursor()
#     cursor.execute("USE worldAthletics")
#     month_dict = {
#         "JAN": "01",
#         "FEB": "02",
#         "MAR": "03",
#         "APR": "04",
#         "MAY": "05",
#         "JUN": "06",
#         "JUL": "07",
#         "AUG": "08",
#         "SEP": "09",
#         "OCT": "10",
#         "NOV": "11",
#         "DEC": "12",
#     }
#     cursor.execute("USE worldAthletics")

#     # read csv and insert into table
#     players=[]
#     with open("Players.csv", "r") as f:
#         next(f)
#         for line in f:
#             players.append(line.split(","))
            
#     event=[]
#     # read csv using csv module
#     with open("Data.csv", "r") as f:
#         next(f)
#         for line in csv.reader(f):
#             x=line[6]
#             y=x.split(",")
#             z=y[3:]
            
            
#             city=z[1]
#             date = y[2]
#             name=z[0]
#             country=line[7]
#             category=line[8]
#             race=line[9]
            
#             if z not in event:
#                 event.append(z)
#                 cursor.execute(f"INSERT INTO Athletic_Events (event_date, event_name, event_city, event_country, event_category, event_race) VALUES ({date},{name},{city},{country},{category},{race})")
                
                
                
     
    
    
#     for i in event:
#         # send to database
        
#         cursor.execute(f"INSERT INTO Athletic_Events (event_date, event_name, event_city, event_country, event_category, event_race) VALUES ({a},{b},{c},{d},{e},{f})")
            
#     # connection.commit()

#     # print(cursor.fetchall())
# finally:
#     connection.close()
