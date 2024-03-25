import praw
from dotenv import load_dotenv
import os

load_dotenv()


def get_memes():
    praw_client_id = os.getenv('PRAW_CLIENT_ID')
    praw_client_secret = os.getenv('PRAW_SECRET')
    reddit = praw.Reddit(client_id=praw_client_id, client_secret=praw_client_secret,
                         user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
    subreddit = reddit.subreddit('memes')
    top_memes = subreddit.top(time_filter='day', limit=20)
    top_memes_list = []
    for submission in top_memes:
        top_memes_list.append({
            'title': submission.title,
            'score': submission.score,
            'url': submission.url,
            'created_utc': submission.created_utc,
            'author': submission.author.name if submission.author else 'Unknown'
        })
    return top_memes_list