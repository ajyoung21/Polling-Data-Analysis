#Imports the tools we need to read the csv.
import os
import csv

csvpath = os.path.join('election_data.csv')

#Opens the csv.
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    

    total_votes = 0

    # Read each row of data after the header
    candidate_list = []
    
    #Since the csvreader only works once, we're going to make a duplicate list so that
    #we can iterate over it later.
    duplicate_list = []

  
   # Read each row of data after the header
    for row in csvreader:
        #counts the number of total votes
        total_votes = total_votes + 1
        #Duplicates the votes to another list so we can iterate over it later.
        duplicate_list.append(row[2])

        #creates a list of the names of allof the candidates.
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        

    vote_totals = []

    #Iterates over each vote one time for each candidate. It counts the number of votes
    #for that candidate and then puts the total into the vote_totals list. The vote_totals
    #list will be in the same order as the candidate list.
    for candi in candidate_list:
        vote_counter = 0
        for vote in duplicate_list:
            if candi == vote:
                vote_counter = vote_counter + 1
        vote_totals.append(vote_counter)


    #Prints the Total votes portion of our analysis
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")

    #sets it so that the winner variable is the first candidate in candidate_list
    winner = vote_totals[0]
    winner_marker = 0

    #iterates over the candidates to see which one got the most votes
    for i in range(0,len(candidate_list)):
        if vote_totals[i] > winner:
            winner = vote_totals[i]
            #keeps track of the relative reference of the winner
            winner_marker = i
        
        #calculates the share of votes for each candidate
        voter_share = vote_totals[i]/total_votes
        #Changes voter_share to a percentage with 3 decimal places
        percent_vs = "{:.3%}".format(voter_share)
        #Prints each candidates' name, percent_vs, and total votes.
        print(f"{candidate_list[i]}: {percent_vs} ({vote_totals[i]})")
    print("-----------------------------")
    print(f"Winner: {candidate_list[winner_marker]}")
    print("-----------------------------")
  