class Person:
    def setData(self,nm,a,add):
        self.name=nm
        self.age = a
        self.add=add
    
    def displayData(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Add :",self.add)
        print("####################################################")
        
        
p1 = Person()
p1.setData("Sachin",57,"Pune")
p1.displayData()

p2 = Person()
p2.setData("Sahil",21,"Ahmednagar")
p2.displayData()
