## python program to put to even and odd  elements of a list into  two different lists

def evenoddlist(li):
    even =[]
    odd = []
    for i in li:
        if(i%2==0):
            even.append(i)
        else:
            odd.append(i)
    return even,odd


li = [10,11,12,13,14,15,16,17,18,19,20]

even,odd=evenoddlist(li)
print("The Original List :",li)
print("The Even List :",even)
print("The Odd List",odd)