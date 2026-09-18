'''11
Reading data from a .csv file using pandas
groupby function to caluclate the avarage
wage by the players age and plot the results
'''

#import the Library
import pandas 

#import graphing library
import matplotlib.pyplot as plt

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["wage_eur","age"]]

#Remove rows with missing age or value. subset checks subset of column
#Only rows where column 'age' and 'wage_eur' is NaN are dropped.
df = fifa_df1.dropna(subset=['age', 'wage_eur'])

df=fifa_df1.groupby("age")["wage_eur"].mean()
#print(df)

#plotting results
plt.plot(df)
plt.title("Wage of player according to their age")
plt.xlabel("Player's Age (Years)")
plt.ylabel("Player's Wage (Euros)")
plt.show()


