# take data from the data.csv and find all cities

import csv
import re

def main():
    cities=[]
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        # from 2nd row
        next(reader)
        for row in reader:
            cities.append((((row.split(' $ '))[3]).split(','))[1])
            
    print(cities)
                