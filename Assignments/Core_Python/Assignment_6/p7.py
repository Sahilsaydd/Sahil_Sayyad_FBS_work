for i in range(1,10):
    for j in range(1,11-i):
        print(" " ,end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end="   ")
    print()


#                   A   
#                 A   B   
#               A   B   C
#             A   B   C   D
#           A   B   C   D   E
#         A   B   C   D   E   F
#       A   B   C   D   E   F   G
#     A   B   C   D   E   F   G   H
#   A   B   C   D   E   F   G   H   I