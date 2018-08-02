# Manage dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For web scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

# Get html
# url = "http://www.hubertiming.com/results/2017GPTR10K"
url = 'https://en.wikipedia.org/wiki/List_of_NASA_missions'
html = urlopen(url) # retrieves the html and stores it in a variable

# Create beautiful soup object
soup = BeautifulSoup(html, 'lxml') # The object to be created and its html parser

# Retrieve all the tabular data
rows = soup.find_all('tr')
list_rows = [] # Define empty array
for row in rows:
    row_td = row.find_all('td') # Iterate through the table for <td> tags
    str_cells = str(row_td) # Convert to string format
    cleantext = BeautifulSoup(str_cells, 'lxml').get_text() # Retrieve the text from the table entries
    print(cleantext) # Sanity check
    list_rows.append(cleantext) # Upload all strings to the empty array. 


# Convert the list into a dataframe
df_racedata = pd.DataFrame(list_rows) # Create a dataframe from list_rows
def format(df): # Define a function for formatting dataframes
    df = df[0].str.split(',', expand = True) # Split at commas
    df[0] = df[0].str.strip('[') # Remove opening brackets
    df[13] = df[13].str.strip(']') # Remove closing brackets
    df[1] = df[1].str.strip(']') # Remove closing brackets
    return df
df_racedata = format(df_racedata) # Call the function on the race dataframe
print(df_racedata.head(10)) # Sanity check

# Find some headers
col_labels = soup.find_all('th') # Find headers
all_header = [] # Initialize array
col_str = str(col_labels) # Convert to strings
cleantext2 = BeautifulSoup(col_str, 'lxml').get_text() # Remove tags
all_header.append(cleantext2) # Append to empty array
print(all_header) # Sanity check
df_header = pd.DataFrame(all_header) # Convert to dataframe
df_header = format(df_header) # Format the header dataframe
frames = [df_header, df_racedata] # Define an array of dataframe variables
df_concat = pd.concat(frames) # Concatenate the frames
df_final = df_concat.rename(columns=df_concat.iloc[0]) # Name columns after first row
df_final = df_final.dropna(axis=0, how='any') # Drop empty rows
df_final = df_final.drop(df_final.index[0]) # Drop the first row which duplicates column titles
print(df_final.head(10)) # Check the result

# Data analysis and visualization






