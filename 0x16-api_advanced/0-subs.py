#!/usr/bin/python3
""" This script queries Reddit API. """
import requests


def number_of_subscribers(subreddit):
    """
    Queries reddit for the number of subscribers for
    a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My Custom User-Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        subreddit_data = response.json().get('data')
        subreddit_subs = subreddit_data.get('subscribers')
        return subreddit_subs
    else:
        return 0
