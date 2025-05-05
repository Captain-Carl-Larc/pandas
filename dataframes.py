import pandas as pd
# Creating a DataFrame from a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'London'},
    {'Name': 'Charlie', 'Age': 22, 'City': 'Paris'},
    {'Name': 'David', 'Age': 28, 'City': 'Tokyo'}
]
df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a dictionary of Series
d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([4, 5, 6, 7], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
print(df)