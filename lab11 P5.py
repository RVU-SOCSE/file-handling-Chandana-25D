# NAME:CHANDANA D   USN:1RUA25BCA0016
# Write a Python program to read a CSV file containing years of experience and perform some operations using Pandas.
import pandas as pd

df = pd.read_csv("C:/Users/Chandana D/OneDrive/lab9(2).csv")

# 1. Display the content of the file.
print("File Content:")
print(df)

# 2. Find the total number of rows and columns.
print("\nRows and Columns:")
print(df.shape)

# 3. Calculate the length of the dataframe.
print("\nLength of DataFrame:")
print(len(df))

# 4. Display the first 2 rows only.
print("\nFirst 2 Rows:")
print(df.head(2))
