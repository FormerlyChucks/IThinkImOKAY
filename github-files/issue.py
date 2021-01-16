import time, praw, github, traceback

g = github.Github('')
repo = g.get_repo("")

reddit = praw.Reddit(client_id="", client_secret="", user_agent="")
sub_list = ""
s_body = """Title: {}
Author: {}
Subreddit: {}
Shortlink: {}"""


while True:
    try:
        for submission in reddit.subreddit(sub_list).stream.submissions(skip_existing=True):
            repo.create_issue(title=submission.id, body=s_body.format(submission.title, submission.author, submission.subreddit, submission.shortlink))
            print('issue made')
        #open_issues = repo.get_issues(state='open')
        #for issue in open_issues:
            #issue.edit(state='closed')
    except Exception:
        print(traceback.format_exc())
        time.sleep(600)
