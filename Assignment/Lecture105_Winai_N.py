class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")


class Car(Vehicle):
    def sayHello(self):
        print("Hello World 4 reel Car")

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()
car1.sayHello()

pickUp1 = PickUp()
pickUp1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estateCar1 = EstateCar()
estateCar1.turnOnAirConditioner()