'''3
Reading data from a .csv file using pandas
to look at specific columns and finding the Irish players
'''

#import pandas Library
import pandas

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["short_name","age","value_eur","nationality"]]

#Filtering by nationality
irish_players_df=fifa_df1[fifa_df1["nationality"]=="Republic of Ireland"]

print(irish_players_df)