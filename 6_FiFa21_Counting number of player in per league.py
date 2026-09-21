'''6
Reading data from a .csv file using pandas
to count players by their nationality
'''

#import the Library
import pandas

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["short_name","age","value_eur","nationality"]]

#Counting the nationalities
nationality_count=fifa_df1["nationality"].value_counts()

print(nationality_count)





#see 6a

#************************************************
#To number of players per nationality, from example 3
#fifa_df2=fifa_df[["nationality"]]
#irish_players=fifa_df2[fifa_df2["nationality"]=="Republic of Ireland"].value_counts()
#print("The number of irish players are:\n ",irish_players)