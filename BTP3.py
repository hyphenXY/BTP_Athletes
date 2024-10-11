import csv
import re


def main():
    lst = []
    with open('Data.csv', 'r') as f:
        reader = csv.reader(f)
        # skip 1st line
        next(reader)
        for row in reader:
            place=row[0]
            name=row[1]
            dob=row[2]
            nation=row[3]
            score=row[4]
            date=row[8]
            resultscore=row[10]
            city=(row[12])
            # remove all the special characters from front and behind
            city = re.sub(r"^\W+|\W+$", "", city)

            lst.append([place, name, dob, nation, score, date, resultscore, city])

    for i in lst:
        print(i)

    # Write to a CSV file, with date and city in separate columns
    with open('Cities_and_Dates.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Place', 'Competitor', 'DOB', 'Nationality', 'Score', 'Date', 'ResultScore', 'City'])
        for row in lst:
            writer.writerow(row)


if __name__ == '__main__':
    main()

