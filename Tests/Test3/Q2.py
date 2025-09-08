## Write a program to calculate the sum of series 

#1/1!+2/2!+3/3!+4/4!+...n/n!

n = int(input('Enter the value of n: '))
series_sum = 0
for i in range(1, n+1):
	fact = 1
	for j in range(1, i+1):
		fact *= j
	series_sum += i / fact
print(f'Sum of the series is: {series_sum}')

