#!/usr/bin/python3
"""
This is used to obtain number of subs in a subreddit again
"""
import requests


def number_of_subscribers(subreddit):
    """
        This is used to obtain number of subs in a subreddit
    """
    try:
        users_api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {'User-Agent': 'MyRedditApp/1.0'}
        # u_res always returns status code
        u_res = requests.get(users_api_url,
                             headers=headers, allow_redirects=False)
        u_res.raise_for_status()
        if 'application/json' not in u_res.headers.get('Content-Type', ''):
            return 0
        user_data = u_res.json()  # have it readable JSON format.
        return int(user_data["data"]["subscribers"])
    except requests.exceptions.HTTPError as errh:
        if u_res.status_code == 404:
            return 0
