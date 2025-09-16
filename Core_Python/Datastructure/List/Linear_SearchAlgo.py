## Write a program of the linearSearch algorithm to find the number in a given list .

def LinearSearch(ele,li):
    for i in range(0,len(li)):
        if(ele==li[i]):
            return i
    else:
        None
        
li =[10,20,30,40,50,60,70,80,90,100]
ele = int(input('Enter the number : '))

res = LinearSearch(ele,li)
if(res!=None):
    print(f'{ele} is element is present on {res} this index')
else:
    print(f'{ele} is not present in this list.')