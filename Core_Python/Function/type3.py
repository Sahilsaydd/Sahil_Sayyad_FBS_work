## Without passing parameter (w/o input)
## With returning a value (w output)
def fact():
    num = int(input('Enter the number'))
    fact =1
    for i in range(1,num+1):
        fact = fact*i
    return fact  ## When we not return the value from the function is return the none

res = fact()
print("Factorial is ",res)