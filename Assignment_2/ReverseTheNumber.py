num = int(input("Enter a three-digit number:"))
print("The Three Digit Number is :", num)
n1 = num//100
# First Place Value 100th Position
print("First Digit :", n1)
n2 =(num//10)%10
print("Second Digit :", n2)
# Second Place Value 10th Position
n3 = num%10
print("Third Digit :", n3)

reverse_number = n3*100+n2*10+n1
print("The Reverse of the Three Digit Number is :", reverse_number) 

