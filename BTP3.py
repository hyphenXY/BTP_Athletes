import csv
import re


def main():
    lst = []
    lengthdict = set()
    with open('Data.csv', 'r') as f:
        reader = csv.reader(f)
        # skip 1st line
        next(reader)
        count=0
        for row in reader:
            count+=1
            if count==6885:
                break
            # if len(row) == 14:
            place = row[0]
            name = row[1]
            dob = row[2]
            nation = row[3]
            score = row[4]
            date = row[8]
            resultscore = row[10]
            resultscore = re.sub(r"^\W+|\W+$", "", resultscore)
            # city=(row[-3])
            if len(row) == 14:
                city = row[-3]
            elif len(row) == 15:
                city=row[-4]
            elif len(row) == 16:
                city = row[-5]
            elif len(row) == 17:
                city = row[-5]
            # remove all the special characters from front and behind
            # if len(row6) == 5:
            #     city = row6[-1]
            # elif len(row6) == 6:
            #     city = row6[-2]
            city = re.sub(r"^\W+|\W+$", "", city)
            city=city.replace('"', '')

            lst.append([place, name, dob, nation,
                        score, date, resultscore])

        #     lengthdict.add(len(row))

        # for row in reader:
        #     count+=1
        #     if count<=6885:
        #         continue
            
        #     place = row[0]
        #     name = row[1]
        #     dob = row[2]
        #     nation = row[3]
        #     score = row[4]
        #     date = (row[6].split(','))[2]
        #     resultscore = row[8]
        #     row6=row[6].split(',')
        #     if len(row6)==5:
        #         city = row6[-1]
        #     elif len(row6)==6:
        #         city = row6[-2]
                
        #     lst.append([place, name, dob, nation,
        #                 score, date, resultscore, city])            
    # for i in lst:
    #     print(i)
    # print('y')
    for i in lst:
        print(i)

    # Write to a CSV file, with date and city in separate columns
    with open('Cities_and_Dates1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Place', 'Competitor', 'DOB',
                        'Nationality', 'Score', 'Date', 'city'])
        for row in lst:
            writer.writerow(row)


if __name__ == '__main__':
    main()
