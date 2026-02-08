class Employee:     # Class name is blueprint for creating object
    
    language = ""    #class attributes
    salary = 0

    def __init__(self, language, salary):
        print("Welcome")
        self.language = language
        self.salary = salary


krishna = Employee("Python", 1500000)
print(krishna.language, krishna.salary)

