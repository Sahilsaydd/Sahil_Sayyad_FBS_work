## Write a program to check if a entered number is a palindrome or not 


def palindromeNumber(num):
    
    temp = num
    
    reversenumber = 0
    while (temp!= 0):
        
        d = temp%10
        reversenumber = reversenumber*10+d
        
        temp=temp//10
    if (reversenumber == num):
        
        print(f'{num} is a palindrome number')
    else:
        print(f'{num} is not a palindrome number')



n = int(input("Enter the number :"))
palindromeNumber(n)
