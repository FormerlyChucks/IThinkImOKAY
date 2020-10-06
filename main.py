import time
from github import Github

token = ''

g = Github(token)

while True:
    try:
        repo = g.get_repo('')
        file = repo.get_contents('', ref="main")
        repo.update_file('', "+1 commit <3", "This is just a test!", file.sha)
        time.sleep(5)
    except Exception as e:
        print(e)
        time.sleep(60)
