'''5a
Reading data from a .csv file using pandas
selecting a specfic row using the loc keyword
'''

#import the Library
import pandas

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all there rows
fifa_df1=fifa_df[["short_name","age","value_eur","nationality"]]

#Filter by row using loc keyword, see code example 5
player_df=fifa_df1.loc[fifa_df1['short_name']=="K. De Bruyne"]
print(player_df)

