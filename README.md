🎬 Movie Recommendation System

This project helps users discover movies similar to their favorites. Users can select a movie from a list, and the system provides the top 5 recommended movies along with their posters. The recommendations are made using machine learning techniques to analyze movie features and identify similarities. Visual context is provided using TMDB API, making the interface engaging and intuitive.

The system is developed with Streamlit, offering an interactive, user-friendly experience to explore movie recommendations effortlessly.

📚 Theory of Recommendation Systems
What is a Recommendation System?

A recommendation system is a type of information filtering system that predicts a user's interest in an item. These systems are used in many domains including movie suggestions, online shopping, and content streaming.

🧠 Types of Recommendation Systems
1. Content-Based Filtering

Recommends items similar to what the user liked before, based on item features (like genres, cast, crew, etc.).

2. Collaborative Filtering

Finds users with similar tastes and recommends items liked by those users. It doesn't depend on item features.

3. Hybrid Methods

Combines both content-based and collaborative filtering for more accurate recommendations.

🧮 Cosine Similarity
This project uses cosine similarity to measure how similar two movies are. Each movie is converted into a vector using its features (like genres, keywords, cast, and crew). Cosine similarity then measures the angle between these vectors to determine similarity.

⚙️ How It Works
Dataset

The system uses a combined dataset containing:

Movie Metadata (title, genres, keywords)
Crew Information (cast, director, etc.)
This data is processed and stored in movie_data.pkl and similarity.pkl. Missing or irrelevant values are cleaned using preprocessing techniques like parsing JSON columns with ast.literal_eval.

🏗️ Model
The recommendation engine works by:

Extracting and combining features like genres, keywords, cast, and director.
Converting these features into a single textual representation.
Transforming the text data into vectors using CountVectorizer.
Calculating cosine similarity between all movie vectors.
Recommending top 5 most similar movies based on the similarity score.
🖼️ Poster Integration
Using the TMDB API, the system fetches movie posters for both the selected movie and its recommendations, enriching the interface with visual feedback.

🚀 How to Run
Installation

git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
pip install -r requirements.txt
Running the App

streamlit run app.py
Then open your browser and go to http://localhost:8501.

💡 Usage
Choose a movie from the dropdown list.
Click on "Recommend".
View the top 5 recommended movies with their posters.
✅ Results
The system successfully recommends the top 5 most similar movies based on content features and displays their posters using the TMDB API. This gives users both context and confidence in the recommendations.