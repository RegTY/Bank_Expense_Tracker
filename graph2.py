import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# FOR REFERENCE : FILE PATH IS "../Expenses2019.xlsx"

class Data:
	""" A class which represents a specific sheet of an excel spreadsheet
		It will contain the methods of analysis on that specific sheet"""

	def __init__(self, file_path = None,sheet_name = None):

		if file_path== None:
			self.file_path=input('Excel File Path :')
		else :
			self.file_path = file_path

		if sheet_name == None:
			sheetlists = pd.ExcelFile(self.file_path).sheet_names
			print(sheetlists)

			for i in range(len(sheetlists)):
				print(str(i) + " is: " + sheetlists[i])
			sheet_number = int(input("Type the number corresponding to that specific sheet")) 

			self.sheet_data =pd.ExcelFile(self.file_path).parse(sheetlists[sheet_number])
		else:
			self.sheet_data = pd.ExcelFile(self.file_path).parse(sheet_name)
		sns.set()
		print("Data Initialized")
		print(self.sheet_data)

		self.sheet_data = self.sheet_data.dropna(axis = 1, how="all")
		self.sheet_data = self.sheet_data.dropna(axis = 0, how = "any")
		self.sheet_data= self.sheet_data.rename(columns=self.sheet_data.iloc[0]).drop(self.sheet_data.index[0])
		print("Data Cleaned!")
		print(self.sheet_data)


	def dbankLine(self):

		"""Generates a line graph with time day as x-axis to show both the commulative spending throught the entire time as well as the normal daily spending"""
		expenses = self.sheet_data
		new_raw = expenses.set_index('Date')
		
		# Sum the duplicate dates
		sum_data = new_raw.sum(level=0)

		# Makes all object as datetime64
		sum_data.index = pd.to_datetime(sum_data.index.astype(str), errors = 'coerce')

		# Creates a range of dates from the first day to the last day from the index
		idx_day = pd.date_range(start=sum_data.index.min(), end=sum_data.index.max())

		# Reindex with the new dates
		l_data = sum_data.reindex(idx_day, fill_value=0).rename_axis('Date')
		# Renames some columns don't mind me
		
		l_data = l_data.rename(columns = {"Price": "Daily Expenses"})  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<
		l_data = sum_data.resample('D').sum()
		l_data['Balance'] =(l_data['In'] - l_data['Out']).cumsum()
		#-----------------------------------------------#

		#--------------------Plotting-------------------#
		fig = plt.figure()
		ax = plt.axes()
		plt.xticks (rotation = 45)
		plt.xlabel(" Date since November 2018")
		plt.ylabel(" Amount (MYR)")
		plt.title(" Total Daily Expenses")

		dateFormat = mdates.DateFormatter('%Y %B')
		ax.xaxis.set_major_formatter(dateFormat)


		print(l_data)
		ax = sns.lineplot( data=l_data, dashes = False)
		#ax = sns.lineplot(x=l_data.index , y=l_data['Price'].cumsum(), hue="Price")
		
		#------------------------------------------------#
		plt.show()

	def mbankLine(self):
		"""Generates a line graph with time day as x-axis to show both the commulative spending throught the entire time as well as the normal Monthly spending"""
		expenses = self.sheet_data
		new_raw = expenses.set_index('Date')
		
		# Sum the duplicate dates
		sum_data = new_raw.sum(level=0)

		# Makes all object as datetime64
		sum_data.index = pd.to_datetime(sum_data.index.astype(str), errors = 'coerce')
		l_data = sum_data.resample('M').sum()
		print(l_data)


		l_data['Balance'] =(l_data['In'] - l_data['Out']).cumsum()

		# Renames some columns don't mind me
		l_data = l_data.rename(columns = {"Price": "Daily Expenses"})  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<
		#-----------------------------------------------#

		#--------------------Plotting-------------------#
		fig = plt.figure()
		ax = plt.axes()
		plt.xticks (rotation = 45)
		plt.xlabel(" Date since November 2018")
		plt.ylabel(" Amount (MYR)")
		plt.title(" Total Daily Expenses")

		dateFormat = mdates.DateFormatter('%Y %B')
		ax.xaxis.set_major_formatter(dateFormat)


		ax = sns.lineplot( data=l_data, dashes = False)
		#ax = sns.lineplot(x=l_data.index , y=l_data['Price'].cumsum(), hue="Price")
		
		#------------------------------------------------#
		plt.show()






	# def dLine(self):
	# 	expenses = self.sheet_data

	# 	#-----------Filters and Cleans Data----------#
	# 	# Makes the data column as index
	# 	new_raw = expenses.set_index('Date')
		
	# 	# Sum the duplicate dates
	# 	sum_data = new_raw.sum(level=0)

	# 	# Makes all object as datetime64
	# 	sum_data.index = pd.to_datetime(sum_data.index.astype(str), errors = 'coerce')

	# 	# Creates a range of dates from the first day to the last day from the index
	# 	idx_day = pd.date_range(start=sum_data.index.min(), end=sum_data.index.max())

	# 	# Reindex with the new dates
	# 	l_data = sum_data.reindex(idx_day, fill_value=0).rename_axis('Date')

	# 	# Makes a column with cummulative values
	# 	l_data = l_data.drop(columns = l_data.columns[len(l_data.columns)-1])
	# 	print(l_data.cumsum())
	# 	l_data['Cummulative expenses'] = l_data.cumsum()
	# 	# # Renames some columns don't mind me
	# 	# l_data = l_data.rename(columns = {"Price": "Daily Expenses"}) 
	# 	# #-----------------------------------------------#

	# 	# #--------------------Plotting-------------------#
	# 	# fig = plt.figure()
	# 	# ax = plt.axes()
	# 	# plt.xticks (rotation = 45)
	# 	# plt.xlabel(" Date since November 2018")
	# 	# plt.ylabel(" Amount (MYR)")
	# 	# plt.title(" Total Daily Expenses")

	# 	# dateFormat = mdates.DateFormatter('%Y %B')
	# 	# ax.xaxis.set_major_formatter(dateFormat)


	# 	# print(l_data)
	# 	# ax = sns.lineplot( data=l_data, dashes = False)
	# 	# #ax = sns.lineplot(x=l_data.index , y=l_data['Price'].cumsum(), hue="Price")
		
	# 	# #------------------------------------------------#
	# 	# plt.show()


 

if __name__ == "__main__":
	test_Data = Data("Expenses2019.xlsx", "Cimb Bank")
	test_Data.dbankLine()


