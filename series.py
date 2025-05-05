import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# Creating a Series from a list
data  = [1, 3, 5, 6, 8]
s = pd.Series(data)
print(s)

# Creating a Series with a custom index
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)

# Creating a Series from a dictionary
d = {'b': 1, 'a': 0, 'c': 2}
s = pd.Series(d)
print(s)