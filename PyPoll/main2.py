"""Modules"""
import os
import csv

#Import CSV
"""
Ballot ID, County, Candidate
"""

#Set path for file
#File_path = 'C:\\Users\\jerry\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv'
csvpath = os.path.join("Resources", "election_data.csv")

"""
The total number of votes cast
"""

#Operns the file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
  
    #Rowcount includes header
    rowcount = sum(1 for row in csvreader)
    
    """Calculate Total Months - need to exclude header"""
    totalvotes = str(rowcount-1)


    """
    A complete (unique) list of candidates who received votes
    """
    
    # Initialize a set to store unique values from the first column
    uniquecandidates = set()
    
#with open(csvpath, encoding='UTF-8') as csvfile:
#    csvreader = csv.reader(csvfile, delimiter=",")   
#    header = next(csvreader)
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Assuming the first column is index 0
        value = row[2]

        # Add the value to the set
        uniquecandidates.add(value)

# Convert the set to a list if needed
uniquelist = list(uniquecandidates)

winner = "Diana DeGette"
Charles_Casper_Stockham = "Charles Casper Stockham"
Diana_DeGette = "Diana DeGette"
Raymon_Anthony_Doane = "Raymon Anthony Doane"

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
print(f"Candidates: {uniquelist}")

print(f"Charles Casper Stockham: {Charles_Casper_Stockham}")
print(f"Diana DeGette: {Diana_DeGette}")
print(f"Raymon Anthony Doane: {Raymon_Anthony_Doane}")
print("-------------------------")
print(f"winner: {winner}")
print("-------------------------")
