import csv
import os

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

months = []
changes = []
netTotal = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months.append(str(row[0]))
        changes.append(int(row[1]))
        netTotal += int(row[1])
    monthTotal = len(months)
    netAverage = round(float(netTotal) / monthTotal, 2)
    maxIncrease = max(changes)
    maxDecrease = min(changes)

print("Financial Analysis")
print("------------------")
print("Total Months: ", str(monthTotal))
print("Total: $", str(netTotal))
print("Average Change: $", str(netAverage))
print("Greatest Increase in Profits: ", str(months[changes.index(maxIncrease)]), "$" + str(maxIncrease))
print("Greatest Decrease in Profits: ", str(months[changes.index(maxDecrease)]), "$" + str(maxDecrease))

output_path = os.path.join("..", "PyBank", "financial_analysis.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write("Total Months: %s\n" % str(monthTotal))
    txtfile.write("Total: $%s\n" % str(netTotal))
    txtfile.write("Average Change: $%s\n" % str(netAverage))
    txtfile.write("Greatest Increase in Profits: %s $%s\n" % (str(months[changes.index(maxIncrease)]), str(maxIncrease)))
    txtfile.write("Greatest Decrease in Profits: %s $%s\n" % (str(months[changes.index(maxDecrease)]), str(maxDecrease)))
