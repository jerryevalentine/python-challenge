
#Dependencies
import pandas as pd

#Define variabes and lists for candiate names
ccs = "Charles Casper Stockham"
dg = "Diana DeGette"
rad = "Raymon Anthony Doane"

Candidate = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
Abbreviation = ["ccs", "dd", "rad"]



#Lists to dataframes
data = {'Abbreviation': Abbreviation,'Candidate': Candidate}
candidate_abbr = pd.DataFrame(data)
candidate_abbr.set_index('Candidate', inplace=True)


#Read the election data into a dataframe (df)
df = pd.read_csv('Resources/election_data.csv')
    
#The length of the dataframe is the total number of votes cast.
totalvotes = len(df)


#Unique list of candidates who received votes
uniquelistdf = df['Candidate'].value_counts()

unique_candidates = df['Candidate'].unique()

#Group by 'Candidate' to get vote count by candidate
count_by_candidate = df.groupby('Candidate').size()

rad_vote_count = count_by_candidate.loc[rad]
dg_vote_count = count_by_candidate.loc[dg]
ccs_vote_count = count_by_candidate.loc[ccs]

rad_vote_percent = str(round((rad_vote_count/totalvotes)*100, 3)) + "%"
dg_vote_percent = str(round((dg_vote_count/totalvotes)*100, 3)) + "%"
ccs_vote_percent = str(round((ccs_vote_count/totalvotes)*100, 3)) + "%"

if rad_vote_count>dg_vote_count and rad_vote_count>ccs_vote_count:
    winner = rad
elif ccs_vote_count>rad_vote_count and ccs_vote_count>dg_vote_count:
    winner = ccs
elif dg_vote_count>rad_vote_count and dg_vote_count>ccs_vote_count:
    winner = dg
elif dg_vote_count == ccs_vote_count:
    winner = "dg and ccs tied"
elif dg_vote_count == rad_vote_count:
    winner = "dg and rad tied"
elif ccs_vote_count == rad_vote_count:
    winner = "ccs and rad tied"
else:
    winner = "All possibilities tried but none were met.  Please check for an issue."





print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
print(f"Charles Casper Stockham: {ccs_vote_percent} ({ccs_vote_count})")
print(f"Diana DeGette: {dg_vote_percent} ({dg_vote_count})")
print(f"Raymon Anthony Doane: {rad_vote_percent} ({rad_vote_count})")


print("-------------------------")
print(f"winner: {winner}")
print("-------------------------")

# Open a text file in write mode ('w')
with open('analysis/write.txt', 'w') as file:
    
    file.write("Election Results" +'\n')
    file.write("-------------------------" +'\n')
    file.write(f"Total Votes: {totalvotes}" +'\n')
    file.write("-------------------------" +'\n')
    file.write(f"Charles Casper Stockham: {ccs_vote_percent} ({ccs_vote_count})" +'\n')
    file.write(f"Diana DeGette: {dg_vote_percent} ({dg_vote_count})" +'\n')
    file.write(f"Raymon Anthony Doane: {rad_vote_percent} ({rad_vote_count})" +'\n')
    file.write("-------------------------" +'\n')
    file.write(f"winner: {winner}" +'\n')
    file.write("-------------------------" +'\n')