import csv
import os

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

votesTotal = 0
canidates = []
canidateVotes = {}
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        votesTotal += 1
        if row[2] not in canidates:
            canidates.append(row[2])
            print(canidates)
        if row[2] not in canidateVotes:
            canidateVotes[row[2]] = 1
            print(canidateVotes)
