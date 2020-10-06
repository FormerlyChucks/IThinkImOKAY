import time
from github import Github

file = ''
token = ''
repository = ''
message = ''
content = ''


g = Github(token)

while True:
    try:
        repo = g.get_repo(repository)
        repo_file = repo.get_contents(file, ref="main")
        repo.update_file(file, message, content, repo_file.sha)
        time.sleep(5)
    except Exception as e:
        print(e)
        time.sleep(60)
