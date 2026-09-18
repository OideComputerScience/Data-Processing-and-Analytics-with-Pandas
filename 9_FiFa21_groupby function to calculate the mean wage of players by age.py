'''9
Reading data from a .csv file using pandas
groupby function to caluclate the mean
wage by the players age 
'''
#import the Library
import pandas


#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["wage_eur","age"]]

#Remove rows with missing age or value. subset checks subset of column
#Only rows where column 'age' and 'wage_eur' is NaN are dropped.
fifa_df = fifa_df1.dropna(subset=['age', 'wage_eur'])

#Pandas groupby() function is a powerful tool used to split a
#DataFrame into groups based on one or more columns, allowing
#for efficient data analysis and aggregation. It follows a
#"split-apply-combine" strategy, where data is divided into
#groups, a function is applied to each group, and the results
#are combined into a new DataFrame. 

print(fifa_df1.groupby("age")["wage_eur"].mean())




