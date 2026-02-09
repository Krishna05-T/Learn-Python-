class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")
    
    #This makes name behave like a variable but actually runs a function.
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        value = value.split(" ")
        self.fname = value[0]
        self.lname = value[1] 

p1 = Employee()
p1.a = 45
p1.show()

p1.name = "Krishna Tirole"
print(p1.name)

