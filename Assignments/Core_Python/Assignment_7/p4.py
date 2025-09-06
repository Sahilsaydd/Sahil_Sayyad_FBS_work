n = 5  # total rows

for i in range(1, n+1):  
    for j in range(1,n-i):
        print(" ",end="   ")

    # Increasing numbers
    val = i
    for j in range(i):
        print(f'{val}', end="  ")
        val += 1

    # Decreasing numbers
    val -= 2
    for j in range(i-1):
        print(val, end="  ")
        val -= 1

    print()

#             1  
#         2  3  2  
#     3  4  5  4  3
#    4  5  6  7  6  5  4
# 5  6  7  8  9  8  7  6  5