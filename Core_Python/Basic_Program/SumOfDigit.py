num = int(input("Enter a number:"))

n1 = num%10
print(f"The last digit is {n1}")
num = num//10
print(f"After removing the last digit, the number is {num}")
n2 = num%10
print(f"The second last digit is {n2}")
num = num//10
print(f"After removing the second last digit, the number is {num}")
n3 = num%10
print(f"The third last digit is {n3}")

num = num//10
print(f"After removing the third last digit, the number is {num}")

sumofdigit= n1+n2+n3
print(f"The sum of the digits is {sumofdigit}")