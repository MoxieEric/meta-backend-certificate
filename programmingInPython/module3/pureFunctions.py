myList = [1,2,3]

print(f'myList {myList}')

# standard function
def addToListStandard(item):
	myList.append(item)
	return myList

newList = addToListStandard(4)
print(f'newList {newList}')

# pure function
def addToList(item, lst):
	lst.append(item)
	return lst

newestList = addToList(5, myList)
print(f'newestList {newestList}')