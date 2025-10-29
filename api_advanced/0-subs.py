#!/usr/bin/python3
"""
Reddit Subreddit Subscriber Counter

This script retrieves and displays the number of subscribers for a given subreddit
using Reddit's JSON API. It includes error handling for non-existent subreddits.

Usage: python 0-subs.py <subreddit_name>
Example: python 0-subs.py python
"""

import json
import requests
import sys

def number_of_subscribers(subreddit):
    """
    Fetches the subscriber count for a specified subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        int: Number of subscribers for the subreddit
        
    Exits:
        Terminates program if subreddit doesn't exist (404 error)
    """
    # Reddit's base URL for API requests
    base_url = "https://www.reddit.com"
    
    # Required User-Agent header to avoid being blocked by Reddit's API
    headers = {"User-Agent": "myApp/1.0 by u/YourUsername"}
    
    # Make GET request to Reddit's JSON API endpoint for subreddit info
    about = requests.get(f"{base_url}/r/{subreddit}/about.json", headers=headers)
    
    # Parse the JSON response
    about_parsed = about.json()
    
    # Check if the subreddit exists by examining HTTP status code
    if about.status_code == 200:
        # Successfully found subreddit - extract subscriber count from nested JSON
        # Structure: response["data"]["subscribers"]
        subscribers = about_parsed.get("data",{}).get("subscribers")
        return subscribers
    elif about.status_code == 404:
        # Subreddit doesn't exist - print error message and exit
        print("this_is_a_fake_subreddit")
        return 0
        sys.exit(1)
    else:
        # Other HTTP errors - raise exception with status details
        about_parsed.raise_for_status()
        sys.exit(1)
    

# Main execution block - only runs when script is executed directly
if __name__ == "__main__":
    # Check if user provided a subreddit name as command line argument
    if len(sys.argv) < 2:
        # No argument provided - display usage message
        print("Please pass an argument for the subreddit to search.")
    else:
        # Argument provided - get subscriber count and display result
        # sys.argv[1] contains the first command line argument (subreddit name)
        print((number_of_subscribers(sys.argv[1])))
       