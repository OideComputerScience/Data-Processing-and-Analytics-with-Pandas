'''4
Reading data from a .csv file using pandas
to look at specific columns and finding the
players in the English premiere league over 30
'''

#import the Library
import pandas

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["short_name","age","value_eur","league_name"]]


#Filtering by league and age
premier_league_over30_df=fifa_df1[(fifa_df1["league_name"]=="English Premier League")&(fifa_df1["age"]>30)]
print(premier_league_over30_df)



#print("The averge players age is :", premier_league_over30["age"].mean())