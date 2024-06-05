#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
        This is used to obtain number of subs in a subreddit
    """
    try:
        users_api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {'User-Agent': 'MyRedditApp/1.0'}
        # user_response always returns status code
        user_response = requests.get(users_api_url, headers=headers)
        user_response.raise_for_status()
        user_data = user_response.json()  # have it readable JSON format.
        return user_data["data"]["subscribers"]
    except requests.exceptions.HTTPError as errh:
        if user_response.status_code == 404:
            return 0
