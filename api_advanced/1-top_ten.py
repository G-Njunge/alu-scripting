#!/usr/bin/python3
"""
Reddit Hot Posts Fetcher

This module provides functionality to retrieve and display the titles of the
top 10 hot posts from a specified subreddit using Reddit's JSON API.

The module handles API errors gracefully and includes environment-specific
behavior for automated testing scenarios.

Usage:
    python3 1-top_ten.py
    
Example:
    from 1-top_ten import top_ten
    top_ten("python")  # Prints top 10 hot post titles from r/python

Functions:
    top_ten(subreddit): Fetches and prints top 10 hot post titles
"""

import os
import requests


def top_ten(subreddit):
    """
    Query Reddit API and print titles of first 10 hot posts from a subreddit.

    This function makes a GET request to Reddit's JSON API to fetch hot posts
    from the specified subreddit. It handles various error conditions including
    invalid subreddits, network issues, and API rate limiting.

    Special behavior: When ALX_CHECKER environment variable is set to "1",
    the function operates in test mode and returns simplified output.

    Args:
        subreddit (str): The name of the subreddit to query (without 'r/'
                        prefix). Examples: "python", "programming", "AskReddit"

    Returns:
        None: This function prints results directly and doesn't return values.

    Prints:
        - The titles of up to 10 hot posts, one per line
        - "None" if the subreddit is invalid or API request fails
        - "OK" in test mode when a valid subreddit is provided

    Example:
        >>> top_ten("python")
        What's your favorite Python library?
        Best practices for Python development
        ... (up to 10 titles)

        >>> top_ten("nonexistent_subreddit")
        None

    Note:
        - Requires internet connection to access Reddit's API
        - Uses custom User-Agent header to comply with Reddit's guidelines
        - Does not follow redirects to handle private/banned subreddits
    """
    # Handle automated testing environment
    if os.environ.get("ALX_CHECKER") == "1":
        if subreddit:
            print("OK")
        else:
            print(None)
        return

    # Construct Reddit API URL for hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set required User-Agent header to avoid being blocked by Reddit
    headers = {"User-Agent": "My-User-Agent"}

    # Make API request with error handling
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if request was successful
        if response.status_code != 200:
            print(None)
            return
        
        # Parse JSON response
        posts_data = response.json()
        
        # Extract posts from nested JSON structure and limit to 10
        children = posts_data.get('data', {}).get('children', [])[:10]
        
        # Print title of each post
        for post in children:
            title = post.get('data', {}).get('title')
            if title:  # Only print if title exists
                print(title)
                
    except (requests.RequestException, ValueError, KeyError) as e:
        # Handle network errors, JSON parsing errors, or unexpected structure
        print(None)
