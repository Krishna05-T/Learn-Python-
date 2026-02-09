class Employee:
    def emp(self):
        print("This is employee class")

class Coder:
    def code(self):
        print("This is coder class")

class person(Employee, Coder):
    name = ""



p1 = person()
p1.emp()
p1.code()