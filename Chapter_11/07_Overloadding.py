class Number:
    n = 0
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n


a = Number(1)
b = Number(2)

print(a+b)


class string:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"
    

p1 = string("Krishna")
print(p1)


class Len:
    def __init__(self, member):
        self.member = member
    
    def __len__(self):
        return len(self.member)
    

team = Len(["1","2", "3"])
print(len(team))
