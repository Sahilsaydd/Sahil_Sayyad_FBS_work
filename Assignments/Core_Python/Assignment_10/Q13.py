## Write a program to print the list after removing the even numbers

def RemoveEvenNumber(li):
    result = []
    for i in li:
        if(i%2!=0):
            result.append(i)
    return result


li =[10,11,12,13,14,15,16,17,18,19,20]
result = RemoveEvenNumber(li)
print("The Odd numbers are :", result)
    