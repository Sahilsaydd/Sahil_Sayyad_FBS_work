## Write a program to check whether the given number is prime or not using recursive function

def is_prime_recursive(n, i=2):
	if n <= 1:
		return False
	if i * i > n:
		return True
	if n % i == 0:
		return False
	return is_prime_recursive(n, i + 1)

n = int(input("Enter a number: "))
if is_prime_recursive(n):
	print(f"{n} is a prime number.")
else:
	print(f"{n} is not a prime number.")