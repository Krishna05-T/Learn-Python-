list = [1, 2, 34.5, "Krishna", "Rohan", "Mohan", False]

print(list)

#Ulike string list are mutable so if we make change in list so it also occur in original list

print(list[2])

list[4] = "Shayam"

print(list)

print(list[1:4])



#Method of list 
li = [5, 33, 8, 4, 45, 23, 90]

li.append(100) # Adds 100 to the end of the list
print(li)

li.sort() # Sorts the list in ascending order
print(li)

li.reverse() # Reverses the order of the list
print(li)

li.insert(1, 95) # Inserts 95 at index 1
print(li)

value = li.pop(1) # Removes the element at index 1
print(value)
print(li)

li.remove(45) # Removes the first occurrence of 45 from the list
print(li)

li2 = [3,5,7,44,87,21,90];

li2.extend([4, 7, 6]) # adds multiple elements (another list)
print(li2)

print(li2.index(44)) #Returens index of first occurrence of 44

print(li2.count(7)) # Count occurrences of 7

copyofli2 = li2.copy() # Returns a shallow copy of the list

print(li2)
print(copyofli2)

copyofli2.clear() #Remove all elements from the list
print(copyofli2)

# python Chapter_4/list.py  : When you run this file in terminal