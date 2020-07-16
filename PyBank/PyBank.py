# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Set path for file i want to open
csvpath = os.path.join("Resources","budget_data.csv")


# Open the CSV
with open(csvpath) as budget_data_file:
    csvreader = csv.reader(budget_data_file)

    # Reading and skipping the header row 
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #setting initial counts    
    total_months=0
    net_total_amount=0
    plvalues=[]
    # for loop to loop thtouh the file by rows
    for row in csvreader:
        total_months+=1
        net_total_amount = net_total_amount + int(row[1])

        #creating a list of Profit/Losses values, used later to... 
        #...calculate the month to month diference
        plvalues.append(row[1])
    
    #creating a lits, containing the month to month diference 
    output=[]
    for index,element in enumerate(plvalues[1:]):
        output.append(int(element)-int(plvalues[index]))

    #calculating Average Change
    averagechange=sum(output)/len(output)
    #Formating average Change to 2 decimals
    averagechange=round(averagechange,2)       
        
    #Printing values
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_amount}")
    print(f"Average  Change: $ {averagechange}") 