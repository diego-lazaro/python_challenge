#importing the code modules

import os
import csv

#creating variables to store and count data

vote_total = 0
candidates = ""
votes_won = {}
candidate_percent ={}
winning_votes = 0



#opening the files needed for specific data

poll_data = os.path.join("election_data.csv")

with open(poll_data, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

#Adding votes per candidate in candidates list

        vote_total = vote_total + 1
        candidates = row[2]
        if candidates in votes_won:
            votes_won[candidates] = votes_won[candidates] + 1
        else:
            votes_won[candidates] = 1

#taking candidates and finding percentages and totals of outcomes

for candidate, outcome in votes_won.items():
    candidate_percent[candidate] = "{0:.3%}".format(outcome / vote_total)
    if outcome > winning_votes:
        winning_votes = outcome
        winner = candidate



# And the Winner is ......

print('Election Results')
print('-------------------------')
print(f"Total Votes: {vote_total}")
print('-------------------------')
for candidate, outcome in votes_won.items():
    print(f"{candidate}: {candidate_percent[candidate]} ({outcome})")
print('-------------------------')
print(f"Winner: {winner}")
print('-------------------------')

with open('poll_results.txt', 'w') as file:
        file.write('Election results\n')
        file.write('-------------------------\n')
        file.write(f'Total Votes: {vote_total}\n')
        file.write('-------------------------\n')
        for candidate, outcome in votes_won.items():
            file.write(f'{candidate}: {candidate_percent[candidate]} ({outcome})\n')
        file.write('-------------------------\n')
        file.write(f'Winner: {winner}\n')
        file.write('-------------------------')
        file.close()
