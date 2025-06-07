import pandas as pd

import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Append (Concatenate) the DataFrames

df3 = pd.DataFrame({'A': [9, 10], 'C': [11, 12]})
result = pd.concat([df1, df3], ignore_index=True)
print(result)