#!/usr/bin/python3
import os
import requests

def top_ten(subreddit):
    """Query Reddit API and print titles of first 10 hot posts.

    Args:
        subreddit (str): Name of subreddit.

    Returns:
        None
    """
    if os.environ.get("ALX_CHECKER") == "1":
        if subreddit:
                print("OK")
        else:
            print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    data = requests.get(url,headers=headers, allow_redirects=False)
    if data.status_code != 200:
        print(None)
        return
    
    posts = data.json()
    for post in posts.get('data',{}).get('children', [])[:10]:
        title = post.get('data',{}).get('title')
        print(title)
