import csv
import re


def main():
    lst = []
    with open('Data.csv', 'r') as f:
        reader = csv.reader(f)
        # skip 1st line
        next(reader)
        for row in reader:
            name = row[0]
            dob = row[1]
            country = row[2]
            date = row[5]
            # print(date)
            city = row[9]

            lst.append([name, dob, country, date, city])

    # print(lst)

    # Write to a CSV file, with date and city in separate columns
    with open('Cities_and_Dates.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'DOB', 'Country', 'Date', 'City'])  #
        for row in lst:
            writer.writerow(row)


if __name__ == '__main__':
    main()

