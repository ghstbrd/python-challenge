# -*- coding: UTF-8 -*-

"""PyPoll Homework Starter File."""



# Import necessary modules

import csv

import os



# Files to load and output (update with correct file paths)

file_to_load = os.path.join("Starter_Code", "PyPoll", "Resources", "election_data.csv")  # Input file path

file_to_output = os.path.join("Starter_Code", "Pypoll", "pypoll_analysis.txt")  # Output file path



# Initialize variables to track the election data

total_votes = 0  # Track the total number of votes cast

candidate_votes = {}  # Track candidate names and vote counts



# Winning Candidate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0



# Open the CSV file and process it

with open(file_to_load) as election_data:

    reader = csv.reader(election_data)



    # Skip the header row

    header = next(reader)



    # Loop through each row of the dataset and process it

    for row in reader:

        # Increment the total vote count for each row

        total_votes += 1



        # Get the candidate's name from the row

        candidate_name = row[2]



        # If the candidate is not already in the candidate list, add them

        if candidate_name not in candidate_votes:

            candidate_votes[candidate_name] = 0



        # Add a vote to the candidate's count

        candidate_votes[candidate_name] += 1



# Open a text file to save the output

with open(file_to_output, "w") as txt_file:

    # Prepare the output header

    output = (

        "Election Results\n"

        "-------------------------\n"

        f"Total Votes: {total_votes}\n"

        "-------------------------\n"

    )

    print(output)

    txt_file.write(output)



    # Loop through the candidates to determine vote percentages and identify the winner

    for candidate, votes in candidate_votes.items():

        # Get the vote count and calculate the percentage

        vote_percentage = (votes / total_votes) * 100



        # Update the winning candidate if this one has more votes

        if votes > winning_count:

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate



        # Print and save each candidate's vote count and percentage

        candidate_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

        print(candidate_output)

        txt_file.write(candidate_output)



    # Generate and print the winning candidate summary

    winning_candidate_summary = (

        "-------------------------\n"

        f"Winner: {winning_candidate}\n"

        "-------------------------\n"

    )

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)


