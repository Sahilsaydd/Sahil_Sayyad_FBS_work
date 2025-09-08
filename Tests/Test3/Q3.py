## Write a program to accept basic salary of n emp (n should be accepted from user ). 
## If basic salary is below  20000 then da =10$ and hra =15% otherwise da =15% ta=18% and
##hra = 20% .
## Based on this salary calculate the total salary of each emp and also total salary of all emp .

n = int(input('Enter number of employees: '))
total_all_emp = 0.0
for i in range(1, n+1):
	basic = int(input(f'Enter basic salary for employee {i}: '))
	if basic < 20000:
		da = basic * 0.10
		hra = basic * 0.15
		ta = 0
	else:
		da = basic * 0.15
		hra = basic * 0.20
		ta = basic * 0.18
	total_salary = basic + da + hra + ta
	print(f'Total salary for employee {i}: {total_salary}')
	total_all_emp += total_salary
print()
print(f'Total salary of all employees: {total_all_emp}')
