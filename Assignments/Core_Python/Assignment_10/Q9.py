## Write a program that having a N number of elements in the list and find out 
## Even and odd element in that list and then create the two separate
## lists which will have even element and others have odd elements

def EvenOdd(li):
    even =[]
    odd=[]
    for i in li:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    return even,odd


li = [10,11,12,13,14,15,16,17,18,19,20]

even,odd=EvenOdd(li)  
print(f'The original List is :{li}')
print(f"The Even Number list is : {even}")
print(f"The Odd Number list is : {odd}")