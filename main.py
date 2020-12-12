import time, github, traceback #packages to use

g = github.Github('<github_api_token>') #github api token

while True: #while loop, keeps code running
    try: #try the following code:
        repo = g.get_repo('<user/repo>') #github repo
        file = repo.get_contents('<file_to_update>', ref="main") #file to update, branch
        repo.update_file('<file_to_update>', '<commit_message>', '<content_to_write_to_file>', file.sha) #update file, commit message, write some text
        time.sleep(1) #sleep for 1 second
    except Exception: #if any errors, what do?
        print(traceback.format_exc()) #print full traceback
        time.sleep(600) #sleep for 10 minutes
