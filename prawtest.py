import praw
import config

def bot_login():
    r = praw.Reddit(username=config.username,
            password=config.password,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent="test python bot")

    return r

def run_bot(r):
    for submission in r.subreddit("python").top("all"):
        print(submission.title)

# r = bot_login()
run_bot(bot_login())