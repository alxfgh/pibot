import praw
import config

def login():
    r = praw.Reddit(username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "Pi Finder Bot")
    return r

def run(r):
    for comment in r.subreddit('all').comments(limit=25):
        if "3.14" or 3.14 in comment.body:



r = login()