a = int(input("Enter no. 1 : "))
b = int(input("Enter no. 2 : "))

if(b == 0):
    raise ZeroDivisionError("Hey you can't divide by zero")
else:
    print(f"The division a/b is {a/b}")