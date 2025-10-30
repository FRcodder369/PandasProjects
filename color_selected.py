import pandas as pd

df = pd.read_csv('color_srgb.csv', index_col='Name')

print(df.loc["Red"])
