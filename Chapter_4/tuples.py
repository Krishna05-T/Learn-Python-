# A tuple is an immutable data type in python

a = (2, 4, 8, "Holy", "Eleven", "Max", True);
print(a)
# a[0] = 7
# print(a) # This will raise a TypeError because tuples are immutable

#single element tuple
single_tuple = (1,)
print(type(single_tuple))

# empty tuple
empty_tuple = ()
print(type(empty_tuple))

# Method of tuple
b = (2,7,986,5,3,9,33,4,51,986,986)

print(b.count(986)) #Retun number of occurrence of value

print(b.index(986)) #Return the first index of value

