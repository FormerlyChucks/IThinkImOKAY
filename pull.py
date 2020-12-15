import time, github, traceback

g = github.Github('')

while True:
    try:
        repo = g.get_repo("")
        fork = g.get_user().create_fork(repo)
        print('forked')
        repo2 = g.get_repo("")
        contents = repo2.get_contents("", ref="main")
        repo2.update_file(contents.path, "", "", contents.sha, branch="main")
        print('updated fork')
        pr = repo.create_pull("", "", 'main', ':main')
        print('pulled')
        base = repo.get_branch("main")
        head = repo2.get_branch("main")
        merge_to_master = repo.merge("main", head.commit.sha, "")
        print('merged')
        repo2.delete()
        print('deleted')
        time.sleep(5)
    except Exception:
        print(traceback.format_exc())
        time.sleep(600)
