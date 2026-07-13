def apply_discount(price, discount=0.05):
    price = price - (price * discount)
    return price

def apply_tax(price, tax=0.07):
    price = price + (price * tax)
    return price

def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    total_price = apply_tax(discounted, tax)
    return total_price

print(f"Total cost with default discount and tax: ${calculate_total(120)}")
print(f"Total cost with custom discount and tax: ${calculate_total(100, discount=0.10, tax=0.08)}")
