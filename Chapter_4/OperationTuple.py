t = (10, 20, 30, 40, 50)

print(t[0]) #Accessing

print(t[1:4]) #Slicing

t1 = (1 ,2)
t2 = (3, 4)

t3 = t1 + t2       #Concatenation
print(t3)

print(t1 * 3)   #Repetition

print(2 in t1)      #Membership  return boolean answer is no. is present in tuple or not
print(99 in t1)

#Lenght, Min, Max, Sum

print(len(t))
print(max(t))
print(min(t))
print(sum(t))

#unpacking

a, b = t1           #wrap element of the tuple in different variable
print(a, b)

*c, d = t2

print(c, d)

t3 = (1,(3, 4), 5)

print(t3[1][0])

del t3

# print(t3)     give error because t3 is delect (del)

#converting Tuple
#tuple to list

list = (t)

tuple([1, 2 ,3])


