#!/usr/bin/python3
""" This script queries Reddit API. """
import requests


def top_ten(subreddit):
    """
    Queries reddit and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'My Custom User-Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        subreddit_data = response.json().get('data')
        subreddit_children = subreddit_data.get('children')
        for data in subreddit_children:
            children_data = data.get('data')
            hot_title = children_data.get('title')
            print(hot_title)
    else:
        print('None')
