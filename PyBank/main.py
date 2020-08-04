
#Py Me Up Charlie
# For import the os and csv
import os
import csv
import math
#Assign the csv file path to an object
csvpath = os.path.join(r"C:\Users\Mr. Me Too\Desktop\python-challenge\PyBank\Resources\budget_data.csv")
#open the csv with a "with statement"
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvfile) #moves past the header
#List store strings as integers 
    total = []
    budgetdata = [data for data in csvreader]
#Unzip date and dollars into two seperate list
    date,dollars = zip(*budgetdata)
    list_dollars = list(dollars)
    list_date = list(date)
# Manipulate dollar and date list into integers and strings for Calculations
    months = len(date)
    for numbers in list_dollars:
        total.append(int(numbers))
    Total = (sum(total)) 
#Greatest increase in proftis and its date
    great_profit = max(total)
    Sgreat_profit = str(max(total))
    where_Pdollars = list_dollars.index(Sgreat_profit)
    what_Pdate = list_date[where_Pdollars]

    great_loss = min(total)
    Sgreat_loss = str(min(total))
    where_Ldollars = list_dollars.index(Sgreat_loss)
    what_Ldate = list_date[where_Ldollars]
#Finding the average of profits/loses entire time frame

    average = Total/len(list_dollars)
    print(average)

    print ("Financail Analsysis")
    print (25*"-")
    print (f"Total Months: {months}")
    print (f"Total: ${Total}")
    print (f"Average Change: ${average}")
    print (f"Greatest Increase in Progits: {what_Pdate} {Sgreat_profit}")
    print (f"Greatest Decrease in Progits: {what_Ldate} {Sgreat_loss}")


#exporting to text file
    with open ("budegt_data_output.txt", "w") as bdo:
        print ("Financail Analsysis", file =bdo)
        print (25*"-",file = bdo)
        print (f"Total Months: {months}", file = bdo)
        print (f"Total: {Total}", file = bdo)
        print (f"Average Change: ${average}", file = bdo)
        print (f"Greatest Increase in Progits: {what_Pdate} {Sgreat_profit}", file = bdo)
        print (f"Greatest Decrease in Progits: {what_Ldate} {Sgreat_loss}", file = bdo)
       
        

#Get average of both Profit and Losses list
# def average (#list):
#   length = len(#list)
#   total = 0.0
#   for numbers in profits:
#     total += numbers
#   return total/length  
  

# EXAMPLE
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 

 
 

# ----------------------------------------------

#Py Poll Script

## For import the os and csv

#Assign the csv file path to an object

#open the csv with a "with statement"

#Read and print to make sure your in the file the data 

### Get the total number of votes cast

#Seperate Candiates into a list

#Calclulate the percentage of votes each candiate wont (Candiate votes/total)

#Find the winner with the populare vote

#write output to a new text file 