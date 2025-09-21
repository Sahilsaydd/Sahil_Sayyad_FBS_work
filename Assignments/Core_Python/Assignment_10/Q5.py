## Accept the number from user and check if this element is present in this list or not 
## Also tell how many times it is present in the list

def SearchNumber(ele,li):
    count =0
    for i in range(0,len(li)):
        if(ele==li[i]):
            count+=1
        else:
            None
    
    return ele ,count

        

li =[10,20,30,40,40,40,40,40,90,100]
element = int(input("Enter the number to check that the number is present in the list or not ."))
ele,count=SearchNumber(element,li)
print(f"The {ele} is present No. of Times {count} in a list")