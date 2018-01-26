import discord # Make sure you have discord.py installed!
import asyncio

client = discord.Client()

error = '[ ERROR ] - '
warn =  '[ WARN ] -'
info =  '[ INFO ] - '


text = []
phrases = []
punishments = []

@client.event
async def on_ready():
    print(info + 'Logged In!')
    print('Username: ' + client.user.name)
    print('User ID: ' + client.user.id)
    print('=====================')
    f = open('./list.txt')
    print(info + 'Opened file.')
    
    raw = f.read()
    print(info + 'Ran file read.')
    
    text = raw.split(':')
    print(info + 'Split the string.')
    
    for i in range(len(text)):
	if (i % 2) == 0:
		# Even
		phrases.append(text[i].rstrip())
	else:
		# Odd
		punishments.append(text[i].rstrip())


@client.event
async def on_message(message):
	for i in range(len(phrases)):
		if message.content.lower().contains(phrases[i]):
			Client.delete_message(message)
			if punishments[i] == 'k'
				# Kick
				Client.kick(member)
				print(info + 'Kicked ' + message.author + ' for saying: ' + message.content)
			elif punishments[i] == 'b'
				# Ban
				Client.ban(member)
				print(info + 'Banned ' + message.author + ' for saying: ' + message.content)
			#elif punishments[i] == 'm'
				# TODO: Add time based mute.
				#mute(message.author)

client.run('INSERT TOKEN HERE') # Make sure you have added your own token!
