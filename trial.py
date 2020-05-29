import pandas as pd 
import numpy as np
import sys
import graphs as g
#file_path = "Expenses2019.xlsx"
#file_path = input("insert file_path here: ")

#db = g.Data()


# ~~~~~~~~~~~~~~Sheet Selection Portion~~~~~~~~~~~~~~~~~
db = pd.ExcelFile("Expenses2019.xlsx")
sheetlists = db.sheet_names # Array form
print(sheetlists) # Prints Sheet List


while True:
	for i in range(len(sheetlists)):
		print(str(i) + " is:  " + sheetlists[i])
	sheet_number = int(input("Type the number to access the respective Sheets "))
	if sheet_number <= len(sheetlists):
		selected_db = db.parse(sheetlists[sheet_number])
		print(selected_db)
		response = input("Do you want to sort the data? Y/N ") # DEBUG ONLY
		if (response == 'Y' or response == 'y'):
			sorted_db = selected_db.dropna(axis = 1, how="all") # drop columns if if all values are n/a, meaning drop empty columns
			print(sorted_db)
			sorted_db = sorted_db.dropna(axis = 0, how = "any") # drop rows if any value is n/a, drop rows if there is a single n/a
			print(sorted_db)
			print(sorted_db.rename(columns=sorted_db.iloc[0]).drop(sorted_db.index[0]))

		else:
			print("Wat")

	else:
		print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ("your number is not in the list")
		print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

