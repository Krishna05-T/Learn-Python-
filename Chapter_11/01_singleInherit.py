class Employee:
    company = "ITC Company"
    def show(self):
        print("Name of employee is : {self.name} and the salary : {salary}")

class Programmer(Employee):
    language = "Python"
    def show(self):
        print("Name of employee is : {self.name} and the salary : {salary}")
    def showLang(self):
        print(f"Language is used : {self.language}")


P = Programmer()
print(P.company)