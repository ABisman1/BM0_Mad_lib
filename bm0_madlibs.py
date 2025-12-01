import random

gameOn = True

def play():
	verb = input('Please enter a verb: ')
	noun = input('Please enter a noun: ')
	adjective = input('Please enter an adjective: ')

	stories = ['story1', 'story2', 'story3']

	story = random.choice(stories)

	if story == 'story1':
		print('Once Upon a time there was a ' + adjective + ' princess')
		print('This princess lived in a ' + noun)
		print('This princess loved to ' + run)

	elif story == 'story2':
		print('When I go to the beach I love to ' + verb)
		print(f'I always bring a {adjective} {noun}')

	elif story == 'story3':
		print(f'Osei is {adjective}')
		print(f'Because he forgot to {verb} his {noun}')

while gameOn == True:
	play()
	gameOn = False

