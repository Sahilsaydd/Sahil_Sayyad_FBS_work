## Write a program to take value from the user and print the value  

r =int(input('Enter the Rows :'))
c = int(input('Enter the column :'))
for i in range(1,r+1):
    for j in range(1,c+1):
        print('*', end=" ")
    print(i)