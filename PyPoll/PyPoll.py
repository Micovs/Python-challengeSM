# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

# Set path for the file we want to open
csvpath = os.path.join("Resources","election_data.csv")

# Open the CSV
with open(csvpath) as election_data_file:
    csvreader = csv.reader(election_data_file)

    # Reading and skipping the header row 
    csv_header = next(csvreader)

    # starting values
    total_votes=0
    listofcandidates=[]

    #loop throuhg the file by rows
    for row in csvreader:

        #Count the total votes and create a list of candidates names
        total_votes+=1
        listofcandidates.append(row[2])
    
    #As a test, the lenght (len) of listofcandidates should be same with the total votes, 
    # since each candidate got one vote, represented by their name in the list of candidates. 
    # print(len(listofcandidates))

    # Getting the unique names in the list of candidates
    list_set=set(listofcandidates)
    # print(list_set) Printing as a test
    uniquelist=list(list_set)
    # print(uniquelist) Printing as a test
    
    numberofvotes=[]

    #Printing values
    print("-------------------------")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:: {total_votes}")
    print("-------------------------") 

    # Save the analysis to text file

filepathtosave = os.path.join("analysis","election_data_analysis.txt")
with open(filepathtosave,'w') as text:

    text.write("-------------------------" + "\n")
    text.write("Election Results" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Total Votes:: {total_votes}" + "\n")
    text.write("-------------------------" + "\n")

    # output={} as test

    # For each unique candidate, we loop through the total list of candidates. 
    # Aquiring the total number of ocurances/votes, 
    # calculating the percentage of votes the candidate won, and printing the results.
    for candidate in uniquelist:
        count=0
        for i in listofcandidates:
            if candidate == i:
                count+=1
        numberofvotes.append(count)

        # output.update({candidate:count}) As a test, 
        
        percentofvotes = '{0:.00%}'.format(count / total_votes) 
        # printing and saving to file       
        print(f"{candidate}: {percentofvotes} ({count})") 
        text.write(f"{candidate}: {percentofvotes} ({count})" + "\n")
         
    # print(numberofvotes)
    winnervotes=max(numberofvotes)
    winnervotesindex=numberofvotes.index(winnervotes)
    # print(winnervotes)
    winnername =uniquelist[winnervotesindex] 
    # print(winnername)

    print("-------------------------")  
    print(f"Winner {winnername}")  
    print("-------------------------")  

    text.write("-------------------------" + "\n")  
    text.write(f"Winner {winnername}" + "\n")  
    text.write("-------------------------" + "\n")




    
    