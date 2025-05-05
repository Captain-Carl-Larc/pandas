import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 28, 24],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'London']
    
}
df = pd.DataFrame(data)

# Add a new column
df['Salary'] = [50000, 60000, 45000, 70000, 55000]
# print(df.head())

# Add a new column based on existing columns
df['SalaryIncrease'] = df['Salary'] * 0.1
# print(df.head())

# Add a new column with a default value
df['Bonus'] = 1000
print(df.head())