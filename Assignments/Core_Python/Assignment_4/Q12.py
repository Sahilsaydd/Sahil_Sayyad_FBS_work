## Write a program to check the number is armstrong or not
n = int(input('Enter the number: '))
original_number = n
cnt = 0
temp = n

# Count the number of digits
while temp > 0:
    cnt += 1
    temp //= 10

sum = 0
temp = n
while temp > 0:
    d = temp % 10
    sum += d ** cnt
    temp //= 10

if sum == original_number:
    print(f'{original_number} is an Armstrong number')
else:
    print(f'{original_number} is not an Armstrong number')