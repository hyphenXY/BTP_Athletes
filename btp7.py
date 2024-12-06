# open data.csv and take all the last column values and store it in a list
import csv

lst=[]

with open('Data.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        lst.append(row[-1])
        
        
# print(lst)

for i in range(len(lst)):
    lst[i]=lst[i].replace('"','')
    lst[i]=lst[i].replace(' ','')
    lst[i]=lst[i].replace(',','')
    
# open cdall.csv and add the list to the last column
with open('cdall.csv', 'r') as file:
    reader = csv.reader(file)
    data = [row for row in reader]
    
for i in range(1,len(data)):
    data[i].append(lst[i])
    
with open('cdall.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    