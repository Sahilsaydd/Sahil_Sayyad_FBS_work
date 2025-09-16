class Car:
    def setData(self , brand, color , price):
        self.brand=brand
        self.color=color
        self.price=price
    
    def showData(self):
        res=f'\nBrand:{self.brand}\nColor:{self.color}\nPrice:{self.price}\n'
        return res
    
    def StartCar(self):
        print("Car Started.....")
    
    def StopCar(self):
        print("Car Stopped")
        
        
p1 = Car()
p1.setData("Toyota","Black",50000)
print(p1.showData())
p1.StartCar()
p1.StopCar()