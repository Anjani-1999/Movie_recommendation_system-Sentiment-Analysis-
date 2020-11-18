import pandas as pd
import numpy as np


link = "https://en.wikipedia.org/wiki/List_of_American_films_of_2018"
df1 = pd.read_html(link, header=0)[2]
df2 = pd.read_html(link, header=0)[3]
df3 = pd.read_html(link, header=0)[4]
df4 = pd.read_html(link, header=0)[5]

df = df1.append(df2.append(df3.append(df4,ignore_index=True),ignore_index=True),ignore_index=True)

from tmdbv3api import TMDb
import json
import requests
tmdb = TMDb()
tmdb.api_key = 'b69875a7edf46e3010a6ca14f5b6ed0e'


from tmdbv3api import Movie
tmdb_movie = Movie()
def get_genre(x):
    genres = []
    result = tmdb_movie.search(x)
    movie_id = result[0].id
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
    data_json = response.json()
    if data_json['genres']:
        genre_str = " "
        for i in range(0,len(data_json['genres'])):
            genres.append(data_json['genres'][i]['name'])
        return genre_str.join(genres)
    else:
        np.NaN


df['genres'] = df['Title'].map(lambda x: get_genre(str(x)))
print(df)

df_2018 = df[['Title','Cast and crew','genres']]
print(df_2018)

def get_director(x):
    if " (director)" in x:
        return x.split(" (director)")[0]
    elif " (directors)" in x:
        return x.split(" (directors)")[0]
    else:
        return x.split(" (director/screenplay)")[0]
    
    
df_2018['director_name'] = df_2018['Cast and crew'].map(lambda x: get_director(x))



def get_actor1(x):
    return ((x.split("screenplay); ")[-1]).split(", ")[0])
df_2018['actor_1_name'] = df_2018['Cast and crew'].map(lambda x: get_actor1(x))

def get_actor2(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 2:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[1])

df_2018['actor_2_name'] = df_2018['Cast and crew'].map(lambda x: get_actor2(x))


df_2018['actor_2_name'] = df_2018['Cast and crew'].map(lambda x: get_actor2(x))
def get_actor3(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 3:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[2])

df_2018['actor_3_name'] = df_2018['Cast and crew'].map(lambda x: get_actor3(x))
print(df_2018)

df_2018 = df_2018.rename(columns={'Title':'movie_title'})

new_df18 = df_2018.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]

print(new_df18)


new_df18['actor_2_name'] = new_df18['actor_2_name'].replace(np.nan, 'unknown')
new_df18['actor_3_name'] = new_df18['actor_3_name'].replace(np.nan, 'unknown')


new_df18['movie_title'] = new_df18['movie_title'].str.lower()

new_df18['comb'] = new_df18['actor_1_name'] + ' ' + new_df18['actor_2_name'] + ' '+ new_df18['actor_3_name'] + ' '+ new_df18['director_name'] +' ' + new_df18['genres']

print(new_df18)


link = "https://en.wikipedia.org/wiki/List_of_American_films_of_2019"
df1 = pd.read_html(link, header=0)[3]
df2 = pd.read_html(link, header=0)[4]
df3 = pd.read_html(link, header=0)[5]
df4 = pd.read_html(link, header=0)[6]


df = df1.append(df2.append(df3.append(df4,ignore_index=True),ignore_index=True),ignore_index=True)
print(df)

df['genres'] = df['Title'].map(lambda x: get_genre(str(x)))

df_2019 = df[['Title','Cast and crew','genres']]


print(df_2019)


def get_director(x):
    if " (director)" in x:
        return x.split(" (director)")[0]
    elif " (directors)" in x:
        return x.split(" (directors)")[0]
    else:
        return x.split(" (director/screenplay)")[0]



df_2019['director_name'] = df_2019['Cast and crew'].map(lambda x: get_director(str(x)))
def get_actor1(x):
    return ((x.split("screenplay); ")[-1]).split(", ")[0])

df_2019['actor_1_name'] = df_2019['Cast and crew'].map(lambda x: get_actor1(x))


def get_actor2(x):

    if len((x.split("screenplay); ")[-1]).split(", ")) < 2:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[1])
df_2019['actor_2_name'] = df_2019['Cast and crew'].map(lambda x: get_actor2(x))

def get_actor3(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 3:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[2])

df_2019['actor_3_name'] = df_2019['Cast and crew'].map(lambda x: get_actor3(x))
df_2019 = df_2019.rename(columns={'Title':'movie_title'})
new_df19 = df_2019.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]
new_df19['actor_2_name'] = new_df19['actor_2_name'].replace(np.nan, 'unknown')
new_df19['actor_3_name'] = new_df19['actor_3_name'].replace(np.nan, 'unknown')
new_df19['movie_title'] = new_df19['movie_title'].str.lower()
new_df19['comb'] = new_df19['actor_1_name'] + ' ' + new_df19['actor_2_name'] + ' '+ new_df19['actor_3_name'] + ' '+ new_df19['director_name'] +' ' + new_df19['genres']
print(new_df19)


my_df = new_df18.append(new_df19,ignore_index=True)
print(my_df)

old_df = pd.read_csv('new_data.csv')
print(old_df)
final_df = old_df.append(my_df,ignore_index=True)
print(final_df)


print(final_df.isna().sum())
final_df = final_df.dropna(how='any')
print(final_df.isna().sum())
final_df.isna().sum()

final_df.to_csv('final_data.csv',index=False)

