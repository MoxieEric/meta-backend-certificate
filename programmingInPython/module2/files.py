# Open and close files

# modes
# r - open and read in text format
# rb - open and read binary files. `b` can be appended to any other mode
# r+ open for reading and writing
# w - open for writing
# a - open for appending

# # Open
# open('filename.txt', 'r')

# # Close
# close() # no arguments

# with open() method - automatically closes the file
with open('assets/test.txt', 'r') as file:
	# print(file.read()) # returns entire file contents
	# print(file.readline(4)) # returns n characters/bytes from the current file line
	print(file.readlines()) # returns each line of the file as an item in a List
