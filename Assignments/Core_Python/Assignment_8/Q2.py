## Write a program to calculate area of circle 

def AreaOfCircle(r):
    return 3.14*r*r

radius = int(input("Enter the number ."))
res = AreaOfCircle(radius)
print(f'{res} is a area of circle')