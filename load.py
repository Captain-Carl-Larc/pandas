import pandas as pd
import numpy as np

# 1. Load the Dataset
# Load the dataset from a CSV file.  You can replace 'your_dataset.csv' with the path to your file.
# For example, you could use a dataset like 'iris.csv' or 'sales_data.csv'.
dataset_path = r"C:\Users\kalwe\Downloads\Video+Game+Sales\vgchartz-2024.csv"  # CHANGE THIS PATH

try:
    df = pd.read_csv(dataset_path)
    print(f"Dataset successfully loaded from {dataset_path}")
except FileNotFoundError:
    print(f"Error: File not found at {dataset_path}.  Please make sure the path is correct and the file exists.")
    #  To make the code runnable, I'll create a dummy DataFrame.  Remove this 'except' block
    #  when you have your actual data file.
    # data = {'A': [1, 2, np.nan, 4, 5], 'B': [6, np.nan, 8, 9, 10], 'C': ['a', 'b', 'c', 'd', 'e']}
    # df = pd.DataFrame(data)
    # print("Using dummy DataFrame instead.")


# 2. Display the First Few Rows
# Display the first 5 rows of the DataFrame
print("\nFirst 5 rows of the dataset:")
print(df.head())

# 3. Explore the Structure of the Dataset
# Get information about the DataFrame (data types, non-null values, etc.)
print("\nDataset information:")
print(df.info())

# Get descriptive statistics for numerical columns
print("\nDescriptive statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 4. Clean the Dataset
# Handle missing values.  You can choose to fill or drop them.
# Option A: Fill missing values with the mean (for numerical columns)
df_filled = df.copy()  # Create a copy to keep the original df unchanged
for col in df_filled.columns:
    if pd.api.types.is_numeric_dtype(df_filled[col]):  # Check if the column is numeric
        df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
print("\nDataFrame with missing values filled with the mean:")
print(df_filled)

# Option B: Drop rows with any missing values
# df_dropped = df.dropna()
# print("\nDataFrame with rows containing missing values dropped:")
# print(df_dropped)

# Option C: Forward fill
# df_ffill = df.ffill()
# print("\nDataFrame with missing values forward filled:")
# print(df_ffill)

#  You can choose ONE of the options (A, B, or C) or comment them out as needed.  For example,
#  if you want to drop missing values, comment out the fillna() part and uncomment the dropna() part.
#  I've shown all 3 options so you can see how they work.
