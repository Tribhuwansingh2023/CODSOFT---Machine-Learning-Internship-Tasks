import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import random 
movies = pd.DataFrame({
    'MovieID': range(1, 16), 
    'Title': [
        'The Shawshank Redemption', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump', 'Inception',
        'The Lord of the Rings: The Return of the King', 'The Matrix', 'Fight Club', 'Goodfellas', 'The Silence of the Lambs',
        'Saving Private Ryan', 'Seven', 'City of God', 'Spirited Away', 'Life Is Beautiful'
    ],
    'Genre': [
        'Drama', 'Action, Crime, Drama', 'Crime, Drama', 'Drama, Romance', 'Action, Sci-Fi, Thriller',
        'Adventure, Drama, Fantasy', 'Action, Sci-Fi', 'Drama', 'Crime, Drama', 'Crime, Thriller', 
        'Drama, War', 'Crime, Drama, Mystery', 'Crime, Drama', 'Animation, Adventure, Family', 'Comedy, Drama, Romance'
    ]
})
num_users = 100
ratings = pd.DataFrame({
    'UserID': [random.randint(1, num_users) for _ in range(500)],
    'MovieID': [random.randint(1, len(movies)) for _ in range(500)],
    'Rating': [random.randint(1, 5) for _ in range(500)]
})
def create_user_item_matrix(ratings):
    matrix = ratings.pivot_table(index='UserID', columns='MovieID', values='Rating', fill_value=0)
    return matrix

def recommend_collaborative(user_id, user_item_matrix, num_recommendations=5):
    user_ratings = user_item_matrix.loc[user_id]
    similarities = cosine_similarity(user_item_matrix)
    similar_users_index = similarities[user_id - 1].argsort()[::-1][1:]

    recommended_movies = []
    for similar_user_index in similar_users_index:
        similar_user_id = user_item_matrix.index[similar_user_index]
        for movie_id in user_item_matrix.columns:
            if (user_item_matrix.loc[similar_user_id, movie_id] > 0 and 
                movie_id not in user_ratings.index and 
                len(recommended_movies) < num_recommendations):
                recommended_movies.append(movie_id)
                break 
    return recommended_movies

def recommend_content_based(movie_id, movies, num_recommendations=5):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['Genre'])
    cosine_sim = cosine_similarity(tfidf_matrix)

    movie_index = movies[movies['MovieID'] == movie_id].index[0]
    similar_movies_indices = cosine_sim[movie_index].argsort()[::-1][1:num_recommendations+1]
    recommended_movie_ids = [movies.iloc[i]['MovieID'] for i in similar_movies_indices]
    return recommended_movie_ids

user_item_matrix = create_user_item_matrix(ratings)

user_id = 1 
collab_recs = recommend_collaborative(user_id, user_item_matrix)
print(f"Collaborative Recommendations for User {user_id}: {collab_recs}")

movie_id = 2  
content_recs = recommend_content_based(movie_id, movies)
print(f"Content-Based Recommendations for Movie {movie_id}: {content_recs}") 