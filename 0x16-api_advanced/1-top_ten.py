#!/usr/bin/python3
"""
This is used to obtain number of subs in a subreddit again
"""
import requests


def top_ten(subreddit):
    """
        This is used to obtain number of subs in a subreddit
    """
    try:
        u_a_url = f"""https://www.reddit.com/r/{subreddit}/hot.json?limit=10"""
#        print(u_a_url)
        headers = {'User-Agent': 'MyRedditApp/1.0'}
        # user_response always returns status code
        user_response = requests.get(u_a_url,
                                     headers=headers, allow_redirects=False)
        user_response.raise_for_status()
        user_data = user_response.json()  # have it as readable JSON format.
#        print(user_data)
#        print()
        for post in user_data["data"]["children"]:
            print(post["data"]["title"])
    except requests.exceptions.HTTPError as errh:
        if user_response.status_code == 404:
            print(None)
