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

    #setting initial counts    
    total_months=0
    net_total_amount=0
    plvalues=[]
    # loop thtouh the file by rows
    for row in csvreader:
        total_months+=1
        net_total_amount = net_total_amount + int(row[1])

        #creating a list of Profit/Losses values, used later to... 
        #...calculate the month to month diference
        plvalues.append([row[0],row[1]])
        
    #creating a lits, containing the month to month diference, 
    outputsum=[]
    #creating a dictionary with the assosiated month as a key 
    output={}

    for index,element in enumerate(plvalues[1:]):
        output.update({element[0]:int(element[1])-int(plvalues[index][1])})
        outputsum.append(int(element[1])-int(plvalues[index][1]))

    #calculating Average Change
    averagechange = sum(outputsum) / len(outputsum)
    #Formating average Change to 2 decimals
    averagechange = round (averagechange,2)
    #Finding Greates increase in profits
    greatestincrease = max(outputsum) 
    #Finding Greates decreases in profits
    greatestdecrease = min(outputsum)      
    #Finding the month assosiated with the Greatest increase
    greatestincreasemonth = max(output,key=output.get)
    #Finding the month assosiated with the Greatest decrease
    greatestdecreasemonth = min(output,key=output.get)
    


    #Printing values
    print("-------------------------------------------------------")
    print("Financial Analysis")
    print("-------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_amount}")
    print(f"Average  Change: $ {averagechange}")
    print(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})")
    print(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})")
    print("-------------------------------------------------------")

# Save the analysis to text file

filepathtosave = os.path.join("analysis","budget_data_analysis.txt")
with open(filepathtosave,'w') as text:
    text.write("-------------------------------------------------------" + "\n")
    text.write("Financial Analysis" + "\n")
    text.write("-------------------------------------------------------" + "\n")
    text.write(f"Total Months: {total_months}" + "\n")
    text.write(f"Total: ${net_total_amount}" + "\n")
    text.write(f"Average  Change: $ {averagechange}" + "\n")
    text.write(f"Greatest Increase in Profits: {greatestincreasemonth} (${greatestincrease})" + "\n")
    text.write(f"Greatest Decrease in Profits: {greatestdecreasemonth} (${greatestdecrease})" + "\n")  
    text.write("-------------------------------------------------------")  


     