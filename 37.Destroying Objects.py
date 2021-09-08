# cook your dish here

class Vehicle:#(object):
    speed = 0
    
    #def __new__(cls):
    #    return object.__new__(cls)
    
    def __init__(self, speed = 0):
        self.speed = speed
    
    def IncreaseSpeed(self, increaseAmount):
        self.speed += increaseAmount
        
    def __del__(self):
        print("Object has been destroyed")
        
car1 = Vehicle()
car2 = Vehicle(89)

print("Speed for car1: %i" % car1.speed)
print("Speed for car2: %i" % car2.speed)
car1.IncreaseSpeed(5)
print("Speed for car1: %i" % car1.speed)
print("Speed for car2: %i" % car2.speed)

del car1

print("Speed for car1: %i" % car1.speed)
print("Speed for car2: %i" % car2.speed)