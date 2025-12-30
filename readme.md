# 🤖 GitHub Unfollow Bot

A simple automation tool that unfollows inactive or unwanted users on your GitHub account. Great for keeping your "Following" list clean and relevant.

![GitHub stars](https://img.shields.io/github/stars/condongilbert/UnfollowProg?style=social)
![Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)

---

## 🔧 Features

- ✅ Automatically unfollows users based on:
  - Inactivity (no recent repos or commits)
  - Follower/following ratio
  - Custom blocklist
- ✅ Dry-run mode to preview who would be unfollowed
- ✅ Optional logging and backup of unfollowed users
- ✅ Works with GitHub Personal Access Token (PAT)

---

## 🚀 Getting Started

### 🔐 1. Generate a GitHub Token

Create a GitHub [Personal Access Token](https://github.com/settings/tokens) with the following scopes:

- `read:user`
- `user:follow`

### 🛠️ 2. Clone the Repo

    git clone https://github.com/yourusername/github-unfollow-bot.git
    cd github-unfollow-bot

### 📁 3. Environment Setup

To configure the bot, create a `.env` file in the root of the project using the format below:

    # .env

    # Your GitHub username
    GITHUB_USERNAME=your_github_username

    # Your GitHub personal access token
    GITHUB_TOKEN=your_github_token_here

    # Optional: usernames to always keep following (comma-separated)
    IGNORE_LIST=torvalds,octocat,myfriend123

> 📌 You can use the provided `.env.example` file as a template:

    cp .env.example .env

### ⚠️ .env Security Reminder

Your `.env` file contains sensitive information. **Do not commit it** to version control.

Ensure this line is in your `.gitignore`:

    .env

### ▶️ 4. Run the Bot

    python unfollow_bot.py

Optional flags:

    --dry-run           # Show who would be unfollowed without taking action
    --min-followers 10  # Unfollow users with fewer than 10 followers
    --inactive-days 180 # Unfollow users inactive for more than 180 days

---

## 🧪 Example Output

    [INFO] Unfollowing @inactiveDev123 - last commit 400 days ago
    [INFO] Skipping @torvalds (on ignore list)

---

## 💡 Why Use This?

If you follow hundreds of developers, it becomes hard to manage who's worth following. This tool helps you:

- Clean up inactive follows
- Remove spam or irrelevant accounts
- Maintain a relevant feed and professional network

---

## 🤝 Contributing

Pull requests are welcome! You can contribute by:

- Adding more filtering logic
- Improving CLI output
- Creating a GitHub Action version

---

## 📄 License

MIT © 2025 [Gilbert Condon](https://github.com/condongilbert)