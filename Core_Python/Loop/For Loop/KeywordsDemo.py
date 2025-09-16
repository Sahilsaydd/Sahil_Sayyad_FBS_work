#1. pass - to neglect indentation started error
for i in range(1,10):
    pass 
print("Pass block")

#2. break - to terminate the loop forcefully
print()
for i in range(1,10):
    if(i==4):
        break
    print(i)


#3. Continue . - to stop the current iteration only

for i in range(1,11):
    if(i==4):
        continue
    print(i)

#4. else - this will execute only if loop will executed successfully

for i in range(1,11):
    if(i==4):
        continue
    print(i)
else:
    print("This is else block in looping.")