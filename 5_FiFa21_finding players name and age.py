'''5
Reading data from a .csv file using pandas
to look at specific columns and finding 
players names over 30- filtering by row and column
'''

#import the Library
import pandas

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")


#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["short_name","age","value_eur","league_name"]]

#Select the rows where age is greater than 30, and from those rows display the short_name and age columns
players_over_30=fifa_df1.loc[(fifa_df1["age"]>30),["short_name","age"]]



print(players_over_30)
