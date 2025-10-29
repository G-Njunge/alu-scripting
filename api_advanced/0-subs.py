#!/usr/bin/python3
import json
import requests
import sys

def number_of_subscribers(subreddit):
    base_url = "https://www.reddit.com"
    headers = {"User-Agent": "myApp/1.0 by u/YourUsername"}
    about = requests.get(f"{base_url}/r/{subreddit}/about.json", headers=headers)
    about_parsed = about.json()
    
    #check if the subreddit exists
    if about.status_code == 200:
        subscribers = about_parsed.get("data",{}).get("subscribers")
    elif about.status_code == 404:
        print("this_is_a_fake_subreddit")
        sys.exit(1)
    else:
        about_parsed.raise_for_status()
    return subscribers
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print((number_of_subscribers(sys.argv[1])))
       