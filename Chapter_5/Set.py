# Set is colllection of non-repetitive element

#how to creat empty set

EmpytSet = {}
print(type(EmpytSet))  # this will print dictionary
EmpytSet = set();
print(type(EmpytSet)) # this will print set



set = {1,2,3,4,5,5,5,6,7}
print(set)

# set is mutable, unordered, unindexed
#set cannot contain duplicate element

#Methods

print(len(set)) # return length of set

set.add(8) # add element to set
print(set)

set.remove(8) # remove element from set
print(set)

set.pop() # remove random element from set
print(set)

# set.clear() # clear all element from set
# print(set)

set.update([9,10,11]) # add multiple element to set
print(set)

set.discard(11) # remove multiple element from set and if element not present it will not give error
print(set)

unionSet = set.union({5,6,7,8,9,10}) # return union of two sets
print(unionSet)

intersectionSet = set.intersection({5,6,7,8,9,10}) # return intersection of two sets
print(intersectionSet)



set1 = {1,2,3,4}
set2 = {3,4,5,6}
differenceSet = set1.difference(set2) # return set which is in set1 but not in set2
print(differenceSet)

symmetricDifferenceSet = set1.symmetric_difference(set2) # return set which is in set1 or set2 but not in both
print(symmetricDifferenceSet)



print({1,2}.issubset(set1)) # return boolean value if set1 is subset of set2
print(set1.issuperset({1,2})) # return boolean value if set1 is superset of set2

copySet = set1.copy() # return copy of set1
print(copySet)

set1 = {1,2}
set2 = {3,4}

print(set1.isdisjoint(set2)) # return boolean value if set1 and set2 have no element in common