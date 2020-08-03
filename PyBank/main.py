
#Py Me Up Charlie
# For import the os and csv
import os
import csv

#Assign the csv file path to an object
csvpath = os.path.join("..","Resources","budget_data.csv")
#open the csv with a "with statement"
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    csv_header = next(csvfile) #moves past the header
    print(f"Header: {csv_header}")

    #List for different variables 
    budgetdata = []
    profits = []
    losses = []
    
    budgetdata = [data for data in csvreader]
    print(len(budgetdata))
    months= len(budgetdata)
    
 
#Get the total number of months = the 'len' function
    total_months = len(budgetdata) 
    print(f'"The total number of months is: {months}")

#Spilt the profit losses  column into two seperate list
#check how the file output to determine how to loop through the csv.
#then make a list for each piece of dats and append 
#with a loop

#Get net total amount of both Profit list and Losses list
# total_profits = sum(profits)
# total_loses = sum(losses)
# total_cash = sum(profits)+sum(losses)

#Get average of both Profit and Losses list
# def average (#list):
#   length = len(#list)
#   total = 0.0
#   for numbers in profits:
#     total += numbers
#   return total/length  
  
#Find the row with the greatest increase/decrease and its date
#  use dictionary csvdictionary to loop throgh dates and values
#  then use a if statement for greatest increase/decrease and append to another
#  list great_Increase =[] and great_ decrease =[]


#Date format in "Feb-2013"

#Dollar amount in "$00000" add "$" string

#write output to a new text file
# print to terminal

# print (f'
# Financail Analysis\n
# -------------------------\n
# Total Months: {total_months}\n+
# Total: {total_cash}\n
# Average Change: ${avg}\n
# Greatest Increase in Profits:{great_increase/date}\n
# Greatest Decrease in Profits: {great_decrease}')may have to use . format (key,value)

# EXAMPLE
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 

 
 

----------------------------------------------

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