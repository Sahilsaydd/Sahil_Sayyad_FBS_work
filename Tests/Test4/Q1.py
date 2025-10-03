### Write a function to which we pass a parameter  and print the factors of a given number 
## for eg. number =12  factors - 1,2,3,4,6,12

def print_factors(number):
    factors =[]
    for i in range(1, number +1):
        if(number%i==0):
            factors.append(i)
    return factors



print(print_factors(12))