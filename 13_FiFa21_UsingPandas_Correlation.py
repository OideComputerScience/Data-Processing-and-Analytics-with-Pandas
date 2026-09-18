'''13
Reading data from a .csv file using pandas
and demostrating corr method

This code computes the correlation coefficient between age
and palyer's values in eurs, a result between -1 and +1 that measures
the strength and direction of their linear relationship.
+1 indicates a perfect positive correlation, -1 a perfect
negative and 0 means no linear correlation.

'''
#import the Libraries
import pandas
import matplotlib.pyplot as plt


#Read the entire .csv file into a pandas Dataframe
fifa_df=pandas.read_csv("players_21.csv")

#Remove rows with missing age or value. subset checks subset of column
#Only rows where column 'age' and 'wage_eur' is NaN are dropped.
fifa_df = fifa_df.dropna(subset=['age', 'value_eur'])


# Filter out the column, value_eur
player_values = fifa_df['value_eur']
player_ages = fifa_df['age']

plt.plot(player_ages, player_values)
plt.title("Value of player according to their age")
plt.xlabel("Player's Age (Years)")
plt.ylabel("Player's Value (Euros)")
plt.show()

#Calculate Correlation Between Two series
correlation = fifa_df['age'].corr(fifa_df['value_eur'])

print("The correlation between a players age and the value is: ",round(correlation,3))




