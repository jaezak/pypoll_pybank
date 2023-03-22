import csv
import os

# Files to load
budget_data = os.path.join("budget_data.csv")
# file to output
output_path = os.path.join("..", "analysis", "pybank_analysis.csv")

# set variables
date = []
month = []
year = []
total_months = []
profit_change = []
average_change = []
greatest_increase = [""]
greatest_decrease = [""]
net_total_profit_and_loss = []
total_profits = []

#read CSV
with open(budget_data) as csv_file:
    reader = csv.reader(csv_file)
    # Read the header row
    header = next(reader)
    for row in reader:
        print (row)
# split  month and year


    for row in reader:
#caclulations
# total number of months included in the dataset
        total_months 
# net total amount of "Profit/Losses" over the entire period
        total_profits 
#changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period
        greatest_increase = max()
#The greatest decrease in profits (date and amount) over the entire period
        greatest_decrease = min()

# compare profit change to greatest increase
  
# average profit change
        average_change = sum(profit_change) / len(total_months)


#output text

print(
    f"\nFinancial Analysis\n"
    f" ------------------------- \n"
    f"Total Months : {total_months}\n"
    f"Total Profits : ${total_profits}\n"
    f"Average Profit Change: ${average_change}\n"
    f"Greatest Increase in Profit: \n"
    f"Greatest Decrease in Profit: \n"
)
# write summary to txt file
path1 = os.path.join("pybank_analysis.txt")
path1 = "pybank_analysis.txt"

with open(path1, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("--------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total Profits: ${total_profits}\n")
    output.write(f"Average Profit Change: ${average_change}\n")
    output.write(f"Greatest Increase In Profit: \n")
    output.write(f"Greatest Decrease in Profit: \n")
                 