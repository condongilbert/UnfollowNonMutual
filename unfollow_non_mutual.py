import requests

# Replace with your GitHub username and personal access token
GITHUB_USERNAME = "your_username"
TOKEN = "your_personal_access_token"

# GitHub API base URL
BASE_URL = "https://api.github.com"

# Headers for authentication
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_following():
    """Get a list of users you are following."""
    url = f"{BASE_URL}/users/{GITHUB_USERNAME}/following"
    response = requests.get(url, headers=HEADERS)
    return {user['login'] for user in response.json()} if response.status_code == 200 else set()

def get_followers():
    """Get a list of users following you."""
    url = f"{BASE_URL}/users/{GITHUB_USERNAME}/followers"
    response = requests.get(url, headers=HEADERS)
    return {user['login'] for user in response.json()} if response.status_code == 200 else set()

def unfollow_users(users_to_unfollow):
    """Unfollow users who don't follow back."""
    for user in users_to_unfollow:
        url = f"{BASE_URL}/user/following/{user}"
        response = requests.delete(url, headers=HEADERS)
        if response.status_code == 204:
            print(f"Unfollowed {user}")
        else:
            print(f"Failed to unfollow {user}: {response.status_code}")

if __name__ == "__main__":
    following = get_following()
    followers = get_followers()
    
    # Find users you follow who don't follow you back
    non_mutuals = following - followers
    
    if non_mutuals:
        print(f"Unfollowing {len(non_mutuals)} users who don't follow back...")
        unfollow_users(non_mutuals)
    else:
        print("No non-mutual follows found.")