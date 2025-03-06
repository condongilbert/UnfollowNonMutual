import requests
import time

# Replace with your GitHub username and token
GITHUB_USERNAME = "enter your username here"
TOKEN = "enter your token here"

BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_paginated_list(url):
    """Fetch all pages of a paginated GitHub API response."""
    results = set()
    page = 1
    while True:
        response = requests.get(f"{url}?per_page=100&page={page}", headers=HEADERS)
        if response.status_code != 200 or not response.json():
            break
        results.update(user['login'] for user in response.json())
        page += 1
    return results

def get_following():
    """Get a list of users you are following."""
    return get_paginated_list(f"{BASE_URL}/users/{GITHUB_USERNAME}/following")

def get_followers():
    """Get a list of users following you."""
    return get_paginated_list(f"{BASE_URL}/users/{GITHUB_USERNAME}/followers")

def unfollow_users(users_to_unfollow):
    """Unfollow users who don't follow back."""
    for user in users_to_unfollow:
        url = f"{BASE_URL}/user/following/{user}"
        response = requests.delete(url, headers=HEADERS)
        if response.status_code == 204:
            print(f"✅ Unfollowed {user}")
        else:
            print(f"❌ Failed to unfollow {user}: {response.status_code} - {response.text}")
        time.sleep(1)  # Avoid rate limits

if __name__ == "__main__":
    following = get_following()
    followers = get_followers()

    non_mutuals = following - followers  # Users you follow who don't follow back

    if non_mutuals:
        print(f"Unfollowing {len(non_mutuals)} users who don't follow back...")
        unfollow_users(non_mutuals)
    else:
        print("✅ No non-mutual follows found.")