# Dictionary is a collection of keys-value pairs 

d1 = {
    "Name" : "Krishan",
    "Surname": "Tirole",
    "age": 19,
    "Course": "B.Tech",
    "SGPA" : [8.85, 8.85],
    "City" : "Indore"
}

# print(d1["Name"], type(d1))
# print(d1["SGPA"])
#dict is mutable, unordered, indexed 
#cannot contain duplicate element


#Method

print(d1.items())   #Return a list of(key.value) tuples
print(d1.keys())    #Return a list containing dictionary's keys
print(d1.values())  #Return a list containing dictionary's values
(d1.update({"SGPA" : [8.85, 8.85, 9.0], "CGPA": 8.85})) #Update the dictionary with the specified key-value pairs
print(d1)

print(d1.get("rollNo")) #Return the value of the specified key if not present give none

# print(d1["rollNo"]) # This give error when key is not present

d2 = d1.copy()    # It return copy of the dictionary
print("heloo")
print(d2)
print("\n")
keys = ["a", "b", "c"]
d2 = dict.fromkeys(keys, 8) # Creates a new dictionary from given keys and a single value.
print(d2)


print("\n")

value = d2.pop("a") # It return remove value of key enter 
print(value)

print("\n")
print(d1)
value = d1.popitem() # Remove and returns the last inserted key-value pair
print(value)

d1.setdefault("Collage", "IPS ACADEMY")
print(d1)


d2.clear()
print(d2)   #Clear all key-value pair

print("age" in d1) #return boolean value key is present or not

print(len(d1))