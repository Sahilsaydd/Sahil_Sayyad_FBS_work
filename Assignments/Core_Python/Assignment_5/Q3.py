## Accept the the number of passengers from user and per ticket cost 
## Then accept the age of each passenger and then calculate the total amount 
## to travel for all of them based on the following condition
## a . children below 12 = 30% discount
## b. Senior citizen above 59 = 50% discount
# c. others need to pay full.

n =int(input('Enter number of passengers:'))
ticket_cost = 1000
total_cost =0
for i in range(1,n+1):
    age = int(input(f'Enter age of passenger {i}:'))
    if(age<12):
        d=  ticket_cost*0.30 
        cost = ticket_cost - d
        print(cost)
    elif(age>59):
        d =  ticket_cost*0.50
        cost = ticket_cost - d
        print(cost)
    else:
        cost = ticket_cost
        print(cost)
    total_cost+=cost
print(f'Total ticket cost for {n} passengers is {int(total_cost)}')