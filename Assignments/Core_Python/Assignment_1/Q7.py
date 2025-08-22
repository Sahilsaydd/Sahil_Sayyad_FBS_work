## Write program to input two angles from user and
# find third angle of the triangle


a1 = float(input("Enter first angle of triangle: "))
a2 = float(input("Enter second angle of triangle: "))
a3 = 180 - (a1 + a2)
print(f"The third angle of the triangle is: {a3}")