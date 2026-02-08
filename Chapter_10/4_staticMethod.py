
class Employee:     # Class name is blueprint for creating object

    language = "python"    #class attributes
    salary = 1200000

    @staticmethod
    def greet():
        print("Good morning")
#we make a method static when we don't need to access any instance-specific data

krishna = Employee()
krishna.greet()  # Output: Good morning