import requests

# Replace with your GitHub username and personal access token, be sure to enable the 'user' scope when creating token
GITHUB_USERNAME = "condongilbert"
TOKEN = "enter token"

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

# Get followers and following lists
followers = get_paginated_list(f"https://api.github.com/users/{GITHUB_USERNAME}/followers")
following = get_paginated_list(f"https://api.github.com/users/{GITHUB_USERNAME}/following")

# Find the follower you're not following back
not_following_back = followers - following

if not_following_back:
    print("You are not following back these users:")
    for user in not_following_back:
        print(f"🔍 {user}")
else:
    print("✅ You are following all your followers back!")