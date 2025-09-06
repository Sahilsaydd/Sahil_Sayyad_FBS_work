# for i in range(1,6):
#     for j in range(1,7-i):
#         print("*",end=" ")
    
#     val =1
#     for  j in range(1, i+1):
#         print(val,end="  ")
#         val = val*(i - j) // (j + 1)
#     print()

for i in range(1,6):
    for j in range(1,7-i):
        print(" ", end=" ")      # prints stars for spacing
    
    val = 1
    for j in range(0, i):
        print(val, end="  ")
        val = val * (i - j - 1) // (j + 1)
    print()
