# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
n = int(input("Enter the Number :"))
sum = 0
for i in range(1,11):
    term = (n**i)/i
    sum =+term
print(f'The sum of a series is {sum}')