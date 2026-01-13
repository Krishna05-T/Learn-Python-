str = "krishna"

print(len(str))  # length of string
print(str.startswith("kri")) # True
print(str.endswith("na")) # True
print(str.capitalize()) # Krishna
print("hello world".title()) #Hello World
print(str.upper()) # KRISHNA
print(str.lower()) # krishna
print(str.find("sh")) # 3 (index of first occurrence)
print(str.replace("krishna", "RadheRadhe")) # RadheRadhe    
print(str.count("i")) # 1 (number of occurrences)
print(str*3) # krishnakrishnakrishna
print(str + " RadheRadhe") # krishna RadheRadhe
print(str[2]) # i (character at index 2)
print("   hello   ".strip()) # "hello" (removes leading/trailing spaces)

#lstrip() - removes left space
#rstrip() - removes right spaces

print("a,b,c,d,e".split(",")) # ['a', 'b', 'c', 'd', 'e']
print(",".join(['a', 'b', 'c', 'd', 'e'])) # "a,b,c,d,e"

