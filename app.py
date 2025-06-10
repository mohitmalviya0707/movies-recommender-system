#
#
# import pickle
# import streamlit as st
# import requests
#
# # TMDB API Key
# API_KEY = "cb75e7c6aad1a1f40d91822a76a147e8"
#
# # Load data
# movies = pickle.load(open('movies.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # Fetch poster
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     data = requests.get(url).json()
#     poster_path = data.get('poster_path')
#     return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""
#
# # Fetch detailed info
# def fetch_movie_details(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=videos,credits"
#     return requests.get(url).json()
#
# # Recommend logic
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
#     names, posters, ids = [], [], []
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         ids.append(movie_id)
#         posters.append(fetch_poster(movie_id))
#         names.append(movies.iloc[i[0]].title)
#     return names, posters, ids
#
# # Streamlit Config
# st.set_page_config(page_title="Movie Recommender", layout="wide")
#
# # CSS Styling
# st.markdown("""
# <style>
# body {
#     background-color: #1e1e1e;
# }
# h1 {
#     color: #0ef;
#     text-align: center;
#     font-size: 3rem;
#     font-weight: 900;
# }
# .poster-container {
#     border-radius: 15px;
#     overflow: hidden;
#     box-shadow: 0 0 10px rgba(0, 238, 255, 0.3);
#     cursor: default;
#     text-align: center;
#     margin-bottom: 10px;
# }
# .poster-container:hover {
#     transform: scale(1.05);
#     box-shadow: 0 0 20px rgba(0, 238, 255, 0.6);
# }
# .poster-img {
#     width: 100%;
#     height: 300px;
#     object-fit: cover;
#     border-radius: 15px;
# }
# .movie-title {
#     color: white;
#     font-size: 1rem;
#     margin-top: 8px;
#     font-weight: bold;
# }
# .stButton>button {
#     background-color: #0ef;
#     color: black;
#     font-weight: bold;
#     border: none;
#     padding: 0.5em 1em;
#     border-radius: 10px;
#     box-shadow: 0 0 10px rgba(0, 238, 255, 0.6);
# }
# .stButton>button:hover {
#     transform: scale(1.05);
#     box-shadow: 0 0 20px rgba(0, 238, 255, 1);
# }
# .details-box {
#     background-color: #111;
#     border-radius: 15px;
#     padding: 20px;
#     color: white;
#     box-shadow: 0 0 15px rgba(0, 238, 255, 0.3);
# }
# </style>
# """, unsafe_allow_html=True)
#
# # App Title
# st.markdown("<h1>🎬 Minimalist Movie Recommender</h1>", unsafe_allow_html=True)
#
# # Session state
# if 'clicked_movie_id' not in st.session_state:
#     st.session_state.clicked_movie_id = None
# if 'recommendations' not in st.session_state:
#     st.session_state.recommendations = None
#
# # Selectbox
# selected_movie = st.selectbox("🔍 Choose a movie you like", movies['title'].values)
#
# # Button to show recommendations
# if st.button("🎥 Show Recommendations"):
#     st.session_state.clicked_movie_id = None
#     st.session_state.recommendations = recommend(selected_movie)
#
# # Show recommended posters
# if st.session_state.recommendations and not st.session_state.clicked_movie_id:
#     names, posters, ids = st.session_state.recommendations
#     st.markdown("### Recommended for You:")
#     cols = st.columns(5)
#     for i in range(5):
#         with cols[i]:
#             st.markdown(f"""
#                 <div class="poster-container">
#                     <img src="{posters[i]}" class="poster-img" alt="{names[i]}" />
#                     <div class="movie-title">{names[i]}</div>
#                 </div>
#             """, unsafe_allow_html=True)
#             with st.form(key=f"form_{i}"):
#                 submitted = st.form_submit_button("ℹ️ More Info", use_container_width=True)
#                 if submitted:
#                     st.session_state.clicked_movie_id = ids[i]
#                     st.rerun()
#
# # Show movie detail
# if st.session_state.clicked_movie_id:
#     details = fetch_movie_details(st.session_state.clicked_movie_id)
#     st.markdown("---")
#     st.markdown(f"<div class='details-box'>", unsafe_allow_html=True)
#     st.markdown(f"## 🎥 {details.get('title')} ({details.get('release_date', '')[:4]})")
#     cols = st.columns([1, 2])
#     with cols[0]:
#         st.image(fetch_poster(st.session_state.clicked_movie_id), width=300)
#     with cols[1]:
#         st.markdown(f"**📅 Release Date:** {details.get('release_date')}")
#         st.markdown(f"**⭐ Rating:** {details.get('vote_average')} / 10")
#         st.markdown(f"**🗣️ Language:** {details.get('original_language', '').upper()}")
#         genres = ", ".join([g['name'] for g in details.get('genres', [])])
#         st.markdown(f"**🎭 Genres:** {genres}")
#         crew = details.get('credits', {}).get('crew', [])
#         director = next((p['name'] for p in crew if p['job'] == 'Director'), 'N/A')
#         st.markdown(f"**🎬 Director:** {director}")
#         cast = details.get('credits', {}).get('cast', [])[:5]
#         cast_names = ", ".join([actor['name'] for actor in cast])
#         st.markdown(f"**🧑‍🤝‍🧑 Cast:** {cast_names}")
#         st.markdown(f"**📝 Overview:** {details.get('overview')}")
#         trailer = next((vid for vid in details.get('videos', {}).get('results', []) if vid['type'] == 'Trailer' and vid['site'] == 'YouTube'), None)
#         if trailer:
#             st.markdown(f"[▶️ Watch Trailer](https://www.youtube.com/watch?v={trailer['key']})")
#     st.markdown("</div>", unsafe_allow_html=True)
#
#     # Back button
#     if st.button("🔙 Back to Recommendations"):
#         st.session_state.clicked_movie_id = None
#         st.rerun()




import os
import pickle
import streamlit as st
import requests
import gdown

# Google Drive links
MOVIES_URL = "https://drive.google.com/uc?id=1BT4c0seOYKsESyvLH6nJK1NxAc--EAd8"
SIMILARITY_URL = "https://drive.google.com/uc?id=1FzQeQAH1XpKQU2zQk0ZxplZygZJ6NA1d"

# Download if not present
if not os.path.exists("movies.pkl"):
    gdown.download(MOVIES_URL, "movies.pkl", quiet=False)

if not os.path.exists("similarity.pkl"):
    gdown.download(SIMILARITY_URL, "similarity.pkl", quiet=False)

# Load files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# TMDB API
API_KEY = "cb75e7c6aad1a1f40d91822a76a147e8"

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US&append_to_response=videos,credits"
    return requests.get(url).json()

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    names, posters, ids = [], [], []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        ids.append(movie_id)
        posters.append(fetch_poster(movie_id))
        names.append(movies.iloc[i[0]].title)
    return names, posters, ids

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Styling
st.markdown("""
<style>
body {
    background-color: #1e1e1e;
}
h1 {
    color: #0ef;
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
}
.poster-container {
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 0 10px rgba(0, 238, 255, 0.3);
    cursor: default;
    text-align: center;
    margin-bottom: 10px;
}
.poster-container:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(0, 238, 255, 0.6);
}
.poster-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 15px;
}
.movie-title {
    color: white;
    font-size: 1rem;
    margin-top: 8px;
    font-weight: bold;
}
.stButton>button {
    background-color: #0ef;
    color: black;
    font-weight: bold;
    border: none;
    padding: 0.5em 1em;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 238, 255, 0.6);
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(0, 238, 255, 1);
}
.details-box {
    background-color: #111;
    border-radius: 15px;
    padding: 20px;
    color: white;
    box-shadow: 0 0 15px rgba(0, 238, 255, 0.3);
}
</style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1>🎬 Minimalist Movie Recommender</h1>", unsafe_allow_html=True)

# Session
if 'clicked_movie_id' not in st.session_state:
    st.session_state.clicked_movie_id = None
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

# Selectbox
selected_movie = st.selectbox("🔍 Choose a movie you like", movies['title'].values)

if st.button("🎥 Show Recommendations"):
    st.session_state.clicked_movie_id = None
    st.session_state.recommendations = recommend(selected_movie)

# Posters
if st.session_state.recommendations and not st.session_state.clicked_movie_id:
    names, posters, ids = st.session_state.recommendations
    st.markdown("### Recommended for You:")
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"""
                <div class="poster-container">
                    <img src="{posters[i]}" class="poster-img" alt="{names[i]}" />
                    <div class="movie-title">{names[i]}</div>
                </div>
            """, unsafe_allow_html=True)
            with st.form(key=f"form_{i}"):
                submitted = st.form_submit_button("ℹ️ More Info", use_container_width=True)
                if submitted:
                    st.session_state.clicked_movie_id = ids[i]
                    st.rerun()

# Details
if st.session_state.clicked_movie_id:
    details = fetch_movie_details(st.session_state.clicked_movie_id)
    st.markdown("---")
    st.markdown(f"<div class='details-box'>", unsafe_allow_html=True)
    st.markdown(f"## 🎥 {details.get('title')} ({details.get('release_date', '')[:4]})")
    cols = st.columns([1, 2])
    with cols[0]:
        st.image(fetch_poster(st.session_state.clicked_movie_id), width=300)
    with cols[1]:
        st.markdown(f"**📅 Release Date:** {details.get('release_date')}")
        st.markdown(f"**⭐ Rating:** {details.get('vote_average')} / 10")
        st.markdown(f"**🗣️ Language:** {details.get('original_language', '').upper()}")
        genres = ", ".join([g['name'] for g in details.get('genres', [])])
        st.markdown(f"**🎭 Genres:** {genres}")
        crew = details.get('credits', {}).get('crew', [])
        director = next((p['name'] for p in crew if p['job'] == 'Director'), 'N/A')
        st.markdown(f"**🎬 Director:** {director}")
        cast = details.get('credits', {}).get('cast', [])[:5]
        cast_names = ", ".join([actor['name'] for actor in cast])
        st.markdown(f"**🧑‍🤝‍🧑 Cast:** {cast_names}")
        st.markdown(f"**📝 Overview:** {details.get('overview')}")
        trailer = next((vid for vid in details.get('videos', {}).get('results', []) if vid['type'] == 'Trailer' and vid['site'] == 'YouTube'), None)
        if trailer:
            st.markdown(f"[▶️ Watch Trailer](https://www.youtube.com/watch?v={trailer['key']})")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔙 Back to Recommendations"):
        st.session_state.clicked_movie_id = None
        st.rerun()
