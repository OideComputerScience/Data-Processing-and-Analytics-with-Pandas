#1 Reading data from a .csv file using pandas
#Ensure the .csv file you are analysing is in the same folder as the pyhton file

#import the pandas library
import pandas

#Read the entire .csv file into a pandas dataframe called fifa_df
fifa_df=pandas.read_csv("players_21.csv")

#This displays the length of the DataFrame
print("Number of rows",len(fifa_df))

#Display the number or rows and columns in the DataFrame
print("Shape (rows,cols)",fifa_df.shape)

#gives you more information about the data set.
print(fifa_df.info())

