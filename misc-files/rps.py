import random

def core(usr,bot):
    if usr == bot:
        return 'tie'
    if usr == 'paper' and bot == 'rock':
        return 'player wins'
    if usr == 'rock' and bot == 'scissors':
        return 'player wins'
    if usr == 'scissors' and bot == 'paper':
        return 'player wins'
    else:
        return 'bot wins'

ops = ['rock', 'paper', 'scissors']
usr = input('choose: ').lower()
bot = random.choice(ops)
chc = core(usr=usr,bot=bot)

while usr not in ops:
    usr = input('choose: ').lower()

print('I chose {}, you chose {}. Result: {}.'.format(bot,usr,chc))
