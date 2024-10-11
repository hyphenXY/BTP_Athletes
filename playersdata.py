# open worldathletics.html file

# from sympy import re


import re


links=[]
with open('worldathletics.html', 'r') as f:
    contents = f.read()
    # wherever there is data-athlete-url, get the value of it
    links = re.findall(r'data-athlete-url="(.*?)"', contents)
    
print(links)

datalst=[]
with open("Men's Marathon_8 Oct 2024.csv", 'r') as f:
    # put all the data in a list
    datalst = f.readlines()
    
# print(datalst)

# from every row in datalst, append the link from links
# to the end of the row

for i in range(len(links)):
    datalst[i+1] = (datalst[i+1][:-1]).strip() + ',' + links[i] + '\n'
    
print(datalst)

with open("Players.csv", 'w') as f:
    for row in datalst:
        f.write(row)