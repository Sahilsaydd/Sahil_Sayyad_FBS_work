# ## Write a to check the number is armstrong number or not 

# def dig_cnt(num):
#     cnt = 0 
#     while(num!=0):
#         d= num%10
#         cnt+=1
#         num//=10
#     return cnt

# def power(num,cnt):
#     powerOfDigit=1
#     while(num!=0):
#         d= num%10
#         powerOfDigit = d**cnt
#         num//=10
#     return powerOfDigit

# def sum_of_pow(powerOfDigit):
#     sum =0    
#     sum+= powerOfDigit
    
#     return sum


# def is_armstrong(num,sum):
#     if(num==sum):
#         print(f'{num} is a armstrong number.')
#     else:
#         print(f'{num} is not a armstrong number.')
    

# num=int(input("Enter the number :"))

# cnt =dig_cnt(num)
# p =power(num,cnt)
# sum_of_pow(p)
# is_armstrong(num,sum)


# Function to count digits
def dig_cnt(num):
    cnt = 0
    temp = num
    while temp != 0:
        cnt += 1
        temp //= 10
    return cnt

# Function to calculate sum of powers of digits
def sum_of_powers(num, cnt):
    temp = num
    total = 0
    while temp != 0:
        d = temp % 10
        total += d ** cnt   # add power of each digit
        temp //= 10
    return total

# Function to check Armstrong number
def is_armstrong(num):
    cnt = dig_cnt(num)             # step 1: count digits
    total = sum_of_powers(num, cnt) # step 2: calculate sum of powers
    
    if num == total:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is NOT an Armstrong number.")

# ----------- MAIN PROGRAM -----------
num = int(input("Enter the number: "))
is_armstrong(num)
