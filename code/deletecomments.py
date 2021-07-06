import praw, time

username = ""

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="",
                     username=username,
                     password="")

try:
    for comment in reddit.redditor(username).comments.new(limit=1000):
        comment.delete()
    for comment in reddit.redditor(username).comments.hot(limit=1000):
        comment.delete()
    for comment in reddit.redditor(username).comments.top(limit=1000):
        comment.delete()
    for comment in reddit.redditor(username).comments.controversial(limit=1000):
        comment.delete()
except Exception as e:
    print(e)
    time.sleep(30)
