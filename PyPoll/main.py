import csv
import os

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

votesTotal = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimitter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        votesTotal += 1