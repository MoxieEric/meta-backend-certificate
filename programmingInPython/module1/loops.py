# For Loop
txt = 'Ima Looper'

# loop over a sequence type, e.g. a string
for letter in txt:
	print(letter)

# loop over an array
favorites = ['Chocolate', 'Vanilla', 'Strawberry', 'Mint']

# basic for loop of a List
for flavor in favorites:
	print(f'I like {flavor}')

# using inumerate and an index
for idx, flavor in enumerate(favorites):
	print(f'{idx} {flavor}')

# # While loop
count = 0
while count < len(favorites):
	print(f'I like {favorites[count]}')
	count+=1


# break
for flavor in favorites:
	if flavor == 'Chocolate':
		print(f'{flavor} is one of my favorites!')
		break # break stops the loop
	else: 
		print('Sorry, I do not like that')

# continue
for flavor in favorites:
	if flavor == 'Chocolate':
		continue # skips over the remaining code, but does not stop the loop
		print('I like chocolate') # this will not be printed
	print(f'I like{flavor}')

# pass
for flavor in favorites:
	if flavor == 'Chocolate':
		pass # code within the if gets ignored, but the loop continues
	print(f'I like{flavor}')
