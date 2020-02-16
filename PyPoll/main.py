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
            canidateVotes[row[2]] = 1
        elif row[2] in canidateVotes:
            canidateVotes[row[2]] += 1

winnervalue = max(canidateVotes.values())
winner = list(canidateVotes.keys())[list(canidateVotes.values()).index(winnervalue)]
print(winner)
canidatePercents = {}
for canidate in canidateVotes:
    if canidateVotes[canidate] not in canidatePercents:
        canidatePercents[canidate] = round(((canidateVotes[canidate] / votesTotal) * 100),3)

print("Election Results")
print("-------------------------------")
print("Total Votes: " + str(votesTotal))
print("-------------------------------")
for canidate in canidates:
    print(str(canidate) + ": " + str(canidatePercents[canidate]) + "% " + "(" + str(canidateVotes[canidate]) + ")")
print("-------------------------------")
print("Winner: " + str(winner))
print("-------------------------------")