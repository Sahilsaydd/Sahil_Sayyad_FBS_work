li = [[10,20,30],[40,50,60]]

# Research om how to iterate the individual ele from the list
# li2 = [10,[20,30,[40,50]],[60,70,80]]
print(li[0][2])
for l in li:
    for ele in l:
        print(ele,end=" ")
        
        
li2 = li.copy()
li[0][1]=100
print(li2)