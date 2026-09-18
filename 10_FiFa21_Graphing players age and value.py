# 10 Plotting palyers age against their wage


#import the Libraries
import pandas
import matplotlib.pyplot as plt

# Read the entire CSV file into a pandas DataFrame
fifa_df = pandas.read_csv('players_21.csv')

#Remove rows with missing age or value. subset checks subset of column
#Only rows where column 'age' and 'wage_eur' is NaN are dropped.
fifa_df = fifa_df.dropna(subset=['age', 'value_eur'])


# Filter out the column, value_eur
player_values = fifa_df['value_eur']
player_ages = fifa_df['age']

plt.plot(player_ages, player_values)
plt.show()
