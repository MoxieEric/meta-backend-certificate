# Dictonary
# Collection of key/value pairs. Much faster to access values than Lists or Sets

sampleDictionary = {
	1: 'Coffee',
	2: 'Beer',
	3: 'Whiskey',
	'nightcap': 'cognac'
}

# Access by key, which can be integer or string
print('What you drink in the morning: ', sampleDictionary[1])
print('What you drink socially before turning in: ', sampleDictionary['nightcap'])

# modify a dictionary value
sampleDictionary['nightcap'] = 'Port'
sampleDictionary['bedtime'] = 'water'

# delete a value
del sampleDictionary[3]


# Iterate
print("Iterating over dictionaries#\n#\n")

for x in sampleDictionary:
	print(x) # prints the key only
	print(sampleDictionary[x]) # print value, using key

for k, v in sampleDictionary.items():
	print(k, ' is ', v)