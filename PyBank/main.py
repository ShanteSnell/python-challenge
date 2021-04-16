# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources','budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    rowcount  = 0
    profit_loses =0
    # Read each row of data after the header
    for row in csvreader:
        print(row[0])
        print(row[1])
        rowcount+= 1 
        profit_loses=profit_loses+int(row[1])
        # bday=11241977
        # print (bday,type(bday)) 
        # bday1='11241977'
        # print(bday1,type(bday1))
        # This how we convert a string to an int 
        int(row[1])
    print('my rowcount is',rowcount)
    print(profit_loses)    
