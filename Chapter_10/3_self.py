class Employee:     # Class name is blueprint for creating object
    language = "python"    #class attributes
    salary = 1200000

    def getInfo(self):
        print(f"language know is : {self.language}   and salary is {self.salary}")

krishna = Employee()

#print(krishna.language, krishna.salary)
krishna.getInfo()
#Employee.getInfo(krishna)

# it give error Employee.getInfo() takes 0 positional arguments but 1 was given 
#if we not use self

#self is a reference to the current instance of the class and is used to access variables that belong to the class.