print('Howdy world')

# Function to introduce me
def introduce_me():
	name = 'Er' # my name
	if name == 'Eric':
		print('My name is ' + name)
	else:
		print('I am not Eric')

introduce_me()

# multiple variable assignments, kinda like array destructuring in JS
firstName,lastName = 'Eric', 'Nowels'
print(lastName,', ', firstName)

#delete a var

del lastName
# print(firstName,lastName) # will fail

####
# Vars
####

aNumber = 4 # a number, but more specifically, an integer subset
aFloat = 3.14 # a float, another subset of number

aString = 'Hello there' # it's a string...
anotherString = 'Well howdy!'

aList = [aNumber,aString, aFloat] # a list is an ordered array of similar data types
print('List Demo: ', aList[2]) # accessing values is the same as JS syntax, using square brackets to reference a zero-based index

aTuple = (2, 4, 'howdy', 5.25) # tuples are immutable arrays or lists, the key difference in assignment is the parenthasis compared to square brackets

# Dictionaries
# key-value pairs, like objects in JS
# like lists and tuples they can hold various data types
# assign with curly braces
aDictionary = {'aardvark': 'first', 'zelda': 99 }

# access dictionary entries by a named key in square brackets 
print(aDictionary['zelda'])

aBoolean = False  # true/false, just remember that they are case sensitive! true != True != TRUE

# Sets
# Unordered, non-indexed, but unique values
# create sets with curly braces, but they do not have keys!
exampleSet = {'me', 'you', 5}

# accessing individual elements in a set is not ideal
# they hold data and are designed to check for existence or for using loops
print( 'you' in exampleSet) # the value is in the set -- will print True

###
# Types
###
print(type(aString)) # string
print(type(aNumber)) # integrer
print(type(aFloat)) # float
print(type(aTuple)) # tuple
print(type(exampleSet)) # set
print(type(aDictionary)) # dictionary
