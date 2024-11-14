import requests

BASE_URL = "https://api.socialverseapp.com"
FLIC_TOKEN = "flic_1e01009f9c1a54706f385bcc1993a08fd9647ba8f499572d280654d1c03c47bf"
RES_ALGO = "resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"

# Utility function to fetch data from API
def fetch_data(endpoint, params=None):
    headers = {
        "Flic-Token": FLIC_TOKEN
    }
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()  # Return the response JSON if successful
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error occurred: {errh}")  # Not a 200 response
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")  # Any other error (like connection issues)
    return None

# Fetch viewed posts
def get_viewed_posts(page=1, page_size=1000):
    endpoint = f"posts/view?page={page}&page_size={page_size}&resonance_algorithm={RES_ALGO}"
    return fetch_data(endpoint)

# Fetch liked posts
def get_liked_posts(page=1, page_size=5):
    endpoint = f"posts/like?page={page}&page_size={page_size}&resonance_algorithm={RES_ALGO}"
    return fetch_data(endpoint)

# Fetch user ratings
def get_user_ratings(page=1, page_size=5):
    endpoint = f"posts/rating?page={page}&page_size={page_size}&resonance_algorithm={RES_ALGO}"
    return fetch_data(endpoint)

# Fetch all posts
def get_all_posts(page=1, page_size=1000):
    endpoint = f"posts/summary/get?page={page}&page_size={page_size}"
    return fetch_data(endpoint)

# Fetch all users
def get_all_users(page=1, page_size=1000):
    endpoint = f"users/get_all?page={page}&page_size={page_size}"
    return fetch_data(endpoint)
