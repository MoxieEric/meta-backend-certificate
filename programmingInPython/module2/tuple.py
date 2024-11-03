# define a tuple
# tuples are just like a List, but immutable
someTuple = (1, 'some string', 2.25, False) # preferred syntax / best practice
someOtherTuple = 1, 'a string', 1.5, True # also works, but not best practice

print(someTuple[1]) # get by index

print(someOtherTuple.count('string')) # prints number of strings within the tuple
print(someOtherTuple.index(1.5)) # returns the index where the value can be found within the tuple

# loop over a tuple
for x in someTuple:
	print(x)