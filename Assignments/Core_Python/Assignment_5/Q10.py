# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
## find the power of the n and calculate the sum

n = int(input('Enter the number :'))
sum =0

for i in range(1,n+1):
    sum +=n**i

print(f'The sum of the {n} power is {sum}')