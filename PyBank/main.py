import csv
import os

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

months = []
profitloss = []
changes = []
netTotal = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months.append(str(row[0]))
        profitloss.append(int(row[1]))
        netTotal += int(row[1])
    monthTotal = len(months)

for number in profitloss:
    if profitloss.index(number) != (len(profitloss) - 1):
        changes.append(profitloss[(profitloss.index(number)) + 1] - profitloss[profitloss.index(number)])

netChange= 0
for change in changes:
    netChange += change

averageChange = netChange / len(changes)
averageChange = round(averageChange, 2)
greatestChange = max(changes)
leastChange = min(changes)

print("Financial Analysis")
print("------------------")
print("Total Months: ", str(monthTotal))
print("Total: $", str(netTotal))
print("Average Change: $", str(averageChange))
print("Greatest Increase in Profits: ", str(months[(changes.index(greatestChange)) + 1]), "$" + str(greatestChange))
print("Greatest Decrease in Profits: ", str(months[(changes.index(leastChange)) + 1]), "$" + str(leastChange))

output_path = os.path.join("..", "PyBank", "financial_analysis.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write("Total Months: %s\n" % str(monthTotal))
    txtfile.write("Total: $%s\n" % str(netTotal))
    txtfile.write("Average Change: $%s\n" % str(averageChange))
    txtfile.write("Greatest Increase in Profits: %s $%s\n" % (str(months[(changes.index(greatestChange)) + 1]), str(greatestChange)))
    txtfile.write("Greatest Decrease in Profits: %s $%s\n" % (str(months[(changes.index(leastChange)) + 1]), str(leastChange)))
