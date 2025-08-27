## Input 5 subject marks from user and display the Grade (Eg.. First class, second class)

sub1 = int(input('Enter marks of subject 1 :'))
sub2= int(input('Enter marks of subject 2 :'))
sub3 = int(input('Enter marks of subject 3'))
sub4 = int(input('Enter marks of subject 4:'))
sub5 = int(input('Enter marks of subject 5 :'))
total = sub1+sub2+sub3+sub4+sub5
avg = total/5
print('Total Marks :',total)
print('Average Marks :',avg)
if(avg>=90):
    print('Grade : A+')
elif(avg>=80):
    print('Grade : A')
elif(avg>=70):
    print('Grade : B+')
elif(avg>=60):
    print('Grade : B')
elif(avg>=50):
    print('Grade : c')
elif(avg>=40):
    print('Grade : D')
else:
    print('Grade :F')