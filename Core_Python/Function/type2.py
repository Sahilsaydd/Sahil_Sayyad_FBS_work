## With passing parameter (w input)
## without returning a value (w/o output)

def checkPrime(num):
    for i in range(2, num//2+1):
        if(num%i==0):
            print(f'{num} is not a prime number ')
            break
        else:
            print(f'{num} is a prime number .')
            break

n= int(input("Enter the number : "))
checkPrime(n)