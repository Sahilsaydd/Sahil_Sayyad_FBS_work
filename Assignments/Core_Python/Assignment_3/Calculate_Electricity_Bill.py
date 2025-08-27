# Program to calculate electricity bill

units = int(input("Enter electricity units consumed: "))

# calculate bill according to slabs
if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = (50 * 0.50) + (units - 50) * 0.75
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 250) * 1.50

# add 20% surcharge
total_bill = bill + (bill * 0.20)

print(f"Total Electricity Bill: Rs. {total_bill:.2f}")