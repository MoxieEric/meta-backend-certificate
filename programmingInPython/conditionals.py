a = True
b = False

if a:
	print('A is True')
if b:
	print('B is True') # won't print anything

if not(b):
	print('B is false!')

if a:
	print('A is true')
else: 
	print('A was not true')

if b:
	print('B is true')
elif not(a):
	print('A is false')
else:
	print('B was not True and A was not False')
