class Vehical:
    def __init__(self):
        print("Vehical")
    def v(self):
        print("this is vehical class")

class type(Vehical):
    def __init__(self):
        print("type")

    def t(self):
        print("vehical are in two type")

class Bike(type):
    def __init__(self):
        super().__init__()
        print("Bike")

    def b(self):
        print("This is bike class")


b1 = Bike()
b1.v()