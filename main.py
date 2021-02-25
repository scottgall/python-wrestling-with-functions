import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join("Resources", "WWE-Data-2016.csv")
# Define the function and have it accept the 'wrestlerData' as its sole parameter
def print_percentages(wrestlerData):
  name = wrestlerData[0]
# Find the total number of matches wrestled
  matches = sum(map(int, wrestlerData[1:]))
# Find the percentage of matches won
  won = int(wrestlerData[1])/matches*100
# Find the percentage of matches lost
  lost = int(wrestlerData[2])/matches*100
# Find the percentage of matches drawn
  drawn = int(wrestlerData[3])/matches*100
# Print out the wrestler's name and their percentage stats
  output = "Wrestler: {}\n".format(name)
  output += "Total matches: {}\n".format(matches)
  output += "Percent won: {:.2f}%\n".format(won)
  output += "Percent lost: {:.2f}%\n".format(lost)
  output += "Percent drawn: {:.2f}%\n".format(drawn)
  print(output)

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

  # Split the data on commas
  csvreader = csv.reader(csvfile, delimiter=',')

  # Prompt the user for what wrestler they would like to search for
  name_to_check = input("What wrestler do you want to look for? --> ")

  found = False
  # Loop through the data
  for row in csvreader:

    # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
    if(name_to_check.lower() == row[0].lower()):
      print_percentages(row)
      found = True
      break
    
  if found == False:
    print("We didn't find {}.".format(name_to_check))
        
