import os
import csv

#variables and lists / dictonary for specific candidate
candidateList = [] 
candidate_votes = {}
percent_votes = {}

#path to collect data from Resource folder
electiondata_csv = os.path.join(".", "Resources", "election_data.csv")

#open the csv file in reader mode
with open(electiondata_csv, "r") as inputcsvfile:

    #split data with comma delimiter
    csv_reader = csv.reader(inputcsvfile, delimiter=",")

    #skip through header row
    csv_header = next(csv_reader)

    #loop through and add candidates to candidate list and get total 
    for row in csv_reader:

        candidateList.append(row[2])

totalvotes = len(candidateList)

#A complete list of candidates who received votes
#loop through candidate list
#if key exists, add one to the value else add to other candidate
for candidate in candidateList:
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1


#put keys and values from dictionary and dump them into lists 
for k, v in candidate_votes.items():
    #key_candidates.append(k)
    #value_votes.append(v)

    #The percentage of each candidate vote
    percent_votes[k] = str(round( v * 100.0 / totalvotes, 3)) + "% ("+str(v) + ")"

    #determine winner based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

#print results
print("Election Results")
print("----------------------------------------")
print("Total Votes:" + str(totalvotes))
print("----------------------------------------")
for k , v in percent_votes.items():
    print(f'{k}:{v}')
print("----------------------------------------")
print("Winner:" + str(winner))
print("----------------------------------------")

#print output to text file
output_text = os.path.join(".", "PyPoll_Analysis.txt")

with open(output_text, "w") as textfile:
    textfile.write("Election Results" + "\n")
    textfile.write("----------------------------------------------------------" + "\n")
    textfile.write("Total Votes:" + str(totalvotes) + "\n")
    textfile.write("----------------------------------------" + "\n")
    for k , v in percent_votes.items():
        textfile.write(f'{k}:{v}' + "\n")
    textfile.write("----------------------------------------" + "\n")
    textfile.write("Winner:" + str(winner) + "\n")
    textfile.write("----------------------------------------" + "\n")






