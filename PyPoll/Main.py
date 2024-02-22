#PyPoll

import os
import csv

#Creating an empty container 
Candidate_votes={}
#Resetting Votes
Total_Votes = 0 

# Path to collect data from the Resources folder
PyPoll_CSV = os.path.join ('source', 'election_data copy.csv')
Outputpath = os.path.join ('Analysis', 'Poll_Analysis.txt')

#Read in CVS File 
with open(PyPoll_CSV, 'r') as csvfile:
    #Split the data on commas 
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    header = next(csvreader)

#Define the function and have it accept ''Ballot_Data' as its sole parameter
    # CSV Header: Ballot ID,County,Candidate

#Iterate through Dataset 
    for row in csvreader: 
        Total_Votes +=1
        Candidate_name = row[2]
        if Candidate_name in Candidate_votes:
            Candidate_votes[Candidate_name] += 1
        else: 
             Candidate_votes[Candidate_name] = 1

with open(Outputpath, 'w') as Output_file:
    Output_file.write("Election Results\n")
    Output_file.write("------------------------------\n")
    Output_file.write(f"Total Votes: {Total_Votes}\n")
    Output_file.write("------------------------------\n")
    for Candidate, votes in Candidate_votes.items():
        percentage = (votes / Total_Votes) * 100
        Output_file.write(f"{Candidate}: {percentage:.2f}% ({votes})\n")
    Output_file.write("------------------------------\n")
    winner = max(Candidate_votes, key=Candidate_votes.get)
    Output_file.write(f"Winner: {winner}\n")

#Print out Results 
print ("Election Results")
print ("------------------------------")
print(f"Total Votes: {Total_Votes}")
print ("------------------------------")
for Candidate, votes in Candidate_votes.items():
    percentage = (votes / Total_Votes) * 100
    print(f"{Candidate}: {percentage:.2f}% ({votes})")
print ("------------------------------")
winner = max(Candidate_votes, key=Candidate_votes.get)
print(f"Winner: {winner}")