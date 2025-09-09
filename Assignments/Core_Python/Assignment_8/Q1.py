## Write a program to calculate area of rectangle 

def calculateAreaRectangle(l,w):
    return l*w

length = int(input("Enter the length :"))
width = int(input('Enter the width :'))

res = calculateAreaRectangle(length,width)
print(f'The area of rectangle is {res}')
    