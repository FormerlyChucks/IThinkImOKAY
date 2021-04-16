import praw, traceback

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",
    username="my username",
    password="my password"
)

while True:
    try:
        for submission in reddit.subreddit('canadianproblems').new(limit=None):
            submission.mod.lock()
            submission.mod.flair(text="FLAIR TEXT", css_class="CSS CLASS IF YOU WANT")
        for submission in reddit.subreddit('canadianproblems').hot(limit=None):
            submission.mod.lock()
            submission.mod.flair(text="FLAIR TEXT", css_class="CSS CLASS IF YOU WANT")
        for submission in reddit.subreddit('canadianproblems').top(limit=None):
            submission.mod.lock()
            submission.mod.flair(text="FLAIR TEXT", css_class="CSS CLASS IF YOU WANT")
        for submission in reddit.subreddit('canadianproblems').controversial(limit=None):
            submission.mod.lock()
            submission.mod.flair(text="FLAIR TEXT", css_class="CSS CLASS IF YOU WANT")
    except Exception:
        print(traceback.format_exc())
