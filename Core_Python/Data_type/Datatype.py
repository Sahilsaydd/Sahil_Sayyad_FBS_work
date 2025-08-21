#Numeric
#Int
x=10
print(type(x))
print("\n")


#float
x =3.14
print(type(x))
print("\n")

#complex 
x = 10+5j
print(type(x))
print(x.real)
print(x.imag)
print("\n")

# string
x='FirstBit Solutions'

print(type(x))
print("\n")

x="This is demo."
print(type(x))
print("\n")

x='''This is First Line 
This is second Line
This is Third Line'''
print(type(x))
print("\n")



"""This is Multiline Comments"""


x="""This is first line

This is next line"""

print(type(x))
print("\n")


## Sequentials
#1 . List 
x=[1,2,"abc",3.14]
print(type(x))
print("\n")

#2 . Tuple
x= (1,2,"abx",3.14)
print(type(x))
print("\n")

#3.Range
x = range(1,11)
print(type(x))

print("Range Datatype",x)

### SetType
#1 .Set

x= {1,2,"abc",3.14}
print(x)
print(type(x))
print("\n")


#2. FrozenSet

x = frozenset({1,2,'abc',3.14})
print(x)
print(type(x))

print("\n")

## Mapping
#1. Dict 
x = {"Name":"Sahil Sayyad","Dept":"Learning"}
print(x)
print(type(x))


#Boolean
#1. True 
x= True
print(x)
print(type(x))
print("\n")
#2. False
x= False
print(x)
print(type(x))
print("\n")

### None

x= None
print(x)
print(type(x))
print("\n")

##Mapping
#1. Dict
x= {"name":"Sahil Sayyad", "age":20, "dept":"Learning"}
print(x)
print(type(x))