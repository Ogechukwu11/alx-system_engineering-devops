#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """ Reddit API endpoint to get subreddit information """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'CustomBot/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()
        # Check if the subreddit exist
        if 'data' in data and 'subscribers' in data['data']:
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit does not exist or there was an error, return 0
            return 0
    else:
        # If there was an error or the subreddit is invalid, return 0
        return 0
