print("Name : Jeev therese v mathew ")
print("Admission No: A24MCA034")
print("Experiment No: 17")

import csv

with open('input.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)
