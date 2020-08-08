#Py Poll Script
# For import the os and csv
import os
import csv
import math

# Assign the csv file path to an object
csvpath = os.path.join(r'C:\Users\Mr. Me Too\Desktop\python-challenge\PyPoll\Resources\election_data.csv')

#Opening the csv and skipping the header row
with open (csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter= ',')
  csv_header = next(csvfile) 

#Adding csv data into a list/unzip list into unique list
  polldata =[data for data in csvreader]

  total_votes = len(polldata)
  voterID, county, candiate = zip(*polldata)
  list_candiate = list(candiate)

  khan= []
  correy= []
  li= []
  oTooley = []
  i = 1

#Loop to seperate candiates votes in their own list
  for person in list_candiate:
    if person == "Khan":
      khan.append(person)
      i += 1
    elif person == "Correy":
      correy.append(person)
      i += 1
    elif person == "Li":
      li.append(person)
      i += 1
    else:
      oTooley.append(person)
      i += 1 

# Obtaining the sum of votes for each candiate
  khan_total =len(khan)
  khan_round = int(round((len(khan)/total_votes)*100,1))

  correy_total = len(correy)
  correy_round = int(round((len(correy)/total_votes)*100,1))

  li_total = len(li)
  li_round = int(round((len(li)/total_votes)*100,1))

  oTooley_total = len(oTooley)
  oTooley_round = int(round((len(oTooley)/total_votes)*100,1))

#Winner based on popoular vote
  if khan_total > correy_total and khan_total > li_total and khan_total > oTooley_total:
    popular_vote = "Khan"
  elif: correy_total > & khan_total and correy_total > li_total and correy_total > oTooley_total:
    popular_vote = "Correy"
  elif: li_total > & correy_total & khan_total & oTooley_total:
    popular_vote = "Li"
  else:
    popular_vote = "O'Tooley"

#Ouput
  print("Election Results")
  print(25*"-")
  print(f'Total votes: {total_votes}')
  print(25*"-")
  print(f'Khan: {khan_round}.000% ({khan_total})')
  print(f'Correy: {correy_round}.000% ({correy_total})')
  print(f'Li: {li_round}.000% ({li_total})')
  print(f"O'Tooley: {oTooley_round}.000% ({oTooley_total})")
  print(25*"-")
  print(f"Winner: {popular_vote}")
  print(25*"-")
  with open ("election_results.txt","w") as er:
     print("Election Results", file = er)
     print(25*"-", file = er)
     print(f'Total votes: {total_votes}', file = er)
     print(25*"-", file = er)
     print(f'Khan: {khan_round}.000% ({khan_total})', file = er)
     print(f'Correy: {correy_round}.000% ({correy_total})', file = er)
     print(f'Li: {li_round}.000% ({li_total})', file = er)
     print(f"O'Tooley: {oTooley_round}.000% ({oTooley_total})", file = er)
     print(25*"-", file = er)
     print(f"Winner: {popular_vote}", file = er)
     print(25*"-", file = er)