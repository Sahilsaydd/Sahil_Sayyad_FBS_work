for i in range(5,0,-1):
    for j in range(1,i+1):
        if(j==1 or j==i or i==5):
            print(i, end=" ")
        else:
            print(' ',end=" ")
    print()