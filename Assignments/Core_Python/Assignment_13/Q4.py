## Python program to ganerate a dictionary that containds numbers (between 1 and n)in the form (x,x*x).
def generate_dict(n):
    my_dict = {}
    for i in range(1,n+1):
        my_dict[i] = i*i
    return my_dict

num = int(input("Enter the value of n :"))
result_dict = generate_dict(num)
print("The generated dictionary is :",result_dict)