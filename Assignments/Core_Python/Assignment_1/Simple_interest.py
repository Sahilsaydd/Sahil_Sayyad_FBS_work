## Write a program to calculate Simple interest
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
simple_interest = (p * r * t) / 100
print(f"The Simple Interest is: {simple_interest}")