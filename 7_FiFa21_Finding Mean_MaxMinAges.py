'''7
Reading data from a .csv file using pandas
to find the mean and median age of players
'''

#import the Library
import pandas

#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Selecting a number of columns with all their rows
fifa_df1=fifa_df[["short_name","age","value_eur","nationality","league_name"]]

#Remove rows with missing age or value. subset checks subset of column
#Only rows where column 'age' and 'wage_eur' is NaN are dropped.
fifa_df1 = fifa_df.dropna(subset=["short_name","age","value_eur","nationality","league_name"])

#Finding mean of ages
print("The averge players wage is :", fifa_df1["value_eur"].mean())

print("The averge players wage to 2 dp is %s euros:" %str(round(fifa_df1["value_eur"].mean(),2)))

# What is the median age and wage of a player?
print("Median age/wage:\n", fifa_df1[['age', 'value_eur']].median())

print("="*30)


# #Finding mean of ages of Irish players
# #Filtering by nationality and age
irish_PlayersAges=fifa_df1[(fifa_df1["nationality"]=="Republic of Ireland")&(fifa_df1["age"])]
#print(irish_PlayersAges)

#Calculating Average age of Irish players
print("The average Irish player's age is :",irish_PlayersAges ["age"].mean())