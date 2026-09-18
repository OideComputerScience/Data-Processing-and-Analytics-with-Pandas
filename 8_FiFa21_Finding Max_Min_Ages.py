'''8
Reading data from a .csv file using pandas
to find the max and min of a DataSet e.g. Irish players
'''
#import the Library
import pandas
#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["short_name","age","value_eur","nationality","league_name"]]

#Finding Max and min of ages
print("The min players age is :", fifa_df1["age"].min())
print("The max players age is :", fifa_df1["age"].max())


print("="*30)

# #Finding max and min of ages of Irish players
# #Filtering by nationality and age
irish_PlayersAges=fifa_df1[(fifa_df1["nationality"]=="Portugal")&(fifa_df1["age"])]

# #Calculating Average
print("The Youngest Irish player's age is :",irish_PlayersAges ["age"].min())
print("The oldeest Irish player's age is :",irish_PlayersAges ["age"].max())

#print(type(irish_PlayersAges))
