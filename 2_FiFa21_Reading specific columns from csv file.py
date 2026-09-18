'''2
Reading data from a .csv file using pandas
to look at specific columns
'''

#import pandas Library
import pandas

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#print(fifa_df)
#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["short_name","age","value_eur", "nationality"]]

#prints dataframe
print(fifa_df1)

#select just one column with all its rows
#values=fifa_df["value_eur"]
#print(values)

#Selecting a single column(.head(10) picks the the first 10 rows only)
# print(fifa_df1.head(10))
# print(fifa_df1.tail(10))

