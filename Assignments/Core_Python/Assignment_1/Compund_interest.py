### Write a program to calculate compound interest
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest (in %): "))
t = float(input("Enter time in years: "))
n = int(input("Enter number of times interest applied per time period: "))
compound_interest = p * ((1 + (r / (n * 100))) ** (n * t)) - p
print(f"The Compound Interest is: {compound_interest}")
