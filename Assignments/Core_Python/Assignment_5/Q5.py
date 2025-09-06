## Write a program to accept an integer amount from user and tell minimum number of notes needed to 
## for representing that amount (use looping to optimize the problem )

amount = int(input("Enter the Amount :"))

for i in range(1,6):
    if(amount>=2000):
        count = amount//2000
        print(f'{count} 2000 x',end=",  ")
        amount = amount%2000
    elif(amount>=500):
        count = amount//500
        print(f'{count} 500 x',end=",  ")
        amount = amount%500
    elif(amount>=200):
        count = amount//200
        print(f'{count} 200 x',end=",  ")
        amount = amount%200
    elif(amount>=100):
        count = amount//100
        print(f'{count} 100 x',end=",  ")
        amount =amount%100
    elif(amount>=50):
        count= amount//50
        print(f'{count} 50 x',end=",  ")
        amount =amount%50
