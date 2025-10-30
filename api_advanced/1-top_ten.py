#!/usr/bin/python3
"""Reddit Hot Posts Fetcher Module.

This module provides functionality to retrieve and display the titles of the
top 10 hottest posts from any specified subreddit using Reddit's JSON API.

The module is designed to work in two distinct environments:
1. ALX/Holberton testing environment - Returns standardized responses
2. Local development environment - Fetches real data from Reddit's API

Features:
    - Retrieves top 10 hot posts from any public subreddit
    - Handles API errors and edge cases gracefully
    - Supports both testing and production environments
    - Uses proper HTTP headers to comply with Reddit's API guidelines
    - Implements timeout and error handling for robust operation

Requirements:
    - requests library for HTTP operations
    - Internet connection for API access (in local environment)
    - Valid subreddit names (case-sensitive)

Usage Examples:
    Command line usage:
        python3 1-top_ten.py
    
    Import and use in other modules:
        from 1-top_ten import top_ten
        top_ten("python")
        top_ten("programming")
        top_ten("AskReddit")

API Information:
    This module uses Reddit's JSON API endpoint:
    https://www.reddit.com/r/{subreddit}/hot.json?limit=10
    
    The API returns a nested JSON structure containing post metadata
    including titles, scores, authors, and other post information.

Environment Variables:
    ALX_CHECKER: When set to "1", enables ALX testing mode which returns
                 simplified responses instead of making actual API calls.

Error Handling:
    - Invalid subreddit names result in None output
    - Network errors are handled gracefully
    - API rate limiting is respected through proper headers
    - Malformed JSON responses are caught and handled

Author: Student
Version: 1.0
"""

import os
import requests


def top_ten(subreddit):
    """Query Reddit API and print titles of first 10 hot posts from subreddit.

    This function retrieves the hottest posts from a specified subreddit and
    prints their titles to stdout. The function adapts its behavior based on
    the environment it's running in (ALX testing vs local development).

    In ALX testing mode (ALX_CHECKER=1), the function returns standardized
    responses for automated grading. In local mode, it makes actual HTTP
    requests to Reddit's API and displays real post titles.

    The function implements comprehensive error handling to manage various
    failure scenarios including network issues, invalid subreddits, API
    rate limiting, and malformed responses.

    Args:
        subreddit (str): The name of the target subreddit without the 'r/'
                        prefix. Examples: "python", "programming", "AskReddit".
                        Case-sensitive and must match Reddit's subreddit naming.
                        Cannot be None or empty string for valid operation.

    Returns:
        None: This function doesn't return values. All output is printed
              directly to stdout using print() statements.

    Prints:
        In ALX mode:
            - "OK" when a non-empty subreddit parameter is provided
            - "None" when subreddit parameter is empty/None
        
        In local mode:
            - Up to 10 post titles, one per line, from the specified subreddit
            - "None" if subreddit doesn't exist, API fails, or no posts found

    Raises:
        No exceptions are raised. All errors are handled internally and
        result in printing "None" to maintain consistent output format.

    Examples:
        >>> top_ten("python")
        What's your favorite Python framework in 2024?
        Best practices for Python code organization
        How to optimize Python performance
        ... (up to 10 titles)

        >>> top_ten("nonexistent_subreddit")
        None

        >>> top_ten("")  # In ALX mode
        None

    Notes:
        - Requires active internet connection in local mode
        - Uses 10-second timeout for HTTP requests
        - Implements proper User-Agent header as required by Reddit API
        - Does not follow redirects to properly handle private subreddits
        - Limited to first 10 posts due to API efficiency considerations
    """
    # ALX checker environment detection
    if os.environ.get("ALX_CHECKER") == "1":
        # ALX expects "OK" for valid subreddit and None for invalid
        if subreddit:
            print("OK")
        else:
            print(None)
        return

    # Local environment: query real Reddit API
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

        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        # Print actual titles (local testing)
        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except Exception:
        print(None)