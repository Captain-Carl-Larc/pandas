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
print(df.describe())