Python-Challenge
  
  /PyBank
    
    Provides a financial analysis over a time period broken up by months.
      Financial data should be provided in a csv file {budget_data.csv} (month, profit/loss).
    
    Takes in the profit or loss for a set of given months and returns the total number of months in the dataset, 
    the total profit or loss, the average change in a month, the greatest increase in profits for a month as 
    well as the greatest decrease in profits in a given month.
    
    Returns the analysis to both the terminal and a seperate .txt file {financial_analysis.txt}.
    
  /PyPoll
  
    Provides analysis of election results to calculate votes for canidates and election winner.
      Election data should be provided in csv file {election_data.csv} (voter_id, county, canidate)
      
     Takes in a voter_id's vote and counts it both in general and for the specific canidate voted for.
     
     Analysis provides total number of votes in the election, each canidates number of votes and their corresponding
     vote percentage, and an overall winner for the election.
     
     Returns the analysis both to the terminal and a seperate .txt file {election_analysis.txt}
     
  /PyBoss
  
    Converts a set of employee data to a different format for new HR standards.
      Employee data should be provided in a .csv file {employee_data.csv} (Emp ID, Name, DOB, SSN, State)
      
    Takes employee's full name and slits it into their first and last names, converts DOB from yyyy-mm-dd to
    mm/dd/yyyy, anominizes the first 5 digits of the SSN with *'s and changes the state to its postal abreviation.
    
    Returns the converted data to a new .csv file {converted_employee_data.csv}
    
  /PyParagraph
  
    Takes in a .txt file and performs a statistical analysis of it.
      Text should be in a .txt file format. Code defaults to {paragraph_ 1.txt} for analysis other file names will
      need to update code first.
      
    Returns the word count, sentence count, average word length, and average sentence length to the terminal.
    
