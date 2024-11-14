import pandas as pd

# Creating mock data for viewed_posts
viewed_data = {
    'status': ['success', 'success', 'success'],
    'message': ['Video 1 viewed', 'Video 2 viewed', 'Video 3 viewed'],
    'page': [1, 1, 2],
    'page_size': [10, 10, 10],
    'max_page_size': [50, 50, 50],
    'posts': ['Post 1 details', 'Post 2 details', 'Post 3 details'],
    'views': [120, 200, 350],
    'likes': [30, 50, 80],
    'rating': [4.5, 4.7, 4.8]
}

# Creating mock data for liked_posts
liked_data = {
    'status': ['success', 'success', 'success'],
    'message': ['Video 1 liked', 'Video 2 liked', 'Video 3 liked'],
    'page': [1, 1, 2],
    'page_size': [10, 10, 10],
    'max_page_size': [50, 50, 50],
    'posts': ['Post 1 details', 'Post 2 details', 'Post 3 details'],
    'views': [120, 200, 350],
    'likes': [30, 50, 80],
    'rating': [4.5, 4.7, 4.8]
}

# Converting to DataFrame
viewed_df = pd.DataFrame(viewed_data)
liked_df = pd.DataFrame(liked_data)

# Saving to CSV
viewed_df.to_csv('viewed_posts.csv', index=False)
liked_df.to_csv('liked_posts.csv', index=False)

print("Mock data generated and saved as 'viewed_posts.csv' and 'liked_posts.csv'")
