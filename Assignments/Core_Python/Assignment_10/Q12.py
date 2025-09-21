## Write a program to create three list of numbers , their squares and cubes 
def SquareCubes(li):
    Square = []
    Cubes = []
    for i in li:
        Square.append(i*i)
        Cubes.append(i**3)
    return Square,Cubes


li = [1,2,3,4,5]
Square,cubes = SquareCubes(li)
print("The Original lists :",li)
print("The Square :",Square)
print("The Cubes :",cubes)