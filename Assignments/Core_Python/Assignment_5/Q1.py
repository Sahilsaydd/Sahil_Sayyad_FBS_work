## Write a program to prompt user to enter userid and password .
# if id and password is incorrect give him change to re enter the credentials.
# Let Him try after 3 times . After that program to terminate

userId = "Sahil"
password = "Sahil1234"
count = 0
while count < 3:
    uid = input("Enter User Id :")
    pid= input('Enter Password :')
    if(uid == userId and pid == password):
        print('Login successful')
        break
    else:
        print('invalid credentials')
        count +=1
        if count == 3:
            print('You have exceeded the limit ')
        else:
            print(f'you have {3-count} attempts left')