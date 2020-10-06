import time
from github import Github

token = ''
repo_file = ''
file1 = ''
message = ''
content = ''
g = Github(token)

while True:
    try:
        repo = g.get_repo(repo_file)
        file = repo.get_contents(file1, ref="main")
        repo.update_file(file1, message, content, file.sha)
        time.sleep(5)
    except Exception as e:
        print(e)
        time.sleep(60)
