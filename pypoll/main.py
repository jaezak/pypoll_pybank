### PyPoll Instructions

#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

#You will be given a set of poll data called `election_data.csv`. 
#The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

import csv
import os

# Files to load
election_data = os.path.join("resources/election_data.csv")
# file to output
output_path = os.path.join("pypoll_analysis.csv")

# set variables
total_votes = 0
candidates = []
percentage_votes = 0
number_votes = 0
winning_candidate = ""
winning_count = 0
charles = []
diana = []
raymon = []


#read CSV
with open(election_data) as csv_file:
    reader = csv.reader(csv_file)
    # Read the header row
    header = next(reader)

    #calculations
    for row in reader:
        total_votes += 1
        #total number of votes cast
        candidates.append(row[2])
for candidate in candidates:
    if candidate == "Charles Casper Stockham":
        charles.append(candidate)
    elif candidate == "Diana DeGette":
        diana.append(candidate)
    else: 
        raymon.append(candidate)
charles_count = len(charles)
diana_count = len(diana)
raymon_count = len(raymon)


#* The percentage of votes each candidate won
charles_percent = round(((charles_count / total_votes)* 100),3)
diana_percent = round(((diana_count/total_votes)*100),3)
raymon_percent = round(((raymon_count/total_votes)*100),3)

#* The winner of the election based on popular vote

votes = (charles_count, diana_count, raymon_count)
winner = max(votes)

#output

print(
    f"\nElection Results\n"
    f"------------------------- \n"
    f"Total Votes: {total_votes}\n"
    f"Charles Votes: {charles_percent}% ({charles_count})\n"
    f"Diana Votes: {diana_percent}% ({diana_count})\n"
    f"Raymon Votes: {raymon_percent}%({raymon_count})\n"
    f"Winner: Diana {winner}\n"


)
# write summary to txt file
textfilepath = "analysis/pypoll_analysis.txt"

with open(textfilepath, 'w') as output:
    output.write("Election Results\n")
    output.write("--------------------\n")
    f"Total Votes: {total_votes}\n"
    f"Charles Votes: {charles_percent}% ({charles_count})\n"
    f"Diana Votes: {diana_percent}% ({diana_count})\n"
    f"Raymon Votes: {raymon_percent}%({raymon_count})\n"
 
                 
