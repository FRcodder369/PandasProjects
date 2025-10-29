import pandas as pd

df_csv = pd.read_csv('superhero.csv')

print(df_csv)


df_json = pd.read_json('employees.json')
print(df_json)