## Write a program to print the following patterns :
def print_z_pattern(n):
    # First row (straight line of stars)
    for i in range(n):
        print("*", end="")
    print()

    # Middle rows (diagonal)
    for i in range(n-2):
        for j in range(n-2-i):
            print(" ", end="")
        print("*")

    # Last row (straight line of stars)
    for i in range(n):
        print("*", end="")
    print()


# Driver code
size = int(input("Enter size of Z pattern: "))
print_z_pattern(size)
