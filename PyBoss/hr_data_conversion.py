import os
import csv

csv_path = os.path.join(".", "employee_data.csv")

empIDs = []
firstnames=[]
lastnames=[]
dobs = []
ssns = []
states = []
with open(csv_path, newline="") as employeeData:
    csvreader = csv.reader(employeeData, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        splitname = row[1].split()
        empIDs.append(row[0])
        firstnames.append(splitname[0])
        lastnames.append(splitname[1])
        dobs.append(row[2])
        ssns.append(row[3])
        states.append(row[4])

