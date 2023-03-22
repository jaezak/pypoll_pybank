import csv
import os

# Files to load
budget_data = os.path.join("budget_data.csv")
# file to output
output_path = os.path.join("..", "pybank", "pybank_analysis.csv")

# Track various financial parameters
total_months = []
previous_profit = []
month_of_change = []
profit_change_list = []
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


#split month and year

#caclulations
    for row in reader:

        total_months = total_months + 1
        total_profits = total_profits + int(row["Profit/Losses"])

        
        previous_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change =  month_of_change + [row["Date"]]

# compare profit change to greatest increase
  
# average profit change
        average_change = sum(profit_change_list) / len(profit_change_list)


#output text

print(
    f"\nFinancial Analysis\n"
    f" ------------------------- \n"
    f"Total Months : {total_months}\n"
    f"Total Profit : {total_profits}\n"
    f"Average Profit Change: ${average_change}\n"
    f"Greatest Increase in Profit: \n"
    f"Greatest Decrease in Profit: \n"
)

path1 = os.path.join("pybank_analysis.txt")
path1 = "pybank_analysis.txt"

with open(path1, 'r') as file:
    print(file.read())