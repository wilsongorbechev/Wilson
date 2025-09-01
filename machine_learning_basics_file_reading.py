import pandas as pd

"""below line is to read the ".csv" file from current file"""
df = pd.read_csv("diamonds.csv")
print(df)
print("---------------------------------------------------------------------")
#
# pd.set_option("display.max_columns",None)
# print("---------------------------------------------------------------------")
#
# """below line is to read only the "columns_names" in csv file from current file"""
# """here we are not giving read , coz we already dig into the file in 1st script"""
# columns = df.columns
# print(columns)
# print("---------------------------------------------------------------------")
#
# """below line is to read the "data_types" of columns names in csv file from current file"""
# column_data_type = df.dtypes
# print(column_data_type)
# print("---------------------------------------------------------------------")
#
# """below line is to get the information about dataset in csv file from current file"""
# df_information = df.info()
# print(df_information)
# print("---------------------------------------------------------------------")
#
# """below function provide details only about details of numerical column"""
# df_description = df.describe()
# print(df_description)
# print("---------------------------------------------------------------------")

# """to read a single column data"""
# single_column = df['carat']
# print(single_column)
# print("---------------------------------------------------------------------")
#
# """to read more than one column data"""
# single_column = df[['carat',"cut"]]
# print(single_column)
# # print("---------------------------------------------------------------------")
#
# """to read first 5 number of rows"""
# data=df.head()
# print(data)
# print("---------------------------------------------------------------------")
#
# """to read last 5 number of rows"""
# data=df.tail()
# print(data)
# print("---------------------------------------------------------------------")
#
# """to read first specific number of rows"""
# data=df.head(10)
# print(data)
# print("---------------------------------------------------------------------")

# """below concept is called SLICING that cuts the rows in the given numeric order"""
# data = df[10:20] #it will return teh rows from 10 to 19
# print(data)
# print("---------------------------------------------------------------------")
#
# """locator function that returns all the specified number rows"""
# data = df. loc[10:20] #it will return teh rows from 10 to 20
# print(data)
# print("---------------------------------------------------------------------")
#
# """it will return the rows from 10 to 20 for specific column"""
# data = df.loc[10:20, "carat"] #doubt why when i remove.here after df it throws error?
# print(data)
# print("---------------------------------------------------------------------")
#
# """it will return the rows from 10 to 20 for specific columns"""
# data = df. loc[10:20, ["carat", "cut"]]
# print(data)
# print("---------------------------------------------------------------------")
#
# """it will return the rows from 10 to 20 for specific columns in numbers"""
# data=df.iloc[10:20,1:4]
# print(data)
# # print("---------------------------------------------------------------------")
#
# """it will return the rows from 10 to 20 for specific columns in numbers at different place"""
# data=df.iloc[10:20,[1,5,7]]
# print(data)