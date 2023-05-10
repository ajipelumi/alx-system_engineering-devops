#!/usr/bin/python3
""" This script queries Reddit API. """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries reddit and returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My Custom User-Agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    subreddit_data = response.json().get('data')
    after = subreddit_data.get('after')
    subreddit_children = subreddit_data.get('children')
    for data in subreddit_children:
        children_data = data.get('data')
        hot_title = children_data.get('title')
        hot_list.append(hot_title)
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
