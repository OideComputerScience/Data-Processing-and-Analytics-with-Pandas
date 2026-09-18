'''
6a
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
nationality_count=fifa_df1.loc[(fifa_df1["nationality"]=="Republic of Ireland"),["nationality"]]

print(nationality_count.value_counts())


