class Vehical:
    def v(self):
        print("This is vehical class")

class Bike(Vehical):
    def b(self):
        print("This is Bike class")

class Type(Bike):
    def t(self):
        print("Bullet Bike")


veh = Vehical()
veh.v()

bike = Bike()
bike.v()
bike.b()


java = Type()
java.v()
java.b()
java.t()
