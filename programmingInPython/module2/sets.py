# Sets
# collection of unorded non-duplicate items -- you cannot access values by index
aSet = {1,2,3,4,5,5}
bSet = {3,4,5,6,7,8}
print(aSet)

# add an item
aSet.add(6)

# remove an item
aSet.remove(6)
aSet.discard(6)

# Merge 2 sets with a union
newSet = aSet.union(bSet)
anotherNewSet = aSet | bSet

print('newSet',newSet)
print('anotherNewSet', anotherNewSet)


# Intersection - assigns only overlapped values
print('interesction of aSet and bSet', aSet.intersection(bSet))

# Set Difference - reduces to non-shared values. inverse of intersection
print('difference of aSet and bSet', aSet.difference(bSet))
print('difference of aSet and bSet alt syntax', aSet - bSet)

# Symetrical difference - values in either set, but not both
print('Symetrical difference', aSet.symmetric_difference(bSet))
print('Symetrical difference alt syntax', aSet ^ bSet)

