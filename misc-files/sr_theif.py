import praw, time

karma_needed = 25000

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="",
                     username="",
                     password="")
while True:
    try:
        for submission in reddit.subreddit("").stream.submissions(skip_existing=True):
            karma = submission.author.comment_karma + submission.author.link_karma
            if karma >= karma_needed:
                reddit.subreddit("").contributor.add(submission.author.name)
                print('Invited:',submission.author.name)
    except Exception as e:
        print(e)
        time.sleep(600)
