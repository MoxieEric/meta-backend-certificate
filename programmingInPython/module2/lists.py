# Lists
# Array of mutable values with 0-based index
list = [0,1,2,3]
stringList = ['A', 'B', 'C']
hybridList = ['A', 2, True]

# Insert an item at a specific index
hybridList.insert(len(hybridList), 'a new value')

# Add an item to the end of the list
stringList.append('D')

# Append a list to another list
list.extend([4,5,6])

# remove an item by index
list.pop(0)

# remove an item by index
del list[1]