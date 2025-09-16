### Constructor 
#1. Special/ Magical method which calls automatically
# when object of that class is created.
# 1. __init__ is  the name of constructor
 ## At the time of object creating you need specify the value  ( )
 
 ##  Type of constructor 
#   1. Default Constructor
#   2. parameter constructor
 
class Car:
    def __init__(self,brand="",color="",price=0):
        self.brand=brand
        self.color=color
        self.price=price
    
    def showData(self):
        Data=f'\nBrand:{self.brand}\nColor:{self.color}\nPrice:{self.price}\n'
        return Data
    
    def StartCar(self):
        print("Car Started.....")
    
    def StopCar(self):
        print("Car Stopped")
        
        
p1 = Car()
# p1.setData("Toyota","Black",50000)
print(p1.showData())
p1.StartCar()
p1.StopCar()