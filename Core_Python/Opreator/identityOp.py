#identity Opreator
#Identity operators are used to compare the memory location of two objects.
#1. is
x=10
y=20
z=10
list1=[1,2,3]
list2 =[1,2,3]
print(x is y)   # False, because x and y are not the same object
print(x is z)   # True, because x and z are the same object
print(list1 is list2)  # False, because list1 and list2 are different objects with the same content

#2. is not
print(x is not y) # True, because x and y are not the same object 
print(x is not z) # False , beacuse x and z are the same object
print(list1 is not list2) # True, because list1 and list2 are different objects
