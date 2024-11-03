# KeyWord args

def sum_of_two(a, b):
	return a + b
def sum_of(*args):
	sum = 0
	for x in args:
		sum += x
	return sum

print('Sum of 4 and  = ',sum_of_two(4,5))
# print('Sum of 3, 4 and 5',sum_of_two(3, 4,5)) # will throw an error
print('Sum of 3, 4 and 5 = ',sum_of(3, 4,5))

# Use keyword args to allow passing of key/value pairs
def kwargSums(**kwargs): # note the double **
	sum = 0
	for k,v in kwargs.items():
		sum += v
	return sum

print('Beer + coffee',kwargSums(beer=5,coffee=2.55))