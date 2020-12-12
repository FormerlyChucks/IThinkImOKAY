import time, github, traceback

g = github.Github('<github_api_token>')

while True:
    try:
        repo = g.get_repo('<user/repo>')
        file = repo.get_contents('<file_to_update>', ref="main")
        repo.update_file('<file_to_update>', '<commit_message>', '<content_to_write_to_file>', file.sha)
        time.sleep(5)
    except Exception:
        print(traceback.format_exc())
        time.sleep(600)
