# basic write to a file.
# using w mode will create the file if it doe not already exist
# with open('./assets/test.txt', 'w') as file:
# 	file.write('Howdy there!')

def readLines():
	with open('sampletext.txt') as file:
		return file.read()

# write lines
def writeLines():
	try:
		with open('./assets/test.txt', 'w') as file:
			file.writelines(['Howdy there\n', 'Oh. Hey\n', 'What? You do not sound happy to see me.\n', 'meh...'])
	except FileNotFoundError as e:
		print('Check your path. File not found.',e, )
	except Exception as e:
		print('Error:', e)


# append lines
def appendLines():
	try:
		with open('./assets/test.txt', 'a') as file:
			file.writelines(['Howdy there\n', 'Oh. Hey\n', 'What? You do not sound happy to see me.\n', 'meh...'])
	except FileNotFoundError as e:
		print(e, 'File was not found.')
	except Exception as e:
		print('Error:', e)

appendLines()