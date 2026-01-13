a = "krishna"
a = 'krishna'
a = '''krishna'''

# string is immutable

#indexing of string in python

#  0   1  2  3  4  5  6
#  K   r  i  s  h  n  a
#  -7 -6 -5 -4 -3 -2 -1

#slice

nameshort = a[0:5]
# print(nameshort)


# negative indexing
nameshort = a[-7:-2]
# print(nameshort)


# print(a[1:]) # rishna in empty place it take length-1 a[1:7]
# print(a[:7]) # krishna in empty place it take 0 a[0:70]

#slice with skip value

str = "0123456789abcdefghijklmnopqrstxyz"

print(str[1:10:4])
print(str[::2])
print(str[1::2])