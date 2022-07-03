
orders = int(input())

total = 0

for num in range(orders):

    price_per_capsule = float(input())
    days = int(input())
    caps_needed_per_day = int(input())
    if price_per_capsule <0.01 or price_per_capsule > 100.00:
        pass
    elif days <1 or days > 31:
        pass
    elif caps_needed_per_day < 1 or caps_needed_per_day > 2000:
        pass
        continue
    coffee_price = price_per_capsule * days * caps_needed_per_day
    print(f'The price for the coffee is: ${coffee_price:.2f}')
    total += coffee_price

print(f'Total: ${total:.2f}')




