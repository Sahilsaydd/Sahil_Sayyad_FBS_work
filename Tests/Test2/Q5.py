
p1 = int(input('Enter the product 1 price :'))
p2 = int(input('Enter the product 2 price'))

p3 = int(input('Enter the product 3 price '))

p4 = int(input('Enter product 4 price'))

p5 = int(input('Enter product 5 price'))


total = p1 + p2 + p3 + p4 + p5
bill_withgst = total*0.18

total_with_gst = total + bill_withgst
print(f'Without GST bill :{total}')
print(f'The total price is {total_with_gst}')