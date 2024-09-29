import pandas as pd  
from sklearn.metrics.pairwise import cosine_similarity  

# Sample data (replace this with your actual data)  
movies = pd.DataFrame({  
    'MovieID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E', 'Movie F', 'Movie G', 'Movie H', 'Movie I', 'Movie J'],  
    'Genre': ['Action', 'Comedy', 'Drama', 'Action', 'Comedy', 'Drama', 'Comedy', 'Action', 'Drama', 'Action'],  
})  

ratings = pd.DataFrame({  
    'UserID': [1, 1, 1, 2, 2, 2, 3, 3, 3, 3],  
    'MovieID': [1, 3, 5, 2, 4, 6, 1, 7, 9, 10],  
    'Rating': [5, 4, 3, 4, 5, 2, 3, 5, 4, 1]  
})  

# Function to create a user-item matrix  
def create_user_item_matrix(ratings):  
    matrix = ratings.pivot_table(index='UserID', columns='MovieID', values='Rating', fill_value=0)  
    return matrix  

# Function to recommend based on collaborative filtering (cosine similarity)  
def recommend_collaborative(user_id, user_item_matrix, num_recommendations=3):  
    user_ratings = user_item_matrix.loc[user_id]  
    similarities = cosine_similarity(user_item_matrix)  
    similar_users_index = similarities[user_id - 1]  # Accessing the corresponding user row  
    
    similar_users = similar_users_index.argsort()[::-1][1:]  # Get indices of most similar users, excluding the user itself  

    recommended_movies = []  
    for similar_user_index in similar_users:  
        similar_user_id = user_item_matrix.index[similar_user_index]  # Get the actual UserID  
        for movie_id in user_item_matrix.columns:  
            if user_item_matrix.loc[similar_user_id, movie_id] > 0 and movie_id not in user_ratings.index and len(recommended_movies) < num_recommendations:  
                recommended_movies.append(movie_id)  
                break  

    return recommended_movies  

# Function to recommend based on content-based filtering (genre similarity)  
def recommend_content_based(movie_id, movies, num_recommendations=3):  
    target_movie = movies[movies['MovieID'] == movie_id]  
    genre = target_movie['Genre'].iloc[0]  
    similar_movies = movies[movies['Genre'] == genre]  

    recommended_movies = similar_movies.sample(n=num_recommendations)['MovieID'].tolist()  
    return recommended_movies  

# Example usage  
user_item_matrix = create_user_item_matrix(ratings)  

# Collaborative filtering recommendations  
user_id = 1  # Replace with actual user ID  
recommendations = recommend_collaborative(user_id, user_item_matrix)  
print(f"Collaborative filtering recommendations for user {user_id}: {recommendations}")  

# Content-based filtering recommendations  
movie_id = 2  # Replace with actual movie ID  
recommendations = recommend_content_based(movie_id, movies)  
print(f"Content-based recommendations for movie {movie_id}: {recommendations}")