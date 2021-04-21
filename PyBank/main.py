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
    max_month =""
    min_month =""
    max_profit =0
    min_profit =0
    month_change =0
    running_change =0
    change_list =list()
    prev_profit_lose =0
    # Read each row of data after the header
    for row in csvreader:
        print(row[0])
        print('pf',row[1])
        # prev_profit_lose = int(row[1])
        rowcount+= 1 
        profit_loses=profit_loses+int(row[1])
        month_change =int(row[1])-prev_profit_lose
        if rowcount>1:
            running_change =running_change+month_change
        if int(row[1]) > max_profit:
            max_profit =month_change
            max_month =row[0]
        if int(row[1]) < min_profit:
            min_profit =month_change
            min_month =row[0]


        print('delta',month_change)
        print('prev',prev_profit_lose)
        print(running_change)
        #change_list.append(month_change)
        #change_list.append (int(row[1]))
        #print("len list",len(change_list))
        #print("sum list",sum(change_list))
        prev_profit_lose = int(row[1])
        # bday=11241977
        # print (bday,type(bday)) 
        # bday1='11241977'
        # print(bday1,type(bday1))
        # This how we convert a string to an int 
        int(row[1])
    print('Financial Analysis')
    print('---------------------------------------')
    print('Total Months: ',rowcount)
    print('Total profit: $',profit_loses)  
    #print("average change: $",sum(change_list) / len(change_list))
    print("Average Change: $",running_change / (rowcount-1))
    print(f"Greatest Increase In Profit: {max_month}  (${max_profit})")
    print(f"Greatest Decrease In Profit: {min_month}  (${min_profit})")

    f = open("OutputFile.txt","w")                    # create / open output file
    f.write('Financial Analysis\n')
    f.write('---------------------------------------------------\n')
    f.write("Total Months: {}\n".format(rowcount))   # create formatted string to write to file. The /n is a new line character
    f.write("total profit: ${}\n".format(profit_loses))
    f.write("average change: $ {}\n".format(round(running_change / (rowcount-1),2)))  # round to 2 decimal places (money)
    f.write("greatest increase in profit: {}  (${})\n".format(max_month,max_profit))
    f.write("greatest decrease in profit: {}  (${})\n".format(min_month,min_profit))
    f.close                                           # close file when done