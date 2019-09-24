maximum = 100
minimum = 0.5
price = 7.49

order_amount = float(input("Enter cheese order weight (numeric value): "))

if order_amount > maximum:
    print(order_amount, "is more than currently available stock")
elif order_amount < minimum:
    print(order_amount, "is below minimum order amount")
else:
    res = order_amount * price
    print(order_amount,"costs $", res)

