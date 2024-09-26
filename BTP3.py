# # take data from the data.csv and find all cities

# import csv
# import re

# def main():
#     cities=[]
#     with open('Data.tsv','r') as f:
#         reader = csv.reader(f, delimiter='\t')
#         # skip 1st line
#         next(reader)
#         for row in reader:
#             temp1=row[0].split('$')
#             temp2=temp1[2].split(',')
#             cities.append(temp2[4][1:])
            
            
            
#     print(cities)
#     # giev it a csv, each city in a new line
#     with open('Cities.csv','w') as f:
#         writer = csv.writer(f)
#         for city in cities:
#             writer.writerow([city])
    
# if __name__ == '__main__':
#     main()

# import csv
# import re

# def main():
#     city_date_pairs = []
#     with open('Data.tsv', 'r') as f:
#         reader = csv.reader(f, delimiter='\t')
#         # skip 1st line
#         next(reader)
#         for row in reader:
#             temp1 = row[0].split('$')
#             date = temp1[1].strip()
#             temp2 = temp1[2].split(',')
#             # if len(temp2) >= 2:
#             #     city = temp2[-2].strip()  # City is the second-to-last element
#             #     city_date_pairs.append((date, city))
#             city_date_pairs.append((date,temp2[4][1:]))
            
#     print(city_date_pairs)
    
#     # Write to a CSV file, with date and city in separate columns
#     with open('Cities_and_Dates.csv', 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Date', 'City'])  # Header row
#         for date, city in city_date_pairs:
#             writer.writerow([date, city])

# if __name__ == '__main__':
#     main()

import csv
import re

def main():
    city_date_pairs = []
    with open('Data.tsv', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        # skip 1st line
        next(reader)
        for row in reader:
            temp1 = row[0].split('$')
            print(temp1)
            # Extract and clean date
            date = temp1[1].strip()
            date = date.replace('*', '').strip()  # Remove asterisk if present
            
            # Extract city (after 4th comma)
            temp2 = temp1[2].split(',')
            if len(temp2) >= 5:
                city = temp2[4].strip()
                city_date_pairs.append((date, city))
            
    print(city_date_pairs)
    
    # Write to a CSV file, with date and city in separate columns
    with open('Cities_and_Dates.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'City'])  # Header row
        for date, city in city_date_pairs:
            writer.writerow([date, city])

if __name__ == '__main__':
    main()