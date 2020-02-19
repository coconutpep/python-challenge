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

ssnsFix = []
for sn in ssns:
    last4 = sn[7:]
    sn = "***-**-" + str(last4)
    ssnsFix.append(sn)

stateAbv = []
stateAbvdict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
for state in states:
    for state_check in stateAbvdict:
        if state_check == state:
            stateAbv.append(stateAbvdict[state_check])
