## Sum of all prime numbers between 1 to n

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def SumOfPrimeN(num):
    total = 0
    print("Prime numbers:", end=" ")
    for i in range(2, num + 1):
        if is_prime(i):
            print(i, end=" ")
            total += i
    print()  
    return total

num = int(input("Enter the number: "))
res = SumOfPrimeN(num)
print(f'The sum of prime numbers between 1 to {num} is : {res}')