'''Creating a data processor module 
for handling data transformations
This file contains files that do:
     cleaning,  
     loading, 
     extracting
     transforming data
'''
import pandas as pd #pd is an alias/nickname of pandas library
import glob #glob module finds all the pathnames matching a specified pattern

#1 Extract:Load all csv files from a directory 
csv_files = glob.glob('data/*.csv') #get all csv files in the data directory

# list to hold dataframes
dfs = []

for filename in csv_files:
    # Read each csv file into a dataframe
    df = pd.read_csv(filename)
    dfs.append(df) #append each dataframe to the list

# Combine all regions into one big table
data = pd.concat(dfs,ignore_index=True)

#2 Transform: Clean the data
#Filter columns as we only need pink morsel
#Compare lower case column names to avoid case sensitivity issues
data = data[data['product'].str.lower() == 'pink morsel']

#Fix price column: remove $ sign and convert to float
data['price'] = data['price'].str.replace('$','')#remove $ sign
data['price'] = data['price'].astype(float) #convert to float

#Ensure quantity is integer
data['quantity']=data['quantity'].astype(int)

#Create column for sales
data['sales']=data['quantity'] * data['price']

#Fix data to ensure its a date column not text
data['date']=pd.to_datetime(data['date'])

#Select relevant columns
cleaned_data = data[['sales','date','region',]]

#Sort data by date
cleaned_data = cleaned_data.sort_values(by='date')

#3 Load: Save to a new file
cleaned_data.to_csv('formatted_data.csv',index=False)
print("Data processing complete. Cleaned data saved to 'formatted_data.csv'.")