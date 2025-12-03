import pandas as pd

df = pd.read_csv('IMDB-Movie-Data.csv')

genre = {}

for i in df['Genre']:
    for j in i.split(','):
        genre[j] = genre.get(j, 0) + 1

print('most populare genre', max(genre, key=lambda x: genre[x]))


movies_about_girls = []
for i in range(len(df)):
    if ('girl' or 'woman' or 'female') in df.iloc[i]['Description']:
        movies_about_girls.append(df.iloc[i]['Title'])

print('movies about girls', movies_about_girls)


#rating
for i in range(len(df)):
    for j in range(len(df)):
        if df.iloc[j]['Metascore'] == i+1:
            print(i+1, df.iloc[i]['Title'])
            break


