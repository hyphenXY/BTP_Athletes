# take data from the data.csv and find all cities

import csv
import re

def main():
    cities=[]
    with open('Data.tsv','r') as f:
        reader = csv.reader(f, delimiter='\t')
        # skip 1st line
        next(reader)
        for row in reader:
            temp1=row[0].split('$')
            temp2=temp1[2].split(',')
            cities.append(temp2[4][1:])
            
            
            
    print(cities)
    # giev it a csv, each city in a new line
    with open('Cities.csv','w') as f:
        writer = csv.writer(f)
        for city in cities:
            writer.writerow([city])
    
if __name__ == '__main__':
    main()