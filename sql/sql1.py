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

#     # read csv and insert into table
#     with open("Players.csv", "r") as f:
#         next(f)
#         for line in f:
#             rank = line.split(",")[0]
#             name = line.split(",")[1]
#             # if there is ' in name, replace it with ''
#             name = name.replace("'", " ")
#             dob = line.split(",")[2]
#             if len(dob.split(" ")) == 1:
#                 year=dob
#                 month="01"
#                 date="01"
#             else:
#                 year = dob.split(" ")[2]
#                 month = month_dict[dob.split(" ")[1]]
#                 date= dob.split(" ")[0]
                
#             if len(dob)==0:
#                 year="0000"
#                 month="01"
#                 date="01"
            
#             country = line.split(",")[3]
#             score = line.split(",")[5]
#             url = line.split(",")[7]
#             print(rank, name, year, month, date, country, score, url)
#             cursor.execute(
#                 f"INSERT INTO Players VALUES ({rank}, '{name}', '{year}-{month}-{date}', '{country}', {score}, '{url}');"
#             )
#     # connection.commit()
    
    

#     print(cursor.fetchall())
# finally:
#     connection.close()
