'''12
Reading data from a .csv file using pandas
groupby function to caluclate the mean
wage by the league and plot the results
'''
#import the Library
import pandas
#import graphing library
import matplotlib.pyplot as plt

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["league_name","wage_eur"]]

#Remove rows with missing age or value. subset checks subset of column
#Only rows where column 'league_name' and 'wage_eur' is NaN are dropped.
df = fifa_df1.dropna(subset=['league_name', 'wage_eur'])

#DataSet to calaclate the mean wage by league
df=fifa_df1.groupby(['league_name'])['wage_eur'].mean()

#print the results - test
#print(df)

# Select the first 10 leagues
#df = df.head(10)

# Print the results
print(df)

# Create a horizontal bar chart
plt.barh(df.index, df.values)

plt.title("Average Player Wage per League")
plt.xlabel("Average Player Wage (Euros)")
plt.ylabel("League")

# Make the chart fit the league names
plt.tight_layout()

plt.show()







# 
# #plotting results
# plt.plot(df.head(10))
# 
# plt.title("Wage of player according to League")
# plt.xlabel("Name of League")
# plt.ylabel("Player's Wage (Euros)")
# plt.show()



















