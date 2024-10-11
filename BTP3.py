import csv
import re


def main():
    lst = []
    lengthdict=set()
    with open('Data.csv', 'r') as f:
        reader = csv.reader(f)
        # skip 1st line
        next(reader)
        for row in reader:
            if len(row)==14:
                place=row[0]
                name=row[1]
                dob=row[2]
                nation=row[3]
                score=row[4]
                date=row[8]
                resultscore=row[10]
                city=(row[-3])
                # remove all the special characters from front and behind
                city = re.sub(r"^\W+|\W+$", "", city)

                lst.append([place, name, dob, nation, score, date, resultscore, city])
            elif len(row)==16:
                place=row[0]
                name=row[1]
                dob=row[2]
                nation=row[3]
                score=row[4]
                date=row[8]
                resultscore=row[10]
                city=(row[-4])
                # remove all the special characters from front and behind
                city = re.sub(r"^\W+|\W+$", "", city)

                lst.append([place, name, dob, nation, score, date, resultscore, city])
            elif len(row)==17:
                place=row[0]
                name=row[1]
                dob=row[2]
                nation=row[3]
                score=row[4]
                date=row[8]
                resultscore=row[10]
                city=(row[-5])
                # remove all the special characters from front and behind
                city = re.sub(r"^\W+|\W+$", "", city)

                lst.append([place, name, dob, nation, score, date, resultscore, city])
            elif len(row)==18:
                place=row[0]
                name=row[1]
                dob=row[2]
                nation=row[3]
                score=row[4]
                date=row[8]
                resultscore=row[10]
                city=(row[-5])
                # remove all the special characters from front and behind
                city = re.sub(r"^\W+|\W+$", "", city)

                lst.append([place, name, dob, nation, score, date, resultscore, city])
            
            
            lengthdict.add(len(row))

    # for i in lst:
    #     print(i)
    
    for i in lengthdict:
        print(i)

    # Write to a CSV file, with date and city in separate columns
    # with open('Cities_and_Dates.csv', 'w', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['Place', 'Competitor', 'DOB', 'Nationality', 'Score', 'Date', 'ResultScore', 'City'])
    #     for row in lst:
    #         writer.writerow(row)


if __name__ == '__main__':
    main()

