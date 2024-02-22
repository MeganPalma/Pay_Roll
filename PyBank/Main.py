# PyBank 

import os
import csv

#Path to collect data from budget_data copy CVS File 
PyBank_CSV = os.path.join('source', 'budget_data copy.csv')
Outputpath = os.path.join ('Analysis', 'Budget_Analysis.txt')

#Read in CVS File 
with open(PyBank_CSV, 'r') as csvfile: 
 #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    header = next(csvreader)
    #Convert cvsreader into a list to iterate through it multiple times 
    data = list(csvreader)

# Define the function and have it accept the 'Sales_data' as its sole parameter
#CSV header: Date (Manth Name & Date), Profit/Losses
    def print_results(data):
    
    #Total Number of Months in Data Set 
        #Count the number of rows excluding header (excluding header is above)
        Total_Months = len(data)

    #Net total amount of "Profit/Losses" over the entire period
        Net_Profit_Losses = sum(int(row[1]) for row in data)

    #Changes in "Profit/Losses" over the entire period, and then the average of those changes
    # Calculate the changes in profit/losses
        changes = [int(data[i+1][1]) - int(data[i][1]) for i in range(len(data) - 1)]
    
    # Calculate the average of the changes
        Average_Profit_Losses = sum(changes) / len(changes)

    #Greatest Increase in Profits - Print Month Name & Date and $$$$
        Greatest_Profit_Increase = max(changes)
        Greatest_Profit_Increase_index = changes.index(Greatest_Profit_Increase)
        Greatest_Profit_Increase_date = data[Greatest_Profit_Increase_index + 1][0]

    #Greatest Decrease in Profits - Print Month Name & Date and $$$$
        Greatest_Profit_Decrease = min(changes)
        Greatest_Profit_Decrease_index = changes.index(Greatest_Profit_Decrease)
        Greatest_Profit_Decrease_date = data[Greatest_Profit_Decrease_index + 1][0]
    
        with open(Outputpath, 'w') as Output_file: 
            Output_file.write("Financial Analysis\n")
            Output_file.write("----------------------------\n")
            Output_file.write(f"Total Months: {Total_Months}\n")
            Output_file.write(f"Total Profit/Losses: ${Net_Profit_Losses}\n")
            Output_file.write(f"Average Change: ${Average_Profit_Losses:.2f}\n")
            Output_file.write(f"Greatest Increase in Profits: {Greatest_Profit_Increase_date} (${Greatest_Profit_Increase})\n")
            Output_file.write(f"Greatest Decrease in Profits: {Greatest_Profit_Decrease_date} (${Greatest_Profit_Decrease})\n")

     #Print out Results 
        print("Financial Analysis")
        print("----------------------------")
        print("Total Months:", Total_Months)
        print(f"Total Profit/Losses: ${Net_Profit_Losses}")
        print(f"Average Change: ${Average_Profit_Losses:.2f}")
        print(f"Greatest Increase in Profits: {Greatest_Profit_Increase_date} (${Greatest_Profit_Increase})")
        print(f"Greatest Decrease in Profits: {Greatest_Profit_Decrease_date} (${Greatest_Profit_Decrease})")

#Print results 
print_results(data)


