import csv
import os

# Files to load
budget_data = os.path.join("resources/budget_data.csv")
# file to output
output_path = os.path.join("..", "analysis", "pybank_analysis.csv")

# set variables

total_months = 0
profit_change = []
average_change = 0
greatest_increase = 0
greatest_decrease = 0
total_profits = 0
increase_month = ""
decrease_month = ""

#read CSV
with open(budget_data) as csv_file:
    reader = csv.reader(csv_file)
    # Read the header row
    header = next(reader)

    #calculations
    for row in reader:
        total_months += 1
        net_value = int(row[1])
        total_profits += net_value

#output

print(
    f"\nFinancial Analysis\n"
    f" ------------------------- \n"
    f"Total Months : {total_months}\n"
    f"Total Profits : ${total_profits}\n"
    f"Average Profit Change: ${average_change}\n"
    f"Greatest Increase in Profit: \n"
    f"Greatest Decrease in Profit: \n"
)
# write summary to txt fi
textfilepath = "analysis/pybank_analysis.txt"

with open(textfilepath, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("--------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total Profits: ${total_profits}\n")
    output.write(f"Average Profit Change: ${average_change}\n")
    output.write(f"Greatest Increase In Profit: \n")
    output.write(f"Greatest Decrease in Profit: \n")
                 