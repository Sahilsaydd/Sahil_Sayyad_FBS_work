## Accept age of five people and also per person ticket amount and the calculate total
## amount ticket to travel for all of them based on following condition
## a. children below 12 = 30% discount
## b. senior citizen above 59% = 50% Discount
## c . others need to pay full

p1_age = int(input('Enter age of person 1 :'))
p1_ticket = float(input('Enter ticket amount of person 1 :'))


p2_age = int(input('Enter age of person 2 :'))
p2_ticket = float(input('Enter ticket amount of person 2 :'))


p3_age = int(input('Enter age of person 3 :'))
p3_ticket = float(input('Enter ticket amount of person 3 :'))


p4_age = int(input('Enter age of person 4 :'))
p4_ticket = float(input('Enter ticket amount of person 4 :'))


p5_age = int(input('Enter age of person 5 :'))
p5_ticket = float(input('Enter ticket amount of person 5 :'))

total_ticket_amt = p1_ticket+p2_ticket+p3_ticket+p4_ticket+p5_ticket

print(f'{total_ticket_amt} is a total amount of all 5 person')

if(p1_age<12):
    p1_ticket = p1_ticket - (p1_ticket*30/100)
elif(p1_age>59):
    p1_ticket = p1_ticket - (p1_ticket*50/100)
else:
    p1_ticket = p1_ticket
print(f'{p1_ticket} is a ticket amount of person 1 after discount')

if(p2_age<12):
    p2_ticket = p2_ticket - (p2_ticket*30/100)
elif(p2_age>59):
    p2_ticket = p2_ticket - (p2_ticket*50/100)
else:
    p2_ticket = p2_ticket
print(f'{p2_ticket} is a ticket amount of person 1 after discount')
if(p3_age<12):
    p3_ticket = p3_ticket - (p3_ticket*30/100)
elif(p3_age>59):
    p3_ticket = p1_ticket - (p3_ticket*50/100)
else:
    p3_ticket = p3_ticket
print(f'{p3_ticket} is a ticket amount of person 1 after discount')
if(p4_age<12):
    p4_ticket = p4_ticket - (p4_ticket*30/100)
elif(p4_age>59):
    p4_ticket = p4_ticket - (p4_ticket*50/100)
else:
    p4_ticket = p4_ticket
print(f'{p4_ticket} is a ticket amount of person 1 after discount')
if(p5_age<12):
    p5_ticket = p5_ticket - (p5_ticket*30/100)
elif(p5_age>59):
    p5_ticket = p5_ticket - (p5_ticket*50/100)
else:
    p5_ticket = p5_ticket
print(f'{p5_ticket} is a ticket amount of person 1 after discount')

total_amt_after_discout  = p1_ticket+p2_ticket+p3_ticket+p4_ticket+p5_ticket
print(f'{total_amt_after_discout} is a total amount of all 5 person after discount')
print(f'{total_ticket_amt-total_amt_after_discout} is a total discount amount of all 5 person')
