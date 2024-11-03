def divideBy(a,b): 
	return a / b

try: 
	value = divideBy(12,0)
except ZeroDivisionError as e:
	print('Cannot divide by zero.', e)
except Exception as e:
	print(e, 'Something went wrong')


# Index error
index = 6
items = [1,2,3,4,5]
item = 0
try:
	item = items[index]
except IndexError as e:
	print(e,f"Index {index} does not exist on `items`")

# File does not exist
filename = 'file_does_not_exist.txt'
try:
	with open(filename, 'r') as file:
		print(file.read())
except FileNotFoundError as e:
	print(e, f'{filename} not found')