## Write a python program print 1 to 100 in snake and ladder pattern

def print_snake_ladder(n):
    for i in range(n):
        if(i%2==0):
            for j in range(1,11):
                print(i*10+j,end=" ")
        else:
            for j in range(10,0,-1):
                print(i*10+j,end=" ")
        print()
        
        

n  = 10
print_snake_ladder(n)
