from sklearn.metrics.pairwise import cosine_similarity

# Function for content-based filtering
def content_based_recommendation(user_data, video_metadata):
    # Calculate cosine similarity between the user's data and the video metadata
    cosine_sim = cosine_similarity(user_data, video_metadata)
    
    # Get recommendations based on highest similarity score (top 5)
    recommendations = cosine_sim.argsort()[:, -5:]
    
    return recommendations

# Function for collaborative filtering (user-based)
def collaborative_filtering(user_data, all_users_data):
    # Compute similarity matrix using cosine similarity
    similarity_matrix = cosine_similarity(user_data, all_users_data)
    
    # Return the most similar users' recommendations
    return similarity_matrix.argsort()[:, -5:]

# Hybrid recommendation (content + collaborative)
def hybrid_recommendation(user_data, video_metadata, all_users_data):
    content_recommendations = content_based_recommendation(user_data, video_metadata)
    collaborative_recommendations = collaborative_filtering(user_data, all_users_data)
    
    # Combine both recommendations
    hybrid_recommendations = content_recommendations + collaborative_recommendations
    return hybrid_recommendations

# The recommend function can be modified as needed for the appropriate recommendation logic
def recommend(user_data, video_metadata):
    # You can choose between content-based, collaborative, or hybrid recommendations
    return content_based_recommendation(user_data, video_metadata)  # Example of using content-based
