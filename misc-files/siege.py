import raw, argparse, yaml, time

parser = argparse.ArgumentParser()
parser.add_argument('-g', '--guild', help="Guild to check siege rep reqs", required=True)
args = parser.parse_args()
access_token = open('/tmp/ruqqus_token').read()

with open('ruqqusConfig.yaml') as y:
    config = yaml.safe_load(y)
    username = config['username']
    user_agent = config['user_agent']
    client_id = config['ruqqus_client_id']
    client_secret = config['ruqqus_client_secret']
    refresh_token = config['ruqqus_refresh_token']
    
#ruqqus instance
ruqqus = raw.Ruqqus(client_id=client_id,
                    client_secret=client_secret,
                    user_agent=user_agent,
                    access_token=access_token,
                    refresh_token=refresh_token)

guild = args.guild
rep = 0
page = 1
now = int(time.time())
g = ruqqus.guild(guild)
name = g.name
date = g.created_utc
subs = g.subscriber_count
repneeded = subs//10 + min(180, (now-date)//(60*60*24))

if g.is_siege_protected:
    print('+{} is siege protected, so you will NOT be able to siege it'.format(name))
    quit()

while True:
    data = ruqqus.get('/api/v1/user/{}/listing?page={}'.format(username,page),data={'page': page})['data']
    if len(data)==0:
        break
    for submission in data:
        if submission['guild_name']==guild:
            rep+=submission['score']
    page+=1
page=1
while True:
    data = ruqqus.get('/api/v1/user/{}/comments?page={}'.format(username,page),data={'page': page})['data']
    if len(data)==0:
        break
    for comment in data:
        if submission['guild_name']==guild:
            rep+=submission['score']
    page+=1
    
print('{} rep is needed to siege +{}'.format(repneeded,name))
print('You have aquired a total of {} rep in +{}'.format(rep,name))
