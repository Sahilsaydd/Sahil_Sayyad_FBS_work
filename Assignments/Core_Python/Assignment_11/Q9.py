##9. Write a program to create three lists of numbers, their squares and cubes

def Calculate_square_cube(li):
    square =[]
    cube =[]
    for i in li:
        square.append(i**2)
        cube.append(i**3)
    return square,cube



li = [1,2,3,4,5,6,7,8,9]
square , cube = Calculate_square_cube(li)
print("List of numbers :",li)
print("List of squares :",square)
print("List of Cubes :",cube)
