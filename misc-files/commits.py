import os, random

while True:
    with open('lol','w') as f: f.write(str(random.randint(0,99)))
    os.system('git add . && git commit -m "lol"')
