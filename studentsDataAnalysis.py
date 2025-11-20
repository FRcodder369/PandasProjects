import pandas as pd

df = pd.read_csv('cdvfile.csv', index_col='Name')

max_score = max(df['Score'])

average = sum(df['Score'])/len(df)

print(f'best score: {max_score} belonges to {df[df['Score'] == max_score].index[0]}')
print(f'average score of class: { average :.2f}')

print('students with grade more than average:')
print(df[df['Score'] > average])