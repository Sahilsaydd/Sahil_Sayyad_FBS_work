def BubbleSort(li):
    for i in range(1,len(li)):
        for j in range(0,len(li)-i):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
                print(li,i)
    return li


li  = [60,50,40,30,20,10]
li = BubbleSort(li)
print(li)