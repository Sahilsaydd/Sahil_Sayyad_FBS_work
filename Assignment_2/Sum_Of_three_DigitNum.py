num =123
print("The Three Digit Number is :", num)
digit1 = num//100
#First Place Value 10Th Position
print("First Digit :", digit1)
digit2 = (num//10)%10
print("Second Digit :", digit2)
#second  Place Value 10th Position
digit3 = num%10
sum_of_digits = digit1+digit2+digit3
print("Third Digit", digit3)
print("Sum of the digits of the three-digit number is :", sum_of_digits)
