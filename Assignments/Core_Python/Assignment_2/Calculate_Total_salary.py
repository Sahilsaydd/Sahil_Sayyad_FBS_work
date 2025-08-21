salary=20000
da=20
ta=10
hra=5
#Calculate The da , ta, hra
daAMt =(salary * da)/100
taAmt=(salary*ta)/100
hraAmt=(salary*hra)/100
print("DA Amount :", daAMt)
print("TA Amount :", taAmt) 
print("HRA Amount :", hraAmt)

#Calculate The Total Salary
totalsalary = salary+daAMt+taAmt+hraAmt
print("Total Salary :",totalsalary)