import pandas as pd
import numpy as np

# 1. Load the Dataset

dataset_path = r"C:\Users\kalwe\Downloads\Video+Game+Sales\vgchartz-2024.csv" 

try:
    df = pd.read_csv(dataset_path)
    print(f"Dataset successfully loaded from {dataset_path}")
except FileNotFoundError:
    print(f"Error: File not found at {dataset_path}.  Please make sure the path is correct and the file exists.")



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
