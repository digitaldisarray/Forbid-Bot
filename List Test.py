# The purpose of this script is to make sure list.txt is formatted properly.
text = []
phrases = []
punishments = []

f = open('./list.txt')
print('Opened file.')

raw = f.read()
print('Ran file read.')

text = raw.split(':')
print('Split the string.')

for i in range(len(text)):
	if (i % 2) == 0:
		# Even
		phrases.append(text[i].rstrip())
	else:
		# Odd
		punishments.append(text[i].rstrip())

print('If the phrases and punishments are in the right places, your list.txt is formatted correctly.')
print('Phrases: ' + phrases)
print('Punishments' + punishments)
