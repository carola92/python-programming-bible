# cook your dish here

class Vehicle:#(object):
    speed = 0
    
    #def __new__(cls):
    #    return object.__new__(cls)
    
    def __init__(self, speed = 0):
        self.speed = speed
    
    def IncreaseSpeed(self, increaseAmount):
        self.speed += increaseAmount
        
    def __add__(self, otherVehicle):
        return Vehicle(self.speed + otherVehicle.speed)
        
    def __del__(self):
        print("Object has been destroyed")
        
class Car(Vehicle):
    weight = 10
    
    def IncreaseWeight(self, weight):
        self.weight += weight

    def IncreaseSpeed(self, increaseAmount):
        self.speed *= increaseAmount
        
car1 = Vehicle()
car2 = Vehicle(89)
childCar = Car(5)

print(childCar.weight)
childCar.IncreaseWeight(9)
print(childCar.weight)
childCar.IncreaseSpeed(5)
print(childCar.speed)

print("Speed for car1: %i" % car1.speed)
print("Speed for car2: %i" % car2.speed)
car1.IncreaseSpeed(5)
print("Speed for car1: %i" % car1.speed)
print("Speed for car2: %i" % car2.speed)

car3 = car1 + car2
print(car3.speed)

del car1

#print("Speed for car1: %i" % car1.speed)
#print("Speed for car2: %i" % car2.speed)