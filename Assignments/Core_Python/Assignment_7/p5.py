# n=5

# for i in range(1,n):
#     for j in range(1,(n+1)-i):
#         print(" ",end="  ")
#     for j in range(1,i+1):
#         if( j==1 or j==i or i==n):
#            print(j,end="    ")
#         else:
#             print(" ",end="  ")
#     print()


n = 5
for i in range(1, n + 1):
    # spaces before numbers
      for j in range(n - i):
        print(" ", end=" ")
    # numbers in row
      for j in range(1, i + 1):
        if j == 1 or j == i or i == n:   # print first, last, and full last row
            print(j, end=" ")
        else:
            print(" ", end=" ")
      print()