import difflib, praw, random, raw, time, traceback, yaml

with open("ruqqus.yaml") as config_file:
    config = yaml.safe_load(config_file)
    user_agent = config['user_agent']
    ruqqus_client_id = config['ruqqus_client_id']
    ruqqus_client_secret = config['ruqqus_client_secret']
    ruqqus_refresh_token = config['ruqqus_refresh_token']
    reddit_client_id = config['reddit_client_id']
    reddit_client_secret = config['reddit_client_secret']
    
ruqqus = raw.Ruqqus(client_id=ruqqus_client_id,
                    client_secret=ruqqus_client_secret,
                    user_agent=user_agent,
                    access_token=open('/tmp/ruqqus_token').read(),
                    refresh_token=ruqqus_refresh_token)
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=user_agent)

listing_data = {'page':1,'sort':'new','ignore_pinned':False}
r = ruqqus.get('/api/v1/all/listing',data=listing_data)
old_ids = [submission['id'] for submission in r['data']]
print(old_ids)

while True:
    try:
        print('------------------------------------------------')
        new = ruqqus.get('/api/v1/all/listing',data=listing_data)
        for s in new['data']:
            if s['id'] not in old_ids:
                print(s['id'])
                print(s['title'])
                old_ids.append(s['id'])
                for result in reddit.subreddit('all').search(s['title'],limit=None):
                    print(result.title)
                    if result.num_comments >= 2:
                        similarity = difflib.SequenceMatcher(None, result.title,s['title']).ratio()
                        if similarity >= .8:
                            comment = result.comments[random.randint(0,result.num_comments)]
                            print(comment.id)
                            if comment.body != '[deleted]' and comment.stickied == False:
                                print(comment.body)
                                params = {'parent_fullname':'t2_'+s['id'],'body':comment.body}
                                c = ruqqus.post('/api/v1/comment',data=params)
                                print(c['permalink'])
                break
        time.sleep(30)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
    except KeyboardInterrupt:
        print('Shutting Down :(')
        quit()
