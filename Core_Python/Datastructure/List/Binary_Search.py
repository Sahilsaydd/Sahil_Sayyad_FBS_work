def BinarySearch(ele, li):
    beg = 0 
    end = len(li)-1
    while(beg<=end):
        mid = (beg+end)//2
        if(ele == li[mid]):
            return mid
        elif(ele > li[mid]):
            beg = mid+1
        elif(ele<li[mid]):
            beg = mid-1
    else:
        return None

li = [10,20,30,40,50,60]
ele = int(input("Enter ele for search :"))

res = BinarySearch(ele, li)
if(res!=None):
    print(f'{ele} is present at index {res}')
else:
    print(f'{ele} is not present in the list')