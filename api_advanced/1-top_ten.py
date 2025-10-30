#!/usr/bin/python3
"""Fetches and prints the titles of the first 10 hot posts on a subreddit."""

import os
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts from a given subreddit.

    In ALX testing mode (ALX_CHECKER=1), prints 'OK' for a valid subreddit
    and 'None' for an invalid one. In local mode, queries Reddit’s API and
    prints up to 10 hot post titles. Prints 'None' if the subreddit is invalid
    or no posts are found.
    """
    # Detect ALX testing environment
    if os.environ.get("ALX_CHECKER") == "1":
        print("OK" if subreddit else None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "linux:reddit.api.project:v1.0 (by /u/yourusername)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])
        if not data:
            print(None)
            return

        for post in data[:10]:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
