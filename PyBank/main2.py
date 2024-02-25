"""Modules"""
import os
import csv

#Gets file path
csvpath = os.path.join("Resources", "budget_data.csv")

#Opens the file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    """
        Calculate Total Months
        The total number of months included in the dataset
        Calculates the number of rows (Calculates Total Months)
    """
    
    #Rowcount includes header
    rowcount = sum(1 for row in csvreader)
    
    """Calculate Total Months - need to exclude header"""
    totalmonths = str(rowcount)
    
    """
        The net total amount of "Profit/Losses" over the entire period
        When addition is used it will take into account negative numbers (losses)
    
    """
    
#Iterate through each row in the CSV file
# Open the CSV file



with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Need to store changes
    changes = []

    header = next(csvreader)

    column_index = header.index('Profit/Losses')

    #Initializes total outside of loop
    total = 0

    # Iterate through each row in the CSV file
    for row in csvreader:
        #CSV cells are string
        value = int(row[column_index])

        #Add the value to the total.
        total += value


"""
#The changes in "Profit/Losses" over the entire period, 
#and then the average of those changes
"""

with open(csvpath, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    header = next(csv_reader)

    # Initialize variables
    previous_profit_loss = None
    changes = []


    """
    Max Changes
    """
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Assuming 'Profit/Loss' is the second column (index 1)
        current_profit_loss = int(row[1])

        # Check if it's not the first row
        if previous_profit_loss is not None:
            #List of the averge changes in "Profit/Losses" over the entire period
            change = current_profit_loss - previous_profit_loss
            changes.append(change)

        # Update the previous_profit_loss for the next iteration
        previous_profit_loss = current_profit_loss

# Calculate the average of the changes
average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

max_value = max(changes)

with open(csvpath, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    header = next(csv_reader)

    # Initialize variables
    previous_profit_loss = None
    changes = []


    """
    Min Changes
    """
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Assuming 'Profit/Loss' is the second column (index 1)
        current_profit_loss = int(row[1])

        # Check if it's not the first row
        if previous_profit_loss is not None:
            #List of the averge changes in "Profit/Losses" over the entire period
            change = current_profit_loss - previous_profit_loss
            changes.append(change)

        # Update the previous_profit_loss for the next iteration
        previous_profit_loss = current_profit_loss

# Calculate the average of the changes
average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

min_value = min(changes)
    
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + totalmonths)
print("Total: $" + str(total))
print("Average Change: $", average_change)
print("Greatest Increase in Profits:" + str(max_value))
print("Greatest Decrease in Profits: " + str(min_value))
#Line6 = "Greatest Increase in Profits: Aug-16 ($1862002)"
#Line6 = "Greatest Increase in Profits: Aug-16 ($1862002)"
#Line7 = "Greatest Decrease in Profits: Feb-14 ($-1825558)"