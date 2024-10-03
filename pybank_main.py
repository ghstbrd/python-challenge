# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.pa"Desktop", "Classwork", "Homework", "Module 3 HW", "Starter_Code", "PyBank", th.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
changes = []
months = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract the first row to initialize tracking of changes
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_value = int(first_row[1])

    # Process each row of data
    for row in reader:
        month = row[0]
        profit_loss = int(row[1])
        
        # Track the total number of months
        total_months += 1
        
        # Track the total net amount
        total_net += profit_loss
        
        # Calculate the monthly change
        change = profit_loss - previous_value
        changes.append(change)
        months.append(month)
        
        # Update previous value
        previous_value = profit_loss

# Calculate the average net change across the months
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
max_increase = max(changes)
max_increase_month = months[changes.index(max_increase)]

max_decrease = min(changes)
max_decrease_month = months[changes.index(max_decrease)]

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
    f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

