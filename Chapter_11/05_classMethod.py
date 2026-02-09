class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")

p1 = Employee()
p1.a = 45
p1.show()

# if want to show class value use class method