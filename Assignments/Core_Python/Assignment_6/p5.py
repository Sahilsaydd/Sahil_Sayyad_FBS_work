for i in range(1,10):
    for j in range(1,11-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        if(i%2==0):
            continue
        else:
            print("*",end="   ")
    print()
    

#                   *   

#               *   *   *

#           *   *   *   *   *

#       *   *   *   *   *   *   *

#   *   *   *   *   *   *   *   *   *