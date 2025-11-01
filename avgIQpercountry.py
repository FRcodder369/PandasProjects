import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

print('countries with the IQ of more than 100')
print(df[df['Average IQ'] >= 100].to_string())