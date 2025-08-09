import pandas as pd
import ast


movies = pd.read_csv('data/tmdb_5000_movies.csv')
credits = pd.read_csv('data/tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title', how='left')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]


movies.dropna(inplace=True)

print(movies.isnull().sum())

def convert(obj):
    L= []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(lambda x: ast.literal_eval(x)[:3] if isinstance(x, str) else [])

def fetch_director(obj):
    L = []

    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
             L.append(i['name'])
             break
       
       
    return L
movies['crew'] = movies['crew'].apply(fetch_director)

movies['overview']=movies['overview'].apply(lambda x:x.split())

# print(movies['overview'])

movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ","") for i in x])
movies['kaywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])


movies['tags'] = movies['overview'] + movies['genres'] + movies['kaywords'] + movies['cast'] + movies['crew']

new_df = movies[['movie_id','title','tags']]

new_df.head()