import pandas as pd

class ExcelLib:

	def readFile(self, filePath, sheetName):
		df = pd.read_excel(filePath, sheetName, header=0, index_col=0)
		#print(df)
		return df

	def readCol(self, df):
		colms = df.columns
		print(colms)

	def readRow(self, df, rowId):
		rowIndex = df.loc[rowId]
		return rowIndex

	def readCell(self, rowIndex):		
		print(str(rowIndex['Name']))


### Add validation to check if file present
### Add validation to check sheet exists
### Add validation to check if column exists

if __name__ == "__main__":

	filePath = "F:\\Study\\RobotFramework\\RF_Pilot\\TestAsset\\DataTables\\DataTable.xlsx"
	obj = ExcelLib()
	df= obj.readFile(filePath, "Data")
	rowIndex= obj.readRow(df, 'TC_01')
	#print(rowIndex)
	obj.readCell(rowIndex)

