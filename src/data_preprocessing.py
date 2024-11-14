import pandas as pd
import numpy as np

# Function to preprocess the data
def preprocess_data(data):
    # Convert data into DataFrame for easier manipulation
    df = pd.DataFrame(data)

    # Handle missing values (example: fill with 0s)
    df.fillna(0, inplace=True)

    # Normalize numerical columns (if necessary)
    if 'rating' in df.columns:
        df['rating'] = (df['rating'] - df['rating'].mean()) / df['rating'].std()

    # Example of feature engineering (e.g., creating a new column for engagement)
    if 'likes' in df.columns and 'views' in df.columns:
        df['engagement'] = df['likes'] / (df['views'] + 1)

    return df

# Function to extract relevant data from 'posts'
def extract_post_data(posts):
    post_data = []
    for post in posts:
        post_info = {
            'views': post.get('views', 0),     # Default to 0 if 'views' is not present
            'likes': post.get('likes', 0),     # Default to 0 if 'likes' is not present
            'rating': post.get('rating', 0)    # Default to 0 if 'rating' is not present
        }
        post_data.append(post_info)
    
    return pd.DataFrame(post_data)

# Example of how to preprocess liked posts
def preprocess_viewed_posts(viewed_posts):
    # Assuming the necessary columns are present in the CSV
    viewed_posts.fillna(0, inplace=True)  # Handle missing data if any
    return viewed_posts[['views', 'likes', 'rating']]  # Selecting relevant columns

def preprocess_liked_posts(liked_posts):
    # Same preprocessing logic as for viewed posts
    liked_posts.fillna(0, inplace=True)
    return liked_posts[['views', 'likes', 'rating']]

