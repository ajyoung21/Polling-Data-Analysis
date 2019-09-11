
#Imports the tools we need to read the csv.
import os
import csv

csvpath = os.path.join('budget_data.csv')

#Opens the csv.
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)

    #Defines variables that we will use when iterating over the csvreader
    total_months = 0
    total_profits = 0

    #Creates a blank list that we can put the residual changes in between the last_profit
    #and this_profit.
    change_list = []
    last_profit = 0
    this_profit = 0
 

    for row in csvreader:
        #Counts total number of months
        total_months = total_months + 1
        this_profit = int(row[1])
        total_profits = total_profits + this_profit
        change = this_profit - last_profit
        change_list.append([row[0],change])
        #By having a staggered last_profit and this_profit, we can calculate the change which we can
        #append to our change_list
        last_profit = this_profit

    sum_change = 0
    #We make this counter so that we can later create reference markers for the GIP and GDP
    counter = 0
    #GIP = Greatest Increase in Profits
    GIP = 0
    GIP_marker = 0
    #GDP = Greatest Decrease in Profits
    GDP = 0
    GDP_marker = 0

    for ch in change_list:
        sum_change = sum_change + int(ch[1])
        counter = counter + 1
        #We create these reference markers so that we can use references to print the month that corresponds
        #with our GIP and GDP in our print statements.
        if int(ch[1]) > GIP:
            GIP = int(ch[1])
            GIP_marker = counter -1
        if int(ch[1]) < GDP:
            GDP = int(ch[1])
            GDP_marker = counter -1
    
    #Note: The change list adds the first, starting value, even though it's not changing from
    #a previous value (it's the first value after all). Thus, our equation needs to not include
    #this value. (Alternatively, we could have removed the first value from the list but this
    # works too.)
    average_change = (sum_change - change_list[0][1]) / (len(change_list) - 1)
        
    
    #Prints our analysis.
    print("Financial Analysis")
    print("--------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profits: ${total_profits}")
    print("Average Change: $%.2f" % average_change)
    print(f"Greatest Increase in Profits: {change_list[GIP_marker][0]} ${change_list[GIP_marker][1]}")
    print(f"Greatest Decrease in Profits: {change_list[GDP_marker][0]} ${change_list[GDP_marker][1]}")
    
    
    
