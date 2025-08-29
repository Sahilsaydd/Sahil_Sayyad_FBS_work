# write a program to accept 3 digit number . if first digit is double of second digit and half of third digit then display "Yes" you have done it otherwise display plese try next time
## eg = 428 ,214
num = int(input("Enter a 3 digit number: "))

d1 = num//100
d2 = (num//10)%10
d3 = num%10

if(d1 == 2*d2 and d1 == d3/2):
        print("yes you hav done it")
else:
        print("please try next time")
