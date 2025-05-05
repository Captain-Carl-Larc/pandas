import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 28, 24],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'London'],
    'Salary': [50000, 60000, 45000, 70000, 55000]
}
df = pd.DataFrame(data)
print(df)