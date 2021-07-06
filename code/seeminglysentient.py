import time, praw, random, traceback, difflib

username = ''
client_secret = ''
user_agent = ''
password = ''
username = ''
subs = ''

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     password=password,
                     username=username)

reddit.validate_on_submit = True
x = random.randint(0,1)

while True:
    try:
        for submission in reddit.subreddit(subs).stream.submissions(skip_existing=True):
            for results in reddit.subreddit(subs).search(submission.title):
                similarity = difflib.SequenceMatcher(None, submission.title,results.title).ratio()
                if results.num_comments >= 2 and similarity >= .8:
                    comment = results.comments[x]
                    if comment.author not in usernames and comment.body != '[deleted]':
                        submission.reply(comment.body)
                        break
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('shutting down :(')
        quit()
