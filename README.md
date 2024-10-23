# python-
PyBank
Create a Python script that analyzes the records to calculate each of the following values:
The total number of months included in the dataset.
The net total amount of "Profit/Losses" over the entire period.
The changes in "Profit/Losses" over the entire period, and then the average of those changes.
The greatest increase in profits (date and amount) over the entire period.
The greatest decrease in profits (date and amount) over the entire period.
    input the resources file ""budget_data.csv".
    output into the file "budget_analysis.txt".
    read the input file, skip the header, and run the for loop to calculate the outputs.
    The output will be printed with the format:
        "Financial Analysis"
    "----------------------------"
    "Total Months: total_months"
    "Net Total Profit/Losses: $total_net :  total_net += profit_loss"
    "Average Change: $average_change = sum(net_changes) / len(net_changes) if net_changes else 0"
    "Greatest Increase in Profits: greatest_increase = net_change if net_change > greatest_increase"
    "Greatest Decrease in Profits: greatest_decrease = net_change if net_change < greatest_decrease"

PyPoll
Create a Python script that analyzes the votes and calculates each of the following values:
The total number of votes cast.
A complete list of candidates who received votes.
The percentage of votes each candidate won.
The total number of votes each candidate won.
The winner of the election based on popular vote.
    input the resources file "election_data.csv".
    output into the file "election_analysis.txt".
    read the input file, skip the header, and run the for loop to find the outputs.
    The output will be printed with the format:
    "Election Results"
    "----------------------------"
    "Total Votes: total_votes"
    "----------------------------"
    "candidate: vote_percentage"
    "----------------------------"
    "Winner: candidate that if votes > winning_count "
    "----------------------------"
