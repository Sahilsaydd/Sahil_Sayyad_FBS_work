def SelectionSort(li):
    for i in range(0,len(li)):
        mid_index =i
        for j in range(i+1,len(li)):
            if(li[j]<li[mid_index]):
                mid_index = j
        li[i],li[mid_index]=li[mid_index],li[i]
        print(li)
    return li


li = [21,434,563,2,655,24,7,97]
li = SelectionSort(li)
print(li)
        