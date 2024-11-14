import pandas as pd
import numpy as np

# Mock data (replace with actual data fetching logic)
# Sample DataFrames for illustration; you should replace these with your actual data fetch logic.
viewed_posts = pd.DataFrame({
    'video_id': [1, 2, 3],
    'views': [100, 150, 50],
    'likes': [10, 15, 5],
    'rating': [5, 4, 3]
})

posts = pd.DataFrame({
    'video_id': [1, 2, 3, 4, 5],
    'views': [100, 150, 50, 200, 250],
    'likes': [10, 15, 5, 20, 25],
    'rating': [5, 4, 3, 2, 1]
})

user_ratings = pd.DataFrame({
    'video_id': [1, 2, 3],
    'rating': [5, 4, 3]
})

# Function to handle cold start problem (when user data is empty)
def handle_cold_start(user_data, posts):
    if isinstance(user_data, pd.DataFrame) and user_data.empty:
        # Check if posts DataFrame has valid data
        posts_sorted = posts[posts['views'] > 0].sort_values(by=['views', 'likes'], ascending=False)
        return posts_sorted[['video_id', 'views', 'likes', 'rating']].head(5)
    return posts[['video_id', 'views', 'likes', 'rating']]  # Default return for non-cold-start

# Content-based recommendation function (simple example)
def content_based_recommendation(user_data, video_metadata):
    content_scores = video_metadata.copy()
    content_scores['content_score'] = content_scores['views'] * 0.5 + content_scores['likes'] * 0.5
    return content_scores[['video_id', 'content_score']]

# Collaborative filtering function (simple example)
def collaborative_filtering(user_ratings):
    collaborative_scores = user_ratings.copy()
    collaborative_scores['collaborative_score'] = collaborative_scores['rating'] * 1  # Weight ratings
    return collaborative_scores[['video_id', 'collaborative_score']]

# Hybrid recommendation function (simple weighted average)
def hybrid_recommendation(content_scores, collaborative_scores):
    merged_scores = pd.merge(content_scores, collaborative_scores, on='video_id')
    merged_scores['hybrid_score'] = 0.5 * merged_scores['content_score'] + 0.5 * merged_scores['collaborative_score']
    return merged_scores[['video_id', 'hybrid_score']]

# MAP score calculation function
def calculate_map(true_relevance, predicted_relevance):
    # Rank-based MAP: Compare rank positions
    ranked_true_relevance = true_relevance.argsort()[::-1]  # Sorting true relevance in descending order
    ranked_predicted_relevance = predicted_relevance.argsort()[::-1]  # Sorting predicted relevance

    ap = 0
    for i, true_idx in enumerate(ranked_true_relevance):
        if true_idx in ranked_predicted_relevance[:i+1]:  # Check if true relevance appears in top 'i' predictions
            ap += 1
    return ap / len(true_relevance) if len(true_relevance) > 0 else 0


# Main recommendation system function
def run_recommendation_system():
    # Print out the fetched data for debugging purposes
    print("Fetched Data:")
    print(viewed_posts.head())  # Check the first few rows of viewed_posts
    print(posts.head())  # Check the first few rows of posts
    print(user_ratings.head())  # Check the first few rows of user_ratings

    # Assuming 'viewed_posts' and 'posts' are valid dataframes
    user_data = viewed_posts[['video_id', 'views', 'likes', 'rating']]  # Adjusted columns
    video_metadata = posts[['video_id', 'views', 'likes', 'rating']]  # Adjusted columns

    # Generate Content-Based Recommendations
    content_scores = content_based_recommendation(user_data, video_metadata)

    # Collaborative Filtering
    collaborative_scores = collaborative_filtering(user_ratings)

    # Hybrid Recommendations
    hybrid_scores = hybrid_recommendation(content_scores, collaborative_scores)

    # Handle Cold Start Problem (Fixing the Empty Dictionary Issue)
    new_user_data = pd.DataFrame(columns=['video_id', 'views', 'likes', 'rating'])  # Empty DataFrame for new user
    cold_start_recommendations = handle_cold_start(new_user_data, posts)

    # Ensure true and predicted relevance are properly aligned
    true_relevance = user_ratings['rating'].fillna(0)[:len(hybrid_scores)]  # Fill NaN with 0 for true relevance
    predicted_relevance = hybrid_scores['hybrid_score'].values[:len(true_relevance)]  # Corrected to .values

    # Debugging step to check if the MAP calculation is working
    print("True Relevance:")
    print(true_relevance.head())
    print("Predicted Relevance:")
    print(pd.Series(predicted_relevance[:len(true_relevance)]).head())

    # Calculate MAP
    map_score = calculate_map(true_relevance, predicted_relevance)

    print(f"MAP Score: {map_score}")
    print(f"Cold Start Recommendations: {cold_start_recommendations}")

# Run the Recommendation System
if __name__ == "__main__":
    run_recommendation_system()
