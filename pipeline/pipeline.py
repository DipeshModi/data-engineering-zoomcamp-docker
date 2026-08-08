import sys

import pandas as pd

print('arguments:', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"Day": [1, 2], "No. of passengers": [3,4]})
df["Month"] = month
print(df.head())

df.to_parquet(f"data_{month}.parquet")

print(f'hello pipeline for month {month}')