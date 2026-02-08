class Employee:     # Class name is blueprint for creating object

    language = "python"    #class attributes
    salary = 1200000


krishna = Employee()
krishna.extra = "Java"  #instance attributes
print(krishna.language, krishna.salary)
print(krishna.extra)

