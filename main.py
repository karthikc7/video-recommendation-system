from src.data_preprocessing import preprocess_liked_posts, preprocess_viewed_posts
from src.recommendation_logic import recommend
import pandas as pd  # Make sure to import pandas for data loading

def main():
    # Load the mock data from CSV files
    processed_viewed_posts = pd.read_csv('viewed_posts.csv')
    processed_liked_posts = pd.read_csv('liked_posts.csv')

    # Check the columns in processed data
    print("Columns in processed_viewed_posts:", processed_viewed_posts.columns)
    print("Columns in processed_liked_posts:", processed_liked_posts.columns)

    # Preprocess the data (you should have preprocessing functions in your preprocessing file)
    processed_viewed_posts = preprocess_viewed_posts(processed_viewed_posts)
    processed_liked_posts = preprocess_liked_posts(processed_liked_posts)

    # Ensure 'views', 'likes', 'rating' are present in preprocessed data
    if 'views' not in processed_viewed_posts.columns or 'likes' not in processed_viewed_posts.columns or 'rating' not in processed_viewed_posts.columns:
        print("Error: Missing required columns in processed_viewed_posts")
        return

    if 'views' not in processed_liked_posts.columns or 'likes' not in processed_liked_posts.columns or 'rating' not in processed_liked_posts.columns:
        print("Error: Missing required columns in processed_liked_posts")
        return

    # Assuming user data is from viewed or liked posts; this is just an example
    user_data = processed_viewed_posts[['views', 'likes', 'rating']].values  # Example user data
    video_metadata = processed_liked_posts[['views', 'likes', 'rating']].values  # Example video metadata

    # Generate recommendations using your chosen method (e.g., collaborative filtering or content-based)
    recommendations = recommend(user_data, video_metadata)

    # Output the recommendations
    print("Recommended videos:", recommendations)

if __name__ == "__main__":
    main()
