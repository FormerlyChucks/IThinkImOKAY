import praw

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="",
                     username="",
                     password="")

usr = input('who to ban? ')
reason = input('reason? ')
perms = ['all','access']

for subreddit in reddit.user.me().moderated():
    for moderator in subreddit.moderator():
        if moderator == reddit.user.me():
            for perm in moderator.mod_permissions:
                if perm in perms:
                    subreddit.banned.add(usr, ban_reason=reason)
                    print('Successfully b& /u/{} from /r/{}'.format(usr,subreddit))
