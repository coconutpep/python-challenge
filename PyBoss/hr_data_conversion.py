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

dobsFix = []
for dob in dobs:
    month = dob[5:7]
    day = dob[8:]
    year = dob[:4]
    dobjoin = str(month) + "/" + str(day) + "/" + str(year)
    dobsFix.append(dobjoin)
