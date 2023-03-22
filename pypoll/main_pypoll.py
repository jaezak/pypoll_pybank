# main pypoll
### PyPoll Instructions

#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

#You will be given a set of poll data called `election_data.csv`. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#* The total number of votes cast

#* A complete list of candidates who received votes

#* The percentage of votes each candidate won

#* The total number of votes each candidate won

#* The winner of the election based on popular vote

#Your analysis should align with the following results:

#Election Results

#Total Votes: 369711

#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)

#Winner: Diana DeGette
compare profit change to greatest increase
    if (profit_change[] > greatest_increase[1]):
        greatest_increase[0] = row["Date"]
        greatest_increase[1] = profit_change
# compare profit change to greatest decrease
    if (profit_change[] < greatest_decrease[1]):
        greatest_decrease[0] = row["Date"]
        greatest_decrease[1] = profit_change
# average profit change
        average_change = sum(profit_change_list) / len(profit_change_list)


#output text

print(
    f"\nFinancial Analysis\n"
    f" ------------------------- \n"
    f"Total Months : {total_months}\n"
    f"Total Profit : {total_profit}\n"
    f"Average Profit Change: ${average_profit}\n"
    f"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(output)

path4 = os.path.join("pybank_analysis.txt")
path4 = "pybank_analysis.txt"

file = open(path4, "w+")



#paste this if needed
# average profit change
        average_change = sum(profit_change_list) / len(profit_change_list)

  if (profit_change_list > greatest_increase[1]):
        greatest_increase[0] = int(row["Date"])
    else:
        greatest_increase[1] = int(profit_change)
# compare profit change to greatest decrease
    if (profit_change_list < greatest_decrease[1]):
        greatest_decrease[0] = int(row["Date"])
    else:
        greatest_decrease[1] = int(profit_change)
#914In addition, your final script should both print the analysis to the terminal and export a text file with the results.
