## Write a program to print the list after removing the even number from the list

def remove_even_numbers(li):
    result =[]
    for i in li:
        if(i%2!=0):
            result.append(i)
    return result


li = [1,2,3,4,5,6,7,8,9,10]
result = remove_even_numbers(li)
print("The original list is :",li)
print("The list after removing even numbers is :",result)