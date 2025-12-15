import requests
import time
import os
from dotenv import load_dotenv  

load_dotenv()
# Create an .env file and update the fields with your github info(be sure to enable the 'user' scope when creating token)
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
ignore_list_str = os.getenv("IGNORE_LIST", "")
IGNORE_LIST = set(user.strip() for user in ignore_list_str.split(",") if user.strip())


BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
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


    #update ignore list with followers you would like to follow even if they are not following you back ie #important users who you dont expect a follow from eg microsoft
    #Uncomment the unfollow_users line to enable unfollowing
    non_mutuals = following - followers - IGNORE_LIST  # Users you follow who don't follow back
    if non_mutuals:
        print(f"Unfollowing {len(non_mutuals)} users who don't follow back...")
        print(non_mutuals)
        #unfollow_users(non_mutuals)
    else:
        print("✅ No non-mutual follows found.")

    #find potential new users to follow 
    #find colloborators of your followers and see if you want to follow them