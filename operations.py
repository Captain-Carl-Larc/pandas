import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 28, 24],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'London'],
    'Salary': [50000, 60000, 45000, 70000, 55000]
}
df = pd.DataFrame(data)
# print(df)

# Display the first 5 rows
# print(df.head(2))

# display last 3
# print(df)
# print(df.tail(3))

# Get information about the DataFrame (data types, non-null values, etc.)
# print(df.info())

# Get descriptive statistics (mean, std, min, max, etc.) for numerical columns
# print(df.describe())

# Get the shape of the DataFrame (number of rows and columns)
# print(df.shape)

# Get the column names
# print(df.columns)

# Get the index
# print(df.index)

# Select a single column
namesOpt = df['Name']
names = df.Name  # syntax : dfName.NameOfColumn
# print(names)

# Select multiple columns
subset_df = df[['Name', 'Age']]
# print(subset_df)

# Select a single row by index
row_0 = df.loc[0]
# print(row_0)

# Select a row by integer position
row_1 = df.iloc[1]
# print(row_1)

# Select a specific value
age_of_bob = df.loc[1, 'Age']
# print(age_of_bob) #30

# Select a subset of rows and columns
subset_df = df.loc[0:2, ['Name', 'Age']]
# print(subset_df)

# Select rows based on a condition
adults = df[df['Age'] >= 25]
# print(adults)

# Select rows based on multiple conditions
london_residents = df[(df['City'] == 'London') & (df['Age'] < 30)]
print(london_residents)