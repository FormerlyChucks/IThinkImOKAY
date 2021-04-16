import praw

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="",
                     username="",
                     password="")

try:
    for user in reddit.subreddit("").contributor():
        reddit.subreddit("").contributor.remove(user)
        print("Removed:",user)
except Exception as e:
    print(e)
