import pandas as pd
import streamlit as st
import pickle

def recmmend(movie):
    movie = movie.strip()  # Remove extra spaces
    if movie not in movies['title'].values:
        print(f"Movie '{movie}' not found in database.")
        return
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    print(f"\nTop 5 recommendations for '{movie}':")
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommend System')

import streamlit as st

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values,
)

if st.button('Get Movie Recommendations'):
   recommendation =  recmmend(selected_movie_name)
   for i in recommendation:
    st.write(i)

# st.write("You selected:", option)