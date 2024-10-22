# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define a dictionary to track candidate names and vote counts
candidates = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

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
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print header and total votes
    header = "Election Results\n"
    separator = "-------------------------\n"
    print(header + separator)
    txt_file.write(header + separator)

    # Write the total vote count to the text file
    total_votes_output = f"Total Votes: {total_votes}\n"
    print(total_votes_output)
    txt_file.write(total_votes_output)
    print(separator)
    txt_file.write(separator)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidates.items():
        # Calculate the percentage of votes
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(output, end="")
        txt_file.write(output)

    # Generate and print the winning candidate summary
    winning_summary = f"-------------------------\nWinner: {winning_candidate}\n-------------------------\n"
    print(winning_summary)
    txt_file.write(winning_summary)
